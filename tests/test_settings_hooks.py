"""Execute template handlers with real stdin; no Claude/model invocation needed."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SETTINGS = REPO / "templates" / "settings"
CONFIG = json.loads((SETTINGS / "hooks.json").read_text(encoding="utf-8"))


class HookIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hook project ")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.configure_project(self.project)

    def configure_project(self, project):
        self.project = project
        hook_dir = self.project / ".claude" / "hooks"
        hook_dir.mkdir(parents=True, exist_ok=True)
        for script in SETTINGS.glob("*.py"):
            shutil.copy2(script, hook_dir / script.name)
        self.env = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.project),
                        PYTHONDONTWRITEBYTECODE="1")

    def run_hook(self, event, tool, path, cwd=None, raw=None):
        key = "notebook_path" if tool == "NotebookEdit" else "file_path"
        payload = {"hook_event_name": event, "tool_name": tool,
                   "cwd": str(cwd or self.project), "tool_input": {key: str(path)}}
        results = []
        for group in CONFIG["hooks"][event]:
            if not re.fullmatch(group["matcher"], tool):
                continue
            for handler in group["hooks"]:
                self.assertEqual(handler["type"], "command")
                # Only the interpreter is adapted to this machine. The real
                # configured script path and arguments are otherwise unchanged.
                self.assertEqual(handler["command"], "python")
                args = [arg.replace("${CLAUDE_PROJECT_DIR}", str(self.project))
                        for arg in handler["args"]]
                results.append(subprocess.run(
                    [sys.executable, *args], input=raw if raw is not None else json.dumps(payload),
                    text=True, capture_output=True, cwd=self.project, env=self.env,
                    timeout=handler["timeout"], check=False))
        self.assertEqual(len(results), 1, "Expected one matching template handler")
        return results[0]

    def test_normal_file_tools_are_not_preapproved_or_blocked(self):
        for tool in ("Read", "Edit", "Write", "NotebookEdit"):
            with self.subTest(tool=tool):
                result = self.run_hook("PreToolUse", tool, self.project / "normal.py")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, "")  # no permissionDecision=allow

    def test_relative_path_uses_input_cwd(self):
        nested = self.project / "nested"
        nested.mkdir()
        result = self.run_hook("PreToolUse", "Write", "normal.py", cwd=nested)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_sensitive_names_above_project_files_are_not_blocked(self):
        original = self.project
        for relative in (".env-project", "archive.key/project", "archive.pem/.env-project"):
            with self.subTest(relative=relative):
                self.configure_project(original / relative)
                result = self.run_hook("PreToolUse", "Read", self.project / "README.md")
                self.assertEqual(result.returncode, 0, result.stderr)
                sensitive = self.run_hook("PreToolUse", "Read", self.project / ".env.local")
                self.assertEqual(sensitive.returncode, 2, sensitive.stderr)

    def test_symlinked_project_uses_matching_entry_and_resolved_roots(self):
        real_project = self.project / "archive.key" / "real"
        self.configure_project(real_project)
        entry = Path(self.temp.name) / ".env-project"
        try:
            entry.symlink_to(real_project, target_is_directory=True)
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"This host cannot create symlinks: {type(error).__name__}")
        self.configure_project(entry)
        for root in (entry, real_project):
            with self.subTest(root=root):
                result = self.run_hook("PreToolUse", "Read", root / "README.md", cwd=root)
                self.assertEqual(result.returncode, 0, result.stderr)
                sensitive = self.run_hook("PreToolUse", "Read", root / ".env.local", cwd=root)
                self.assertEqual(sensitive.returncode, 2, sensitive.stderr)

    def test_nested_sensitive_paths_are_denied(self):
        for name in (".env", "nested/.env.local", "nested/.ENV", "cert.pem", "key.key"):
            for tool in ("Read", "Edit", "Write", "NotebookEdit"):
                with self.subTest(name=name, tool=tool):
                    result = self.run_hook("PreToolUse", tool, self.project / name)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn("File policy denied", result.stderr)

    def test_outside_and_parent_traversal_are_denied(self):
        for target in (self.project.parent / "outside.py", "../outside.py",
                       Path(str(self.project) + "-sibling") / "file.py"):
            with self.subTest(target=target):
                result = self.run_hook("PreToolUse", "Write", target)
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_outside_cwd_is_denied(self):
        result = self.run_hook("PreToolUse", "Read", "file.py", cwd=self.project.parent)
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_sensitive_symlink_target_is_denied(self):
        secret = self.project / ".env.private"
        secret.write_text("DUMMY_ONLY", encoding="utf-8")
        alias = self.project / "ordinary.txt"
        try:
            alias.symlink_to(secret)
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"This host cannot create symlinks: {type(error).__name__}")
        result = self.run_hook("PreToolUse", "Read", alias)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertNotIn("DUMMY_ONLY", result.stdout + result.stderr)

    def test_malformed_input_is_denied(self):
        for raw in ("not json", "null", "[]", "{}", '{"tool_input": null}'):
            with self.subTest(raw=raw):
                result = self.run_hook("PreToolUse", "Read", "file.py", raw=raw)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_post_check_does_not_execute_python(self):
        target = self.project / "normal.py"
        marker = self.project / "executed.txt"
        target.write_text("from pathlib import Path\nPath('executed.txt').touch()\n",
                          encoding="utf-8")
        result = self.run_hook("PostToolUse", "Write", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(marker.exists())

    def test_syntax_failure_is_reported_and_edit_remains(self):
        target = self.project / "broken.py"
        content = "def missing_colon()\n    return 1\n"
        target.write_text(content, encoding="utf-8")
        result = self.run_hook("PostToolUse", "Edit", target)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("syntax check failed at line 1", result.stderr)
        self.assertEqual(target.read_text(encoding="utf-8"), content)

    def test_non_python_edit_is_not_syntax_checked(self):
        target = self.project / "notes.md"
        target.write_text("# not Python", encoding="utf-8")
        result = self.run_hook("PostToolUse", "Write", target)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_python_file_is_reported(self):
        result = self.run_hook("PostToolUse", "Edit", self.project / "missing.py")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("could not run", result.stderr)

    def test_pre_guard_has_handler_level_failure_policy(self):
        for group in CONFIG["hooks"]["PreToolUse"]:
            self.assertNotIn("command", group)
            for handler in group["hooks"]:
                self.assertEqual(handler["onFailure"], "block")


if __name__ == "__main__":
    unittest.main()

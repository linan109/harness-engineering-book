"""Shared path validation for the companion file-tool hooks (Python 3.10+)."""

import json
import os
from pathlib import Path
import sys


def load_target(expected_event, allowed_tools):
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict):
        raise ValueError("Hook input must be an object")
    if payload.get("hook_event_name") != expected_event:
        raise ValueError("Unexpected hook event")
    if payload.get("tool_name") not in allowed_tools:
        raise ValueError("Unexpected file tool")
    project_entry = Path(os.environ["CLAUDE_PROJECT_DIR"]).absolute()
    project = project_entry.resolve()
    cwd = Path(payload["cwd"])
    if not cwd.is_absolute() or not cwd.resolve().is_relative_to(project):
        raise ValueError("Working directory is outside the configured project")
    inputs = payload["tool_input"]
    key = "notebook_path" if payload["tool_name"] == "NotebookEdit" else "file_path"
    raw = inputs[key]
    if not isinstance(raw, str) or not raw or "\x00" in raw:
        raise ValueError("Missing or invalid file path")
    target = Path(raw)
    if not target.is_absolute():
        target = cwd / target
    resolved = target.resolve()
    if not resolved.is_relative_to(project):
        raise ValueError("File is outside the configured project")
    # The configured entry may itself be a symlink. Exclude the project root
    # and its ancestors in both spellings, while retaining in-project aliases.
    try:
        raw_relative = target.relative_to(project_entry)
    except ValueError:
        raw_relative = target.relative_to(project)
    resolved_relative = resolved.relative_to(project)
    # An innocently named in-project symlink can still point to .env.
    for part in (*raw_relative.parts, *resolved_relative.parts):
        name = part.casefold()
        if name.startswith(".env") or name.endswith((".pem", ".key")):
            raise ValueError("Sensitive file paths are excluded by this template")
    return resolved


def report_failure(message):
    # Do not echo the payload, file contents, or secret values into logs.
    print(message, file=sys.stderr)
    return 2

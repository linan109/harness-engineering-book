"""PreToolUse guard: reject sensitive or out-of-project file-tool targets."""

from hook_paths import load_target, report_failure


def main():
    try:
        load_target("PreToolUse", {"Read", "Edit", "Write", "NotebookEdit"})
    except (ValueError, TypeError, KeyError, OSError, RuntimeError):
        return report_failure("File policy denied: sensitive/outside path or invalid hook input.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

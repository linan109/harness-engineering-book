"""PostToolUse demonstration: syntax check the changed .py file without executing it."""

import tokenize

from hook_paths import load_target, report_failure


def main():
    try:
        target = load_target("PostToolUse", {"Edit", "Write"})
        if target.suffix.casefold() != ".py":
            return 0
        with tokenize.open(target) as source:
            compile(source.read(), str(target), "exec")
    except SyntaxError as error:
        return report_failure(
            f"Python syntax check failed at line {error.lineno}. "
            "The edit already happened; inspect and repair it, then rerun checks."
        )
    except (ValueError, TypeError, KeyError, OSError, RuntimeError, UnicodeError):
        return report_failure("Python syntax check could not run; inspect the hook input and file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

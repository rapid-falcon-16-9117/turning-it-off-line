"""Entry for make.fun's "Have You Tried Turning It Off?" bounty.

The whole act is one line: the thing a hopeless tech support agent says
to a desperate customer, written to ``entry.txt`` in the output
directory so the comedy judge can read it. No network, no input, no
state -- the program resolves where to write, writes the line, and
leaves.

The output directory is the ``MAKEFUN_OUTPUT_DIR`` environment variable
when set, and ``/output`` otherwise.
"""

import os
from pathlib import Path

# The line itself. One reply, under the competition's character cap,
# with the twist where the brief wants it: the agent's cheerful
# uselessness, never the customer, is the joke.
LINE = (
    "I know, I know \u2014 turn it off and on again. It fixes the computer "
    "about half the time, but those thirty seconds of silence fix me "
    "every single time."
)


def output_file() -> Path:
    """Where the entry text goes: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    return out_dir / "entry.txt"


# The gate's limits, from the competition rules: the entry text must be
# 1 to 199 characters and not only white space. The program checks its
# own line against them before writing, so a careless future edit to
# LINE fails loudly here instead of scoring a silent 0 out there.
MIN_LINE_CHARS = 1
MAX_LINE_CHARS = 199


def check_line(line: str) -> None:
    """Refuse to write a line the gate would refuse to judge."""
    if not MIN_LINE_CHARS <= len(line) <= MAX_LINE_CHARS:
        raise SystemExit(
            f"line is {len(line)} characters; "
            f"the gate allows {MIN_LINE_CHARS}..{MAX_LINE_CHARS}"
        )
    if not line.strip():
        raise SystemExit("line is only white space; the gate allows none")


def main() -> None:
    check_line(LINE)
    target = output_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    # Just the line: no trailing newline, so the file the gate measures
    # is exactly the text the judge reads.
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()

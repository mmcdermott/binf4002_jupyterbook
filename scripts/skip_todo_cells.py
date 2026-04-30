#!/usr/bin/env python3
"""For TODO cells with ??? placeholders that we don't have automatic
solutions for, replace the cell source with a `print()` statement noting that
this exercise is intentionally left unrun. The downstream cells will then run.

Used for labs 12-16 where the inline_solutions.py heuristic doesn't apply.
"""
import json, sys, re
from pathlib import Path


def get_source(cell):
    s = cell.get("source", "")
    return "".join(s) if isinstance(s, list) else s


def main():
    for path in sys.argv[1:]:
        p = Path(path)
        nb = json.loads(p.read_text())
        n_skipped = 0
        for c in nb["cells"]:
            if c.get("cell_type") != "code":
                continue
            src = get_source(c)
            if "???" in src:
                # Pull out the section header / brief description from the cell
                first_lines = "\n".join(src.splitlines()[:10])
                heading = ""
                m = re.search(r"^#\s*[─━═]+\s*\n#\s+(.+?)\s*[─━═]*\s*$", first_lines, re.MULTILINE)
                if m:
                    heading = m.group(1).strip()
                msg = (heading or "Exercise cell skipped in book build").replace("'", "")
                new_src = (
                    "# This is an exercise cell with TODOs (??? placeholders) for student work.\n"
                    f"# It is skipped in the book build to keep downstream cells runnable.\n"
                    f"# Open the notebook in Colab to complete the exercise:\n"
                    f"# {msg}\n"
                    f'print("[exercise cell skipped — open in Colab to complete the TODOs]")\n'
                )
                c["source"] = new_src
                c["outputs"] = []
                c["execution_count"] = None
                n_skipped += 1
        p.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
        print(f"{path}: skipped {n_skipped} TODO cells")


if __name__ == "__main__":
    main()

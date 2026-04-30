#!/usr/bin/env python3
"""Merge each per-lecture study guide into its lecture page.

For each L1-L27:
- Read book/lectures/lecture-NN.md (existing narrative).
- Strip "Source files in this folder" section (not navigable from the site).
- Strip "To go deeper" section (study guide has fuller Additional Resources).
- Strip "Study tools" section (no separate study-guide page after merge).
- Read book/study_guides/lecture-NN.md.
- Strip the H1 title and the AI-banner from the study guide.
- Append the remaining study-guide content to the lecture page.
"""
import re
from pathlib import Path

LECTURE_DIR = Path("book/lectures")
STUDY_DIR = Path("book/study_guides")

# Sections we want to drop from the lecture page entirely.
DROP_LECTURE_SECTIONS = {
    "Source files in this folder",
    "To go deeper",
    "Study tools",
}


def strip_section(md: str, heading: str) -> str:
    """Remove a `## Heading` block (and its content) up to the next `## ` or EOF."""
    pattern = re.compile(
        r"^## " + re.escape(heading) + r"\s*\n.*?(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub("", md)


def study_guide_body(md: str) -> str:
    """Drop the H1 title and the leading AI-banner blockquote.
    Returns everything from the first `##` onward, with section headings
    promoted no further (already at `##`)."""
    # Find first `## ` and slice from there.
    m = re.search(r"^##[^#]", md, re.MULTILINE)
    if not m:
        return ""
    body = md[m.start():]
    # Drop the trailing "> See also: [LN lecture page]…" backlink line if present.
    body = re.sub(r"\n+> See also:.*$", "", body, flags=re.MULTILINE | re.DOTALL)
    return body.rstrip() + "\n"


def merge_one(num: str) -> bool:
    lec = LECTURE_DIR / f"lecture-{num}.md"
    sg = STUDY_DIR / f"lecture-{num}.md"
    if not lec.exists():
        print(f"skip {num}: no lecture page")
        return False

    lec_md = lec.read_text()
    for h in DROP_LECTURE_SECTIONS:
        lec_md = strip_section(lec_md, h)
    lec_md = lec_md.rstrip() + "\n"

    if sg.exists():
        sg_md = sg.read_text()
        sg_body = study_guide_body(sg_md)
        if sg_body.strip():
            # Insert a divider + the study-guide body
            lec_md += "\n---\n\n## Study guide\n\n*Key terms, self-check questions, and additional resources for active recall.*\n\n"
            # The study-guide body uses ## headings (e.g., `## Key Terms`).
            # Demote them to ### so they sit under the `## Study guide` umbrella.
            sg_body_demoted = re.sub(r"^## ", "### ", sg_body, flags=re.MULTILINE)
            lec_md += sg_body_demoted

    lec.write_text(lec_md)
    return True


def main():
    ok = 0
    for n in range(1, 29):
        num = f"{n:02d}"
        if merge_one(num):
            ok += 1
    print(f"merged {ok} lecture pages")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
For chunk 2/3 lab solution notebooks (labs 6-16), the structure is:
  [Original lab cells with TODO/??? in code cells]
  ...
  [markdown: "# Solutions"]
  [markdown: "### Solution: <topic>"]
  [code:    actual implementation]
  ...

Goal: produce a "fully-solved" version where each TODO cell is *replaced* by
its corresponding solution code, and the appended Solution section is removed.
The result is a notebook where every code cell is runnable end-to-end.

Heuristic: the appended `### Solution:` markdown cells appear in the same
order as the TODO code cells in the body. We pair them by index.

Cell-replacement strategy: each TODO cell typically has exactly one structural
counterpart in the appended Solutions section. If the order doesn't match,
we fall back to a fuzzy match on shared identifiers (function names like
`softmax`, `categorical_cross_entropy`, `compute_macro_f1`, etc.)

If the heuristic fails for a notebook, we leave it alone and log it.
"""
import json
import re
import sys
import argparse
from pathlib import Path


def get_source(cell):
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else src


def has_todo_marker(src):
    """A code cell counts as a TODO cell if it contains the literal `???` token
    or a `# TODO` comment."""
    return "???" in src or re.search(r"#\s*TODO", src) is not None


def find_solutions_split(cells):
    """Return the index where the appended Solutions section starts (markdown
    cell containing `# Solutions`), or None if absent."""
    for i, c in enumerate(cells):
        if c["cell_type"] != "markdown":
            continue
        s = get_source(c)
        # The trailing "# Solutions" header
        if re.search(r"^\s*-{3,}\s*\n\s*-{3,}\s*\n\s*#\s+Solutions\b", s, re.MULTILINE) \
                or re.match(r"\s*#\s+Solutions\s*$", s.strip().split("\n")[0]):
            return i
    return None


def collect_solution_code_cells(cells, start):
    """Return list of code cells in the appended Solutions section."""
    return [c for c in cells[start:] if c["cell_type"] == "code"]


def collect_todo_code_cells(cells, end):
    """Return list of (idx, cell) for TODO code cells *before* end."""
    out = []
    for i in range(end):
        c = cells[i]
        if c["cell_type"] != "code":
            continue
        if has_todo_marker(get_source(c)):
            out.append((i, c))
    return out


# Functions/identifiers commonly defined in the solutions
ID_HINTS = [
    "softmax", "categorical_cross_entropy", "compute_macro_f1",
    "raw_logits_ovr", "raw_sigmoid_ovr", "normalized_ovr",
    "compute_pairwise_distances", "knn_predict",
    "huber_loss", "quantile_loss", "pinball_loss",
    "gini_impurity", "log_loss", "compute_kl",
    "kaplan_meier", "log_rank_test", "cox_partial_likelihood",
    "compute_silhouette", "compute_inertia", "elbow_index",
    "explained_variance_ratio", "reconstruction_error",
    "message_pass", "graph_conv", "node_feature",
    "tokenize", "build_vocab", "encode_sequence",
    "convolve_image", "rgb_to_gray", "compute_iou",
    "moving_average", "autocorrelation", "lag_features",
    "events_to_features", "filter_events", "build_event_table",
]


def best_match(todo_src, sol_cells):
    """Best matching solution cell for a TODO cell, by shared identifier."""
    todo_ids = {h for h in ID_HINTS if h in todo_src}
    if not todo_ids:
        return None
    best_idx = None
    best_overlap = 0
    for j, sc in enumerate(sol_cells):
        sol_src = get_source(sc)
        sol_ids = {h for h in ID_HINTS if h in sol_src}
        overlap = len(todo_ids & sol_ids)
        if overlap > best_overlap:
            best_overlap = overlap
            best_idx = j
    return best_idx


def inline(notebook_path: Path, out_path: Path) -> dict:
    nb = json.loads(notebook_path.read_text())
    cells = nb["cells"]

    sol_start = find_solutions_split(cells)
    if sol_start is None:
        return {"status": "no-solutions-section", "replaced": 0}

    sol_cells = collect_solution_code_cells(cells, sol_start)
    todo_pairs = collect_todo_code_cells(cells, sol_start)

    # Pair them: prefer in-order alignment, fall back to identifier match.
    replacements = {}
    sol_used = set()
    if len(todo_pairs) == len(sol_cells):
        # In-order pairing
        for (i, _todo), sc in zip(todo_pairs, sol_cells):
            replacements[i] = sc
            sol_used.add(id(sc))
    else:
        # Fuzzy match on identifier overlap
        for (i, todo) in todo_pairs:
            todo_src = get_source(todo)
            j = best_match(todo_src, sol_cells)
            if j is not None and id(sol_cells[j]) not in sol_used:
                replacements[i] = sol_cells[j]
                sol_used.add(id(sol_cells[j]))

    if not replacements:
        return {"status": "no-pairs", "replaced": 0}

    # Build the new cell list:
    # - Walk original cells up to sol_start
    # - For each cell at index in `replacements`, swap source for solution source
    # - Drop everything from sol_start onward (the appended solutions block)
    new_cells = []
    for i in range(sol_start):
        c = cells[i]
        if i in replacements:
            sol = replacements[i]
            new_c = {
                "cell_type": "code",
                "metadata": c.get("metadata", {}),
                "source": sol.get("source", ""),
                "outputs": [],
                "execution_count": None,
            }
            new_cells.append(new_c)
        else:
            new_cells.append(c)

    nb["cells"] = new_cells
    out_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
    return {
        "status": "ok",
        "replaced": len(replacements),
        "todo_cells": len(todo_pairs),
        "solution_cells": len(sol_cells),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", help="notebook paths to transform")
    parser.add_argument("--out-dir", default=None,
                        help="if set, write to OUT_DIR/<basename>; else overwrite in place")
    args = parser.parse_args()

    for src in args.inputs:
        src = Path(src)
        if args.out_dir:
            out = Path(args.out_dir) / src.name
            out.parent.mkdir(parents=True, exist_ok=True)
        else:
            out = src
        result = inline(src, out)
        print(f"{src}: {result}")


if __name__ == "__main__":
    main()

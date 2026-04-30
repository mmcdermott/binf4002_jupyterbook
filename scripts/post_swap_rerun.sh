#!/usr/bin/env bash
# After the initial run completes, swap in the inlined / TODO-skipped chunk-2/3
# lab notebooks and the !pip-stripped lecture notebook, then re-execute only those.
set -uo pipefail
cd "$(dirname "$0")/.."

# 1. Swap chunk-2/3 lab notebooks with the staged inlined / TODO-skipped versions.
for f in scripts/staged_labs/lab*.ipynb; do
    cp "$f" "book/labs/$(basename $f)"
done

# 2. Strip "!pip install" lines from all notebooks in book/ — pip is provided by
#    the isolated venv. Replace each !pip install line with a no-op print.
python3 - <<'PYEOF'
import json
import re
from pathlib import Path

PIP_RE = re.compile(r"^\s*!pip\s+install\b.*$", re.MULTILINE)

# Convert get_ipython().system('pip install …') idioms too.
GET_IPY_RE = re.compile(r"^\s*get_ipython\(\)\.system\(['\"]pip\s+install[^'\"]*['\"]\)\s*$", re.MULTILINE)

for path in list(Path("book/labs").glob("*.ipynb")) + list(Path("book/lectures").glob("nb-*.ipynb")):
    nb = json.loads(path.read_text())
    changed = False
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", "")
        if isinstance(src, list):
            src_str = "".join(src)
        else:
            src_str = src
        new = PIP_RE.sub("# (pip install handled by the book's isolated env)", src_str)
        new = GET_IPY_RE.sub("# (pip install handled by the book's isolated env)", new)
        if new != src_str:
            cell["source"] = new
            changed = True
    if changed:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
        print(f"stripped !pip lines from {path}")
PYEOF

# 3. Re-run notebooks that previously had errors. These are the ones with
#    cell-errors > 0 in scripts/exec_status.tsv, plus the chunk-2/3 labs we
#    just swapped (their previous run was on the wrong source).
RERUN=()
while IFS=$'\t' read -r NB EXTRAS; do
    [ -z "${NB:-}" ] && continue
    [ ! -f "$NB" ] && continue
    base=$(basename "$NB")
    case "$base" in
        # Always re-run the swapped chunk-2/3 labs
        lab6_*|lab7_*|lab8_*|lab9_*|lab10_*|lab11_*|lab12_*|lab13_*|lab14_*|lab15_*|lab16_*) RERUN+=("$NB:$EXTRAS"); continue ;;
    esac
    # Re-run anything that had errors last time
    errs=$(awk -F'\t' -v nb="$NB" '$1==nb {print $5}' scripts/exec_status.tsv 2>/dev/null)
    [ -n "${errs:-}" ] && [ "$errs" -gt 0 ] && RERUN+=("$NB:$EXTRAS")
done < scripts/notebook_extras.tsv

echo "Re-running ${#RERUN[@]} notebooks:"
printf "  %s\n" "${RERUN[@]}"

STATUS=scripts/rerun_status.tsv
echo -e "notebook\trc\tcells\toutputs\terrors\tnote" > "$STATUS"

for entry in "${RERUN[@]}"; do
    NB="${entry%:*}"; EXTRAS="${entry#*:}"
    EXTRAS_ARR=()
    if [ -n "${EXTRAS:-}" ]; then
        # shellcheck disable=SC2206
        EXTRAS_ARR=( $EXTRAS )
    fi
    echo "=== $NB :: extras=${EXTRAS_ARR[*]:-none} ==="
    if NB_EXEC_TIMEOUT=900 scripts/execute_notebook.sh "$NB" "${EXTRAS_ARR[@]}"; then
        RC=0
    else
        RC=$?
    fi
    CELLS=$(jq '[.cells[]|select(.cell_type=="code")]|length' "$NB")
    OUTS=$(jq '[.cells[]|select(.cell_type=="code")|.outputs|length]|add // 0' "$NB")
    ERRS=$(jq '[.cells[]|select(.cell_type=="code")|.outputs[]?|select(.output_type=="error")]|length' "$NB")
    echo -e "${NB}\t${RC}\t${CELLS}\t${OUTS}\t${ERRS}\t" >> "$STATUS"
done

echo
echo "=== rerun summary ==="
column -t -s$'\t' "$STATUS"

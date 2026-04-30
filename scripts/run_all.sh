#!/usr/bin/env bash
# Iterate over scripts/notebook_extras.tsv and re-execute each notebook in a fresh
# isolated venv with the required extras. Logs to scripts/exec_status.tsv.
set -uo pipefail
cd "$(dirname "$0")/.."

STATUS=scripts/exec_status.tsv
echo -e "notebook\trc\tcells\toutputs\terrors\tnote" > "$STATUS"

while IFS=$'\t' read -r NB EXTRAS; do
    [ -z "${NB:-}" ] && continue
    [ ! -f "$NB" ] && { echo "skip-missing: $NB"; continue; }
    EXTRAS_ARR=()
    if [ -n "${EXTRAS:-}" ]; then
        # shellcheck disable=SC2206
        EXTRAS_ARR=( $EXTRAS )
    fi
    echo "=== $NB :: extras=${EXTRAS_ARR[*]:-none} ==="
    if scripts/execute_notebook.sh "$NB" "${EXTRAS_ARR[@]}"; then
        RC=0
    else
        RC=$?
    fi
    CELLS=$(jq '[.cells[]|select(.cell_type=="code")]|length' "$NB")
    OUTS=$(jq '[.cells[]|select(.cell_type=="code")|.outputs|length]|add // 0' "$NB")
    ERRS=$(jq '[.cells[]|select(.cell_type=="code")|.outputs[]?|select(.output_type=="error")]|length' "$NB")
    NOTE=""
    if [ "$RC" -ne 0 ]; then NOTE="exit-$RC"; fi
    if [ "$ERRS" -gt 0 ]; then NOTE="${NOTE:+$NOTE,}cell-errors=$ERRS"; fi
    echo -e "${NB}\t${RC}\t${CELLS}\t${OUTS}\t${ERRS}\t${NOTE}" >> "$STATUS"
done < scripts/notebook_extras.tsv

echo
echo "=== summary ==="
column -t -s$'\t' "$STATUS"

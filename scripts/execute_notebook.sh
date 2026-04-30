#!/usr/bin/env bash
# Execute a single notebook in an isolated uv venv with notebook-specific extras.
# Usage:
#   scripts/execute_notebook.sh <path/to/nb.ipynb> [extra_pkg1 extra_pkg2 ...]
set -euo pipefail
NB="$1"; shift
EXTRAS=("$@")
TIMEOUT="${NB_EXEC_TIMEOUT:-600}"

# Base "Colab-like" stack used by every notebook.
BASE_PKGS=(
    "ipykernel"
    "jupyter-client"
    "nbconvert"
    "nbformat"
    "numpy"
    "pandas"
    "matplotlib"
    "seaborn"
    "scipy"
    "scikit-learn"
    "Pillow"
    "requests"
    "tqdm"
)

ALL_PKGS=("${BASE_PKGS[@]}" "${EXTRAS[@]}")
WITH_ARGS=()
for p in "${ALL_PKGS[@]}"; do
    WITH_ARGS+=("--with" "$p")
done

LOG="${NB%.ipynb}.exec.log"
echo "$(date -Is) executing $NB with extras: ${EXTRAS[*]:-none}" | tee "$LOG"

# Use uv to spawn an isolated environment, then run jupyter nbconvert --execute.
# --isolated avoids polluting the project venv. Outputs are written in-place.
uv run --isolated --no-project \
    --python 3.11 \
    "${WITH_ARGS[@]}" \
    -- jupyter nbconvert \
        --to notebook --execute --inplace \
        --ExecutePreprocessor.timeout="$TIMEOUT" \
        --ExecutePreprocessor.allow_errors=True \
        --ExecutePreprocessor.iopub_timeout=120 \
        "$NB" >>"$LOG" 2>&1
RC=$?
echo "$(date -Is) $NB exit=$RC" | tee -a "$LOG"
exit $RC

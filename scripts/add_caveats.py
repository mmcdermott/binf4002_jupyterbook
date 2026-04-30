#!/usr/bin/env python3
"""Prepend a caveat markdown cell to a notebook (idempotent).

Marks specific claims / cells as "read with care" without rewriting the
released student notebook content. Idempotent via a marker string.
"""
import json, sys
from pathlib import Path

MARKER = "<!-- BINF-CAVEAT-V1 -->"

def add_caveat(path: Path, caveat_md: str):
    nb = json.loads(path.read_text())
    cells = nb["cells"]
    # Skip if already added
    for c in cells:
        if c.get("cell_type") == "markdown":
            src = c.get("source", "")
            if isinstance(src, list):
                src = "".join(src)
            if MARKER in src:
                return f"already-applied: {path}"
    new_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": MARKER + "\n" + caveat_md,
    }
    nb["cells"] = [new_cell] + cells
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
    return f"added: {path}"

CAVEATS = {
    "book/lectures/nb-14-llm.ipynb": """
> **Reader notes (not part of the original notebook).** The cells below were authored as Colab demos and contain a few claims worth reading with care:
>
> - Where the notebook says PubMed sample text "is the same biomedical text that BioMedLM was trained on," the right reading is *same broad biomedical-literature domain* — not necessarily the exact same corpus. PubMed abstracts are also *not* the same genre as EHR clinical notes.
> - Where the notebook discusses 4-bit quantization memory ("≈700 MB on GPU" for BioMedLM 2.7B), the figure is optimistic. Raw 4-bit weights for 2.7B parameters are roughly 1.35 GB; practical GPU memory is higher because of quantization metadata, activations, KV cache, and framework overhead.
> - Where the notebook says "no efficient algorithm for the globally best sequence," the algorithmically precise framing is: **exact** global maximum-probability decoding for a long autoregressive sequence is exponential in sequence length in the general case, so practical systems use approximate search (beam search) or stochastic decoding (temperature, top-k, nucleus).
""",
    "book/lectures/nb-27-modern-bio-models.ipynb": """
> **Reader notes (not part of the original notebook).** Two wording calibrations worth flagging:
>
> - The notebook describes pLM attention heads as "recovering coevolution." A more accurate framing: some attention heads and embeddings *correlate with* structural contacts and evolutionary constraints. They are not the same as explicit MSA-derived couplings (DCA-style); read attention as a useful diagnostic signal, not a causal coupling score.
> - The notebook compares zero-shot pLM scores to SIFT / PolyPhen with phrasing that can be read as a blanket ranking. The accurate claim: pLM zero-shot scores are *competitive with, and on some benchmarks outperform,* SIFT / PolyPhen, but the conclusion depends strongly on benchmark, variant set, train/test leakage, and endpoint (molecular fitness vs. clinical pathogenicity). There is no universal ranking.
> - Variants labeled as "real pathogenic mutations (ClinVar / published)" inside the notebook are illustrative hand-picked examples; treat them as pedagogy, not as a benchmark. Refer to ClinVar directly (with Variation IDs and review-status fields) for any decision.
""",
}

for relpath, caveat in CAVEATS.items():
    p = Path(relpath)
    if not p.exists():
        print(f"skip-missing: {p}")
        continue
    print(add_caveat(p, caveat.strip()))

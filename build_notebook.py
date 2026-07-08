"""
build_notebook.py — driver that assembles, writes, and verifies the notebook.

Usage
-----
  python build_notebook.py --smoke --verify both      # validate the pipeline
  python build_notebook.py --write                    # write the shipped .ipynb
  python build_notebook.py --verify both              # QA both states
  python build_notebook.py --write --verify both      # do everything

Modules are registered (in learner order) in MODULES below. Each module is a
callable `build(nb: NB)` that appends its cells via the NB helpers.
"""
from __future__ import annotations

import argparse

import nbformat

from nbcore import NB, assemble, verify, NOTEBOOK_FILENAME
from modules import (
    m0_orientation, m1_python, m2_dictionaries, m3_pandas, m4_numpy,
    m5_matplotlib, m6_sklearn, capstone, career, report, reviews,
)

# Real modules are appended here as they are authored (Orientation -> Report).
MODULES = [
    m0_orientation.build,
    m1_python.build,
    m2_dictionaries.build,
    reviews.build_review_a,      # 🔁 spaced review after Python + Dictionaries
    m3_pandas.build,
    m4_numpy.build,
    reviews.build_review_b,      # 🔁 spaced review after Pandas + NumPy
    m5_matplotlib.build,
    m6_sklearn.build,
    capstone.build,
    career.build,
    report.build,
]


def _smoke_module(nb: NB):
    """Throwaway module that exercises every builder + both verification states."""
    nb.section("smoke", "Smoke Test — pipeline validation", 2)
    nb.md("A tiny lesson used only to prove the generator + two-state QA works.")
    nb.code("prices = [10, 20, 30]\nprint('average price =', sum(prices) / len(prices))")
    nb.md("### 🎯 Your turn\nCompute the average of `[4, 8, 6]` and store it in `avg`.")
    nb.practice(
        "smoke_avg",
        placeholder="avg = None  # YOUR CODE HERE  (hint: sum(...) / len(...))",
        solution="avg = sum([4, 8, 6]) / len([4, 8, 6])",
        hint="Add the three numbers, then divide by how many there are.",
    )
    nb.check("smoke_avg", user="avg", expected="6.0", hint="The sum is 18 and the count is 3.")
    nb.md("### 📝 Quick quiz\n**Q:** What does `len([1, 2, 3])` return?  A) 2  B) 3  C) 6")
    nb.practice(
        "smoke_q1",
        placeholder="answer = None  # set to 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Count the items in the list.",
    )
    nb.mcq("smoke_q1", user="answer", correct="B",
           explanation="`len` counts items, and there are 3.", hint="Just count them.")


def build(smoke: bool = False) -> NB:
    nb = NB()
    if smoke:
        _smoke_module(nb)
    for module in MODULES:
        module(nb)
    return nb


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the shipped .ipynb")
    parser.add_argument("--verify", choices=["unfilled", "filled", "both"])
    parser.add_argument("--smoke", action="store_true", help="use the throwaway smoke module")
    args = parser.parse_args()

    nb = build(smoke=args.smoke)

    if args.write:
        node = assemble(nb, "unfilled")
        nbformat.write(node, NOTEBOOK_FILENAME)
        print(f"📝 wrote {NOTEBOOK_FILENAME} — {len(node.cells)} cells")

    if args.verify:
        modes = ["unfilled", "filled"] if args.verify == "both" else [args.verify]
        problems = 0
        for mode in modes:
            errors, qa_failed = verify(nb, mode)
            problems += len(errors) + (qa_failed if mode == "filled" else 0)
        print("RESULT:", "✅ ALL CLEAN" if problems == 0 else f"❌ {problems} problem(s) found")


if __name__ == "__main__":
    main()

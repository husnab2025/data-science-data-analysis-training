"""
nbcore.py — Core scaffolding that generates the self-contained Data Science
Analyst training notebook (data_analyst_training.ipynb).

This file (and the uv venv it runs in) is BUILD/QA tooling only. It is never
shipped. The single deliverable is the generated .ipynb, which is fully
self-contained: all data is synthesic/in-notebook, all grading logic embedded.

Two-state generation
---------------------
Every "practice" cell has two forms:
  * placeholder  -> shipped to the learner (`# YOUR CODE HERE`, assigns a sentinel
                    so the cell + its self-check run WITHOUT raising).
  * solution     -> substituted in the "filled" build used only for verification.

Verification asserts:
  * unfilled build: runs top-to-bottom with ZERO error outputs (❌ marks are fine).
  * filled build:   runs top-to-bottom with ZERO error outputs AND ZERO ❌ marks
                    (proving every exercise is solvable and every grader correct).
"""
from __future__ import annotations

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

KERNEL_NAME = "dsat-py312"          # QA kernel (Colab-mirrored venv)
NOTEBOOK_FILENAME = "data_analyst_training.ipynb"


# --------------------------------------------------------------------------- #
# Notebook spec builder
# --------------------------------------------------------------------------- #
class NB:
    """Accumulates ordered cell specs plus registries for TOC / hints / solutions."""

    def __init__(self):
        self.specs = []            # list[ (kind, payload) ]  kind in {md, code, practice}
        self.sections = []         # list[ (anchor, title, level) ] -> TOC
        self.hints = {}            # key -> hint text
        self.solutions = {}        # key -> reference solution (string)
        self.keyinfo = {}          # key -> {"group": str, "label": str}
        self.current_group = "Getting Started"

    # -- plain content -----------------------------------------------------
    def md(self, text: str):
        self.specs.append(("md", text))

    def code(self, text: str):
        self.specs.append(("code", text))

    def section(self, anchor: str, title: str, level: int = 2, group: bool = True):
        """Emit a heading cell with an explicit anchor and register it for the TOC.

        `group=True` also makes this the current grouping bucket for the score report.
        """
        self.sections.append((anchor, title, level))
        if group:
            self.current_group = title
        self.specs.append(("md", f'<a id="{anchor}"></a>\n{"#" * level} {title}'))

    def module(self, anchor: str, title: str):
        """A top-level module heading (level 2) that becomes a score-report group."""
        self.section(anchor, title, level=2, group=True)

    def lesson(self, anchor: str, title: str):
        """A sub-lesson heading (level 3) that keeps the current module's group."""
        self.section(anchor, title, level=3, group=False)

    # -- interactive content ----------------------------------------------
    def practice(self, key: str, placeholder: str, solution: str,
                 hint: str | None = None, label: str | None = None):
        """A learner-editable cell. Placeholder ships; solution used for filled QA."""
        self.solutions[key] = solution
        if hint:
            self.hints[key] = hint
        self.keyinfo[key] = {"group": self.current_group, "label": label or key}
        self.specs.append(("practice", {"placeholder": placeholder, "solution": solution}))

    def check(self, key: str, user: str, expected: str, hint: str, points: int = 1):
        """Emit a self-check code cell comparing `user` against `expected`.

        `user` is wrapped in a lambda so the grader evaluates it inside try/except —
        a deleted or misspelled learner variable prints a friendly ❌, never a crash.
        """
        if key not in self.keyinfo:
            self.keyinfo[key] = {"group": self.current_group, "label": key}
        src = (f"check_answer(user=lambda: {user}, expected={expected}, "
               f"hint={hint!r}, key={key!r}, points={points})")
        self.specs.append(("code", src))

    def mcq(self, key: str, user: str, correct: str, explanation: str = "",
            hint: str = "", label: str | None = None, points: int = 1):
        """Emit a multiple-choice self-check cell (learner set `user` above).

        `user` is wrapped in a lambda for the same crash-safety reason as `check`.
        """
        self.keyinfo[key] = {"group": self.current_group, "label": label or key}
        if hint:
            self.hints[key] = hint
        src = (f"check_quiz(user_answer=lambda: {user}, correct={correct!r}, "
               f"explanation={explanation!r}, hint={hint!r}, key={key!r}, points={points})")
        self.specs.append(("code", src))

    # -- reusable callouts (consistent formatting, additive markdown) -----
    def note(self, text: str):
        """A generic blockquote callout cell (each line prefixed so it renders as a quote)."""
        self.specs.append(("md", "> " + text.replace("\n", "\n> ")))

    def tip(self, text: str):
        """💡 A practical pro tip."""
        self.note("💡 **Pro tip:** " + text)

    def gotcha(self, text: str):
        """⚠️ A common beginner mistake and how to avoid it."""
        self.note("⚠️ **Common mistake to avoid:** " + text)

    def realjob(self, text: str):
        """🌍 A 'what you'd actually do on the job' caveat/nuance."""
        self.note("🌍 **In a real job:** " + text)

    def role_note(self, text: str):
        """👔 How this differs between a Data Analyst and a Data Scientist."""
        self.note("👔 **Analyst vs Scientist:** " + text)

    def recap(self, text: str):
        """🧭 A short 'where we are on the journey' orientation note."""
        self.note("🧭 **Where we are on the journey:** " + text)

    def keyterms(self, pairs):
        """🔑 A key-terms glossary block. `pairs` = list of (term, definition)."""
        lines = ["#### 🔑 Key terms from this lesson", ""]
        for term, definition in pairs:
            lines.append(f"- **{term}** — {definition}")
        self.md("\n".join(lines))


# --------------------------------------------------------------------------- #
# Static cell sources (become cells verbatim in the notebook)
# --------------------------------------------------------------------------- #
TITLE_SOURCE = """\
# 📊 From Zero to Data Analyst — An Interactive Python Notebook

Welcome! This is a **self-contained, interactive textbook**. You will *read* short
lessons, *run* worked examples, *write* your own code, and get **instant, automatic
feedback** — no need to ask anyone (or any AI) whether you got it right.

### How to use this notebook
1. Run the two **setup cells** just below (▶️), top to bottom, once.
2. Work through each lesson **in order**. Every lesson follows the same rhythm:
   **explain → worked example → 🎯 your turn → ✅ self-check → 📝 quiz**, with a
   bigger **🧪 test** between modules.
3. In *🎯 your turn* cells, replace `# YOUR CODE HERE` and run the cell, then run the
   **✅ self-check** cell right below it.
4. Stuck? Every exercise has `show_hint('key')` and, if you're truly stuck,
   `show_solution('key')`.
5. At the very end, a **📈 final report** tallies your score and readiness.

> 💡 *You already know:* variables, data types, printing, arithmetic (revenue/profit),
> comparisons, `if/elif/else`, `AND/OR/NOT`, lists, indexing, `len()`, `sum()`.
> We build straight on top of that.
"""

SETUP_SOURCE = """\
# ▶️ SETUP 1/2 — imports & configuration (run me first)
# Every library below ships preinstalled in Google Colab. Running elsewhere? Uncomment:
# !pip install -q numpy pandas matplotlib seaborn scikit-learn

import math
import random
import statistics

import numpy as np
import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

# Deterministic randomness so every run (and every self-check) is reproducible.
random.seed(42)
np.random.seed(42)

plt.rcParams["figure.figsize"] = (7, 4)
plt.rcParams["axes.grid"] = True
sns.set_theme(style="whitegrid")

print("✅ Setup complete — pandas", pd.__version__, "| numpy", np.__version__)
"""

INFRA_SOURCE = '''\
# ▶️ SETUP 2/2 — the self-grading engine (run me second)
# Defines: check_answer, check_quiz, record/progress, show_hint, show_solution.
# These NEVER raise on a wrong/empty answer — they print ❌ and a hint instead,
# so the whole notebook always runs top-to-bottom cleanly.

progress = {}  # key -> {"passed": bool, "earned": int, "max": int}


def record(key, passed, points=1):
    progress[key] = {"passed": bool(passed), "earned": points if passed else 0, "max": points}


def _equal(a, b):
    """Type-aware, exception-safe equality for ints/floats/lists/dicts/np/pandas."""
    try:
        if a is None:
            return False
        if isinstance(a, (pd.DataFrame, pd.Series)) or isinstance(b, (pd.DataFrame, pd.Series)):
            try:
                return bool(a.equals(b))
            except Exception:
                return False
        if isinstance(a, np.ndarray) or isinstance(b, np.ndarray):
            try:
                return bool(np.allclose(np.asarray(a, dtype=float), np.asarray(b, dtype=float)))
            except Exception:
                try:
                    return bool(np.array_equal(np.asarray(a), np.asarray(b)))
                except Exception:
                    return False
        if isinstance(a, bool) or isinstance(b, bool):
            return a is b or a == b
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-9)
        if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
            return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
        if isinstance(a, dict) and isinstance(b, dict):
            return a.keys() == b.keys() and all(_equal(a[k], b[k]) for k in a)
        return a == b
    except Exception:
        return False


def _read_user(supplier):
    """Evaluate the learner's answer safely. Returns (ok, value_or_errormsg).

    `supplier` is a zero-arg lambda wrapping the learner's expression, so an
    undefined/misspelled variable surfaces here as a caught exception instead of
    crashing the cell.
    """
    try:
        return True, (supplier() if callable(supplier) else supplier)
    except Exception as e:
        return False, "%s: %s" % (type(e).__name__, e)


def check_answer(user, expected, hint, key=None, points=1):
    read_ok, user_val = _read_user(user)
    if not read_ok:
        if key is not None:
            record(key, False, points)
        print("❌ I couldn't read your answer yet (" + user_val + ").")
        print("   👉 Did you run your 🎯 cell just above this one, with no typos?")
        print("   💡 Hint:", hint)
        if key is not None:
            print("   (Truly stuck? Run  show_solution('%s')  to reveal it.)" % key)
        return False
    ok = _equal(user_val, expected)
    if key is not None:
        record(key, ok, points)
    if ok:
        print("✅ Correct! Nicely done.")
    else:
        shown = repr(user_val)
        if len(shown) > 70:
            shown = shown[:70] + "..."
        print("❌ Not yet — your result was:", shown)
        print("   💡 Hint:", hint)
        if key is not None:
            print("   (Truly stuck? Run  show_solution('%s')  to reveal it.)" % key)
    return ok


def check_quiz(user_answer, correct, explanation="", hint="", key=None, points=1):
    read_ok, val = _read_user(user_answer)
    if not read_ok:
        if key is not None:
            record(key, False, points)
        print("❌ I couldn't read your answer yet (" + val + ").")
        print("   👉 Set  answer = 'A'  (or 'B'/'C') in the cell above, then re-run.")
        if hint:
            print("   💡 Hint:", hint)
        return False
    ok = str(val).strip().upper() == str(correct).strip().upper()
    if key is not None:
        record(key, ok, points)
    if ok:
        print("✅ Correct!", explanation)
    else:
        print("❌ Not quite.")
        if hint:
            print("   💡 Hint:", hint)
        if key is not None:
            print("   (Reveal with  show_solution('%s') .)" % key)
    return ok


def show_hint(key):
    print("💡", HINTS.get(key, "No extra hint — re-read the lesson and check your variable names/types."))


def show_solution(key):
    sol = SOLUTIONS.get(key)
    if not sol:
        print("(No stored solution for this exercise.)")
    else:
        print("✅ Reference solution — try it yourself first!\\n")
        print(sol)


print("✅ Self-grading engine loaded. Have fun, and don't be afraid to get ❌ — that's how you learn.")
'''


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #
def _toc_source(nb: NB) -> str:
    lines = ["## 🗺️ Table of Contents\n"]
    for anchor, title, level in nb.sections:
        indent = "    " * max(0, level - 2)
        lines.append(f"{indent}- [{title}](#{anchor})")
    return "\n".join(lines)


def _registry_source(nb: NB) -> str:
    return (
        "# ▶️ SETUP 3/3 — hint & solution bank (run me third)\n"
        "HINTS = " + repr(nb.hints) + "\n\n"
        "SOLUTIONS = " + repr(nb.solutions) + "\n\n"
        "KEYINFO = " + repr(nb.keyinfo) + "\n\n"
        'print("✅ Loaded", len(SOLUTIONS), "exercises with hints & solutions.")'
    )


def assemble(nb: NB, mode: str = "unfilled") -> nbformat.NotebookNode:
    assert mode in ("unfilled", "filled")
    cells = [
        new_markdown_cell(TITLE_SOURCE),
        new_markdown_cell(_toc_source(nb)),
        new_code_cell(SETUP_SOURCE),
        new_code_cell(INFRA_SOURCE),
        new_code_cell(_registry_source(nb)),
    ]
    for kind, payload in nb.specs:
        if kind == "md":
            cells.append(new_markdown_cell(payload))
        elif kind == "code":
            cells.append(new_code_cell(payload))
        elif kind == "practice":
            src = payload["placeholder"] if mode == "unfilled" else payload["solution"]
            cells.append(new_code_cell(src))
    node = new_notebook()
    node.cells = cells
    node.metadata = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12"},
        "colab": {"provenance": []},
    }
    return node


# --------------------------------------------------------------------------- #
# Verification (nbclient, Colab-mirrored kernel)
# --------------------------------------------------------------------------- #
def run_notebook(node, timeout: int = 1200):
    from nbclient import NotebookClient
    client = NotebookClient(node, timeout=timeout, kernel_name=KERNEL_NAME, allow_errors=True)
    client.execute()
    return node


def collect_errors(node):
    errs = []
    for idx, c in enumerate(node.cells):
        if c.cell_type != "code":
            continue
        for o in c.outputs:
            if o.get("output_type") == "error":
                errs.append((idx, o.get("ename"), o.get("evalue"), (c.source or "").strip()[:90]))
    return errs


def _parse_qa(node):
    """Return (failed, total) self-checks, parsed from the QA probe cell output."""
    for c in node.cells:
        if c.cell_type != "code":
            continue
        for o in c.outputs:
            if o.get("output_type") == "stream" and "__QA_PROGRESS__" in o.get("text", ""):
                for line in o["text"].splitlines():
                    if line.startswith("__QA_PROGRESS__"):
                        try:
                            _, failed, total = line.split()
                            return int(failed), int(total)
                        except ValueError:
                            return None, None
    return None, None


def verify(nb: NB, mode: str, timeout: int = 1200):
    """Execute one build; return (errors, qa_failed). Prints a concise report.

    Pass criteria: unfilled -> errors == 0 ; filled -> errors == 0 and qa_failed == 0.
    A temporary QA probe cell reads the `progress` dict directly, so grading
    correctness is measured by state — never by scanning prose for emoji.
    """
    node = assemble(nb, mode)
    node.cells.append(new_code_cell(
        'print("__QA_PROGRESS__", sum(1 for v in progress.values() if not v["passed"]), len(progress))'
    ))
    node = run_notebook(node, timeout=timeout)
    errors = collect_errors(node)
    qa_failed, qa_total = _parse_qa(node)
    n_code = sum(1 for c in node.cells if c.cell_type == "code")
    print(f"[{mode}] executed {n_code} code cells | errors={len(errors)} | "
          f"self-checks: {qa_failed} failed / {qa_total} total")
    for idx, ename, eval_, src in errors[:25]:
        print(f"   ⛔ cell#{idx} {ename}: {eval_}\n      └ {src}")
    return errors, (qa_failed or 0)

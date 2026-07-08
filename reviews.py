"""
Spaced-review checkpoints — short mixed exercises that revisit earlier modules.

Revisiting old concepts (spaced repetition) is how learning becomes permanent, so
these appear after Module 2 (Python + Dictionaries) and after Module 4 (Pandas +
NumPy). No new concepts — just proof the earlier ones stuck.
"""
from __future__ import annotations

from nbcore import NB


# --------------------------------------------------------------------------- #
def build_review_a(nb: NB):
    nb.module("review-a", "🔁 Review Checkpoint A · Python + Dictionaries")
    nb.md(
        "A quick mixed review of Modules 1–2. **No new ideas** — just proving the last two modules "
        "stuck. Coming back to concepts a little later (instead of cramming them once) is scientifically "
        "how memory becomes permanent. Two short tasks. 💪"
    )
    nb.recap(
        "You've finished Python fundamentals and Dictionaries. This checkpoint mixes them together — "
        "just like real work, where you rarely use one skill in isolation."
    )
    nb.md(
        "### 🎯 Review 1 — lists, comprehension & totals (Module 1)\n"
        "Given `prices`, build `taxed` (each price with 20% tax added, i.e. `× 1.2`) using a "
        "comprehension, and `tax_total` (the sum of just the tax part, i.e. `price × 0.2`)."
    )
    nb.practice(
        "ra_1",
        placeholder=(
            'prices = [50, 100, 150]\n'
            '\n'
            'taxed = None      # YOUR CODE HERE — [ each price * 1.2 ]\n'
            'tax_total = None  # YOUR CODE HERE — sum of (each price * 0.2)'
        ),
        solution=(
            'prices = [50, 100, 150]\n'
            '\n'
            'taxed = [p * 1.2 for p in prices]\n'
            'tax_total = sum(p * 0.2 for p in prices)'
        ),
        hint="taxed = [p * 1.2 for p in prices]; tax_total = sum(p * 0.2 for p in prices).",
        label="review: list comprehension + sum",
    )
    nb.check("ra_1", user="(taxed, tax_total)",
             expected="([60.0, 120.0, 180.0], 60.0)",
             hint="Taxed = [60, 120, 180]; the tax parts (10+20+30) total 60.")
    nb.md(
        "### 🎯 Review 2 — dictionary summary (Module 2)\n"
        "Given `scores`, store the **total** of all scores in `total_score` and the **name with the "
        "highest score** in `top_student`."
    )
    nb.practice(
        "ra_2",
        placeholder=(
            'scores = {"Ana": 88, "Ben": 72, "Cara": 95}\n'
            '\n'
            'total_score = None  # YOUR CODE HERE — sum of all scores\n'
            'top_student = None  # YOUR CODE HERE — the name with the highest score'
        ),
        solution=(
            'scores = {"Ana": 88, "Ben": 72, "Cara": 95}\n'
            '\n'
            'total_score = sum(scores.values())\n'
            'top_student = max(scores, key=scores.get)'
        ),
        hint="sum(scores.values()); max(scores, key=scores.get).",
        label="review: dict sum + argmax",
    )
    nb.check("ra_2", user="(total_score, top_student)", expected="(255, 'Cara')",
             hint="88+72+95 = 255; Cara has the highest score (95).")
    nb.md("✅ Nice — Modules 1–2 are locked in. Onward to **Pandas**! 🐼")


# --------------------------------------------------------------------------- #
def build_review_b(nb: NB):
    nb.module("review-b", "🔁 Review Checkpoint B · Pandas + NumPy")
    nb.md(
        "Another quick mixed review — this time Modules 3–4 (Pandas + NumPy), the heart of the "
        "analyst toolkit. **No new concepts.** Two short tasks to prove they stuck. 🧠"
    )
    nb.recap(
        "You've now got Pandas (the big one) and NumPy under your belt. This checkpoint blends a "
        "filter-and-group task with a vectorised-math task — exactly the combo real analysis uses."
    )
    nb.md(
        "### 🎯 Review 1 — filter & group (Module 3)\n"
        "Given `df`, store total `sales` **per region** as a dictionary in `by_region`, and the "
        "**number of rows** where sales are **200 or more** in `big_count`."
    )
    nb.practice(
        "rb_1",
        placeholder=(
            'df = pd.DataFrame({\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '    "sales": [100, 250, 300, 150, 200],\n'
            '})\n'
            '\n'
            'by_region = None  # YOUR CODE HERE — {region: total sales} dict\n'
            'big_count = None  # YOUR CODE HERE — how many rows have sales >= 200'
        ),
        solution=(
            'df = pd.DataFrame({\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '    "sales": [100, 250, 300, 150, 200],\n'
            '})\n'
            '\n'
            'by_region = df.groupby("region")["sales"].sum().to_dict()\n'
            'big_count = len(df[df["sales"] >= 200])'
        ),
        hint='df.groupby("region")["sales"].sum().to_dict(); len(df[df["sales"] >= 200]).',
        label="review: groupby + filter",
    )
    nb.check("rb_1", user="(by_region, big_count)",
             expected="({'N': 600, 'S': 400}, 3)",
             hint="N = 100+300+200 = 600; S = 250+150 = 400; three rows are ≥ 200 (250, 300, 200).")
    nb.md(
        "### 🎯 Review 2 — vectorised NumPy (Module 4)\n"
        "Given `units`, compute `revenue` = `units × 5` (a whole-array operation) and store the "
        "**index of the biggest month** in `best_index`."
    )
    nb.practice(
        "rb_2",
        placeholder=(
            'units = np.array([12, 30, 18, 45, 25])\n'
            '\n'
            'revenue = None     # YOUR CODE HERE — units times 5 (vectorised)\n'
            'best_index = None  # YOUR CODE HERE — index of the largest units value'
        ),
        solution=(
            'units = np.array([12, 30, 18, 45, 25])\n'
            '\n'
            'revenue = units * 5\n'
            'best_index = units.argmax()'
        ),
        hint="units * 5 multiplies the whole array; units.argmax() gives the index of the max.",
        label="review: vectorized + argmax",
    )
    nb.check("rb_2", user="(revenue, best_index)",
             expected="(np.array([60, 150, 90, 225, 125]), 3)",
             hint="revenue = [60,150,90,225,125]; the biggest units value (45) sits at index 3.")
    nb.md("✅ Excellent — the core toolkit is solid. On to making it all **visual**! 📊")

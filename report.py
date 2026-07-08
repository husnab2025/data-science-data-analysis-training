"""
Final report — a self-scoring dashboard built from the live `progress` dict and
the generated `KEYINFO` (which maps every graded key to its module group).

Runs cleanly in every state: all-fail (unfilled) shows 0%, all-pass (filled)
shows 100% — never raises.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    nb.module("report", "📈 Final Report & Readiness")
    nb.md(
        "You've reached the end! Run the cell below at any time to see your live score. It tallies "
        "every self-check, quiz, and test you've completed, groups them by module, and gives you a "
        "readiness verdict plus a list of anything worth reviewing.\n\n"
        "> Scores update as you complete exercises — come back and re-run this after improving a weak "
        "area. For a per-exercise breakdown, run `show_details()`."
    )
    nb.code(
        'def _grouped_progress():\n'
        '    """Roll the per-key progress up into per-module totals (in build order)."""\n'
        '    groups = {}\n'
        '    for key, res in progress.items():\n'
        '        group = KEYINFO.get(key, {}).get("group", "Other")\n'
        '        bucket = groups.setdefault(group, {"earned": 0, "max": 0, "passed": 0, "count": 0})\n'
        '        bucket["earned"] += res["earned"]\n'
        '        bucket["max"] += res["max"]\n'
        '        bucket["passed"] += 1 if res["passed"] else 0\n'
        '        bucket["count"] += 1\n'
        '    return groups\n'
        '\n'
        '\n'
        'def final_report():\n'
        '    if not progress:\n'
        '        print("You haven\'t run any self-check cells yet.")\n'
        '        print("Work through the lessons above, then re-run this cell. 🙂")\n'
        '        return\n'
        '\n'
        '    groups = _grouped_progress()\n'
        '    total_earned = sum(g["earned"] for g in groups.values())\n'
        '    total_max = sum(g["max"] for g in groups.values())\n'
        '    pct = 100 * total_earned / total_max if total_max else 0.0\n'
        '\n'
        '    print("=" * 60)\n'
        '    print("📈  FINAL REPORT — From Zero to Data Analyst")\n'
        '    print("=" * 60)\n'
        '    for group, g in groups.items():\n'
        '        gp = 100 * g["earned"] / g["max"] if g["max"] else 0.0\n'
        '        filled = int(round(gp / 10))\n'
        '        bar = "█" * filled + "·" * (10 - filled)\n'
        '        mark = "✅" if gp >= 70 else ("⚠️ " if gp >= 40 else "❌")\n'
        '        name = group if len(group) <= 44 else group[:41] + "..."\n'
        '        print(f"{mark} {name:<44} {g[\'earned\']:>3}/{g[\'max\']:<3} [{bar}] {gp:5.1f}%")\n'
        '    print("-" * 60)\n'
        '    print(f"     TOTAL SCORE: {total_earned}/{total_max}   =   {pct:.1f}%")\n'
        '    print("=" * 60)\n'
        '\n'
        '    if pct >= 90:\n'
        '        print("🌟 EXCELLENT — you\'ve mastered the material in this notebook.")\n'
        '        print("   You\'re ready to start entry-level PORTFOLIO projects and interview prep.")\n'
        '    elif pct >= 75:\n'
        '        print("🎉 STRONG FOUNDATION — the core skills are solid.")\n'
        '        print("   Next: build guided portfolio projects on REAL datasets to become job-ready.")\n'
        '    elif pct >= 50:\n'
        '        print("👍 GOOD PROGRESS — you\'re well on your way.")\n'
        '        print("   Review the flagged areas below, redo their exercises, then push on.")\n'
        '    else:\n'
        '        print("📚 KEEP PRACTISING — repetition is how this becomes natural.")\n'
        '        print("   Revisit the flagged modules below and re-run their cells. You\'ve got this.")\n'
        '\n'
        '    weak = [name for name, g in groups.items()\n'
        '            if g["max"] and (100 * g["earned"] / g["max"]) < 60]\n'
        '    if weak:\n'
        '        print("\\n🔎 Topics to review (under 60%):")\n'
        '        for name in weak:\n'
        '            print("   -", name)\n'
        '    else:\n'
        '        print("\\n🌟 No weak areas — every module is at 60% or above. Excellent work!")\n'
        '\n'
        '    print("\\n🧭 Honest note: this notebook is your FOUNDATION, not the whole job.")\n'
        '    print("   Still ahead of you (see the Career Primer section for the roadmap):")\n'
        '    for item in ["SQL (databases) — your immediate next step",\n'
        '                 "Real, messy datasets and files (not tidy toy data)",\n'
        '                 "Statistics beyond the average (median, spread, significance)",\n'
        '                 "A dashboard / BI tool (Power BI, Tableau, or Looker)",\n'
        '                 "Git / GitHub version control",\n'
        '                 "Explaining results to non-technical stakeholders",\n'
        '                 "2-3 portfolio projects + interview practice"]:\n'
        '        print("   -", item)\n'
        '\n'
        '\n'
        'def show_details():\n'
        '    """Optional: list every exercise with a ✅/❌ and its module."""\n'
        '    if not progress:\n'
        '        print("Nothing to show yet — run some exercises first.")\n'
        '        return\n'
        '    current = None\n'
        '    for key, res in progress.items():\n'
        '        info = KEYINFO.get(key, {})\n'
        '        group = info.get("group", "Other")\n'
        '        if group != current:\n'
        '            print(f"\\n— {group} —")\n'
        '            current = group\n'
        '        mark = "✅" if res["passed"] else "❌"\n'
        '        print(f"   {mark} {info.get(\'label\', key)}")\n'
        '\n'
        '\n'
        'final_report()'
    )
    nb.md(
        "### 🎓 What you've learned\n"
        "If you've made it here with a passing score, you can now — in real, practical Python —\n\n"
        "- summarise and reshape data with core Python, dictionaries, and comprehensions;\n"
        "- **wrangle** real tables with Pandas (select, filter, sort, group, clean, merge);\n"
        "- crunch numbers fast with **NumPy**;\n"
        "- **visualise** insights with the right Matplotlib/Seaborn chart;\n"
        "- and train, evaluate, and interpret **machine-learning models** with scikit-learn.\n\n"
        "That's the **foundation** the whole data-analyst/scientist career is built on — genuinely the "
        "hard part to start. You're not 'done' (nobody ever is), but you've proven you can learn this. "
        "Follow the **Career Primer** roadmap — SQL next — keep this notebook as your reference, and "
        "go build something with real data. 🚀"
    )

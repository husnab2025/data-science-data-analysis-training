"""
Module 0 — Welcome & Orientation.

A gentle on-ramp for a learner with no technical background: growth mindset,
how to run a cell in Colab, why errors are normal, the analytics workflow, and a
plain-English Data Analyst vs Data Scientist overview. Includes the learner's
very first (confidence-building) graded exercise so the practice/check rhythm is
crystal clear before real content begins.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _welcome(nb)
    _how_to_run(nb)
    _first_win(nb)
    _errors_are_normal(nb)
    _workflow(nb)
    _roles(nb)
    _helpers_recap(nb)


# --------------------------------------------------------------------------- #
def _welcome(nb: NB):
    nb.module("mod0", "Module 0 · Welcome — Start Here 👋")
    nb.md(
        "Hello, and **welcome**. 🎉 If you have almost no technical background, you are in exactly the "
        "right place. This notebook was built for *you* — it starts gentle and builds up one small, "
        "friendly step at a time. You will not be thrown in the deep end.\n\n"
        "**A promise:** by the end, you'll be able to load real data, clean it, explore it, chart it, "
        "and even build simple prediction models — the actual daily work of a Data Analyst or Data "
        "Scientist. You don't need to be a genius. You need to **go in order, run every cell, and not "
        "give up.** That's it.\n\n"
        "**How to succeed here (please read slowly):**\n"
        "- Go **top to bottom**. Never skip ahead — each idea rests on the one before it.\n"
        "- **Run every cell**, including the examples. Learning by *doing* beats just reading.\n"
        "- Take your time. There is **no timer** and no one watching. Re-read anything twice.\n"
        "- Getting a ❌ is **not failure** — it's the notebook helping you. More on that below."
    )
    nb.recap(
        "You're at the very start. The road ahead: **Module 0 (this welcome) → 1 Python basics → "
        "2 Dictionaries → 3 Pandas (the big one) → 4 NumPy → 5 Charts → 6 Machine Learning → a "
        "Capstone project → a Career primer → your Final Report.** One step at a time. 🚶"
    )


# --------------------------------------------------------------------------- #
def _how_to_run(nb: NB):
    nb.lesson("m0-run", "Lesson 0.1 — How to Run a Cell (the one skill you need)")
    nb.md(
        "This notebook is made of **cells**. There are two kinds:\n\n"
        "- **Text cells** (like this one) — you just *read* them.\n"
        "- **Code cells** (grey boxes with code) — you *run* them to make them work.\n\n"
        "**To run a code cell:** click on it once, then either press **▶️** (the play button on its "
        "left) **or** hold **Shift** and press **Enter**. That's the single most important skill in "
        "this whole notebook — and you already have it. 🙌\n\n"
        "When a cell runs, any result appears **just below it**. A number `[1]` appears on its left to "
        "show it ran. Always run cells **in order from the top**, because later cells depend on "
        "earlier ones."
    )
    nb.md("**Worked example — run the cell below to see it work:**")
    nb.code(
        'print("👋 Hello! You just ran your first code cell in this notebook.")\n'
        'print("If you can read this line below the cell, you did it perfectly.")'
    )
    nb.tip(
        "If a code cell doesn't seem to do anything, check the top of the notebook: did you run the "
        "**two ▶️ SETUP cells** first? They switch everything on. When in doubt, use the menu "
        "**Runtime → Run all** to run everything from the top in order."
    )


# --------------------------------------------------------------------------- #
def _first_win(nb: NB):
    nb.lesson("m0-first", "Lesson 0.2 — Your First Exercise (an easy win)")
    nb.md(
        "Every lesson gives you a **🎯 your turn** cell where *you* write a little code, followed by a "
        "**✅ self-check** cell that instantly tells you if it's right. Let's practise that rhythm "
        "with the easiest exercise in the book.\n\n"
        "**Your task:** in the cell below, change `None` to the number **7**. Then run it, and run the "
        "check cell after it."
    )
    nb.practice(
        "m0_first",
        placeholder="my_first_answer = None  # 👈 change None to the number 7, then run this cell",
        solution="my_first_answer = 7",
        hint="Delete the word None and type 7 in its place, so the line reads: my_first_answer = 7",
        label="your first exercise",
    )
    nb.check("m0_first", user="my_first_answer", expected="7",
             hint="Set my_first_answer = 7 (just the number 7, no quotes).")
    nb.md(
        "See how that worked? You wrote code, ran the check, and got instant feedback. **That exact "
        "rhythm repeats through the whole notebook.** If you saw a ✅ — congratulations, you're "
        "officially doing data work. If you saw a ❌, read its hint and try again. Either way: you're "
        "learning. 💪"
    )


# --------------------------------------------------------------------------- #
def _errors_are_normal(nb: NB):
    nb.lesson("m0-errors", "Lesson 0.3 — Errors Are Normal (don't panic)")
    nb.md(
        "Sooner or later a cell will show a scary block of red/pink text ending in something like "
        "`NameError` or `SyntaxError`. **This is completely normal.** Every professional programmer — "
        "including senior ones — sees errors *many times a day*. An error is not you failing; it's the "
        "computer politely telling you *what* it didn't understand.\n\n"
        "**What to do when you see an error:**\n"
        "1. **Don't panic.** Nothing is broken. You can't hurt anything.\n"
        "2. Read the **last line** — it's usually the clearest clue (e.g., `NameError: name 'x' is not "
        "defined` means you used `x` before creating it).\n"
        "3. Common causes: you forgot to run an earlier cell, mistyped a name, or missed a quote/bracket.\n"
        "4. Fix it and run again. Repeat. This loop *is* programming.\n\n"
        "The **✅ self-check** cells in this notebook are special: they're designed to *never* throw a "
        "scary error even if your answer is blank or wrong — they just calmly print ❌ and a hint. So "
        "you can always run them safely."
    )
    nb.gotcha(
        "The #1 beginner error is `NameError: name '...' is not defined`. 99% of the time it means you "
        "**skipped a cell** or didn't run the SETUP cells at the top. Fix: scroll up and run the cells "
        "you skipped (or **Runtime → Run all**)."
    )
    nb.tip(
        "Stuck for real? Every exercise has two lifelines: `show_hint('the_key')` nudges your thinking, "
        "and `show_solution('the_key')` reveals the full answer. Using them is smart, not cheating — "
        "just try yourself first."
    )


# --------------------------------------------------------------------------- #
def _workflow(nb: NB):
    nb.lesson("m0-workflow", "Lesson 0.4 — What This Job Actually Is (the data workflow)")
    nb.md(
        "Before we touch more code, let's see the **big picture** of what a data analyst or scientist "
        "actually *does* all day. Almost every real project follows the same six steps:\n\n"
        "| Step | What it means | You'll learn it in… |\n"
        "|---|---|---|\n"
        "| **1. Ask** | Pin down the real question the business needs answered | Module 0 & throughout |\n"
        "| **2. Get** | Collect/load the data (a file, a database, an export) | Module 3 (Pandas) |\n"
        "| **3. Clean** | Fix the mess: typos, blanks, wrong types, duplicates | Module 3 (Pandas) |\n"
        "| **4. Explore** | Slice, filter, group, and summarise to find patterns | Modules 3 & 4 |\n"
        "| **5. Visualise** | Turn findings into clear charts people understand | Module 5 |\n"
        "| **6. Model & Communicate** | Predict the future, then explain it simply | Module 6 + always |\n\n"
        "**Real-world analogy — cooking a meal:** you decide what dish to make (**ask**), buy "
        "ingredients (**get**), wash and chop them (**clean**), taste and adjust (**explore**), plate "
        "it beautifully (**visualise**), and serve it with a description (**communicate**). Data work "
        "is the same recipe, every time.\n\n"
        "**The surprising truth about the job:** steps 3 and 4 — *cleaning and exploring* — eat up "
        "roughly **70–80% of real work time**. Fancy machine learning is often the *smallest* part. "
        "That's why this notebook spends the most time on Pandas. It's not the glamorous part, but "
        "it's where analysts earn their keep."
    )
    nb.realjob(
        "Nobody hands you a perfect spreadsheet. Real data arrives messy, incomplete, and inconsistent "
        "— dates in three formats, blank cells, the same city spelled five ways. The skill that makes "
        "you employable isn't memorising commands; it's calmly turning a mess into something "
        "trustworthy. You'll practise exactly that in Module 3."
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** In a real data project, which step comes **first**?\n\n"
        "- **A)** build a colourful chart\n"
        "- **B)** understand the question you're actually trying to answer\n"
        "- **C)** train a machine-learning model\n"
    )
    nb.practice(
        "m0_q_workflow",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="You can't get useful data or build the right chart until you know the question.",
        label="quiz: workflow order",
    )
    nb.mcq("m0_q_workflow", user="answer", correct="B",
           explanation="Always start by understanding the real question — everything else serves it.",
           hint="Charts and models are useless if they answer the wrong question.")


# --------------------------------------------------------------------------- #
def _roles(nb: NB):
    nb.lesson("m0-roles", "Lesson 0.5 — Data Analyst vs Data Scientist (which are you?)")
    nb.md(
        "People use these titles loosely, and the roles **overlap a lot** — but here's the honest, "
        "plain-English difference. This notebook prepares you for **both**, and we'll point out along "
        "the way which skills lean which direction.\n\n"
        "| | **Data Analyst (DA)** | **Data Scientist (DS)** |\n"
        "|---|---|---|\n"
        "| Core question | *“What happened, and why?”* | *“What will happen, and what should we do?”* |\n"
        "| Daily tools | Pandas, charts, dashboards, **SQL** | All of that **+ machine learning, stats** |\n"
        "| Typical output | Reports, dashboards, clear answers | Predictive models, experiments |\n"
        "| Maths depth | Light–moderate | Moderate–heavy |\n"
        "| This notebook | Modules 1–5 are your bread & butter | Module 6 is where you go further |\n\n"
        "**A helpful way to think about it:** a **Data Analyst** is like a *detective* explaining what "
        "already happened using evidence. A **Data Scientist** is like a *fortune-teller with maths* "
        "who also predicts what happens next. Same crime scene, different job.\n\n"
        "**And a third role you'll hear about — the Data Engineer (DE):** they build the "
        "*plumbing* that delivers clean data to analysts and scientists (we'll cover this in the "
        "Career primer near the end). You don't need to be one, but knowing they exist helps you "
        "understand how a real data team fits together.\n\n"
        "> 💬 **About SQL:** you'll notice SQL in the DA column. It's the language for pulling data out "
        "of databases, and it's essential for real jobs — you'll learn it **right after** this "
        "notebook. We mention it here so the map is complete; everything in *this* notebook is Python."
    )
    nb.role_note(
        "Don't stress about picking a side now. The path is usually **Analyst first, Scientist later**. "
        "Master Modules 1–5 and you're a capable analyst; add Module 6 and you've taken your first real "
        "step toward data science. Same journey, and you're on it."
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** Building a model to **predict** which customers will cancel next month leans more "
        "toward which role?\n\n"
        "- **A)** Data Analyst\n"
        "- **B)** Data Scientist\n"
        "- **C)** neither — that's impossible\n"
    )
    nb.practice(
        "m0_q_roles",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Which role focuses on *predicting the future* with machine learning?",
        label="quiz: DA vs DS",
    )
    nb.mcq("m0_q_roles", user="answer", correct="B",
           explanation="Predicting future outcomes with ML is classic Data Scientist territory "
                       "(though analysts increasingly do it too).",
           hint="Prediction + machine learning = Data Scientist.")


# --------------------------------------------------------------------------- #
def _helpers_recap(nb: NB):
    nb.lesson("m0-helpers", "Lesson 0.6 — Your Toolkit (hints, solutions, score)")
    nb.md(
        "You've already met them, but here's your safety kit for the whole notebook. These are "
        "**always available** after you run the SETUP cells:\n\n"
        "- **`show_hint('key')`** — a gentle nudge when you're stuck (the `key` is shown in each ❌ "
        "message).\n"
        "- **`show_solution('key')`** — reveals the full answer. Try first, but never suffer in "
        "silence.\n"
        "- **`final_report()`** — run it any time (it's the last section) to see your live score, which "
        "modules you've mastered, and what to review.\n\n"
        "Your progress is tracked automatically as you complete exercises. There's no penalty for "
        "retrying — redo any exercise as many times as you like until it clicks. 🔁\n\n"
        "That's everything you need. Take a breath — you're ready. Turn the page to **Module 1** and "
        "let's begin. 🚀"
    )
    nb.keyterms([
        ("Cell", "one block in the notebook — either text to read or code to run."),
        ("Run", "execute a code cell with ▶️ or Shift+Enter; results appear below it."),
        ("Variable", "a named box that stores a value, e.g. `x = 7`."),
        ("Error / traceback", "the computer telling you what it didn't understand — normal and fixable."),
        ("Self-check", "a cell that auto-grades your answer with ✅ or ❌ + a hint."),
        ("Data Analyst vs Data Scientist", "DA explains what happened; DS also predicts what's next."),
    ])

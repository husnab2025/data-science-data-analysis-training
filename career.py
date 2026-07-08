"""
Career Primer — Data Pipelines & Your Roadmap.

A closing, mostly-conceptual lesson (after the capstone, before the final report)
that makes the notebook honest about real work: what DA/DS/DE roles actually do,
what a data pipeline is (ETL/ELT), the gap between a teaching notebook and a real
job, and a concrete skills roadmap (incl. SQL, which the learner studies next).
Kept accessible with plain language, analogies, and a few self-graded quizzes.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _roles(nb)
    _pipelines(nb)
    _real_job_caveats(nb)
    _roadmap(nb)
    _keyterms(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("career", "🧭 Career Primer · Data Pipelines & Your Roadmap")
    nb.md(
        "You've built real skills — congratulations. 🎓 This final teaching section is different: "
        "there are no big coding exercises. Instead, it answers the questions that actually get you "
        "**hired and effective**: *What do these jobs really involve? How does data move through a "
        "company? And what should I learn next?*\n\n"
        "Read it slowly. Understanding the **shape of the work** is what turns a person who can code "
        "into a person who can do the job."
    )
    nb.recap(
        "You've finished all six skill modules and the capstone. This primer zooms out from *how to "
        "code* to *how the job works*, then hands you a concrete roadmap for what comes after this "
        "notebook."
    )


# --------------------------------------------------------------------------- #
def _roles(nb: NB):
    nb.lesson("career-roles", "Who Does What: Analyst, Scientist & Engineer")
    nb.md(
        "A real data team is like a **restaurant kitchen** — different roles, one meal:\n\n"
        "| Role | Kitchen analogy | What they actually deliver |\n"
        "|---|---|---|\n"
        "| **Data Engineer (DE)** | Suppliers + prep cooks who stock the kitchen | Reliable *pipelines* "
        "that move & clean data so it's ready to use (databases, tables, schedules) |\n"
        "| **Data Analyst (DA)** | The chef plating tonight's known dishes | Reports, dashboards, SQL "
        "queries, charts, and clear answers to *“what happened & why?”* |\n"
        "| **Data Scientist (DS)** | The R&D chef inventing new recipes | Experiments, statistical "
        "analysis, and *predictive models* answering *“what's next & what should we do?”* |\n\n"
        "**They overlap constantly** — at a small company one person may do all three. But the "
        "progression most people follow is **Analyst → Scientist**, with Engineering as a separate "
        "(more software-heavy) track.\n\n"
        "**Where this notebook put you:** you can now do the core of the **Analyst** job (Modules 1–5) "
        "and you've taken your first real step into **Science** (Module 6). The **Engineer's** world — "
        "building the pipelines — is what the next lesson explains, so you understand where *your* "
        "clean data actually comes from."
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** Who is mainly responsible for building the **pipelines** that deliver clean, ready-to-"
        "use data to everyone else?\n\n"
        "- **A)** Data Analyst\n- **B)** Data Scientist\n- **C)** Data Engineer\n"
    )
    nb.practice("career_q_roles", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'C'",
                hint="Think about who stocks and preps the kitchen so the chefs can cook.",
                label="quiz: who builds pipelines")
    nb.mcq("career_q_roles", user="answer", correct="C",
           explanation="Data Engineers build and maintain the pipelines that feed analysts & scientists.",
           hint="It's the 'plumbing' role.")


# --------------------------------------------------------------------------- #
def _pipelines(nb: NB):
    nb.lesson("career-pipeline", "What a Data Pipeline Actually Is")
    nb.md(
        "**Plain definition:** a **data pipeline** is a *repeatable, automated path that data follows "
        "from where it's created to where it becomes useful.* Instead of a human copying spreadsheets "
        "around by hand every morning, a pipeline does it reliably, on schedule, forever.\n\n"
        "**Real-world analogy — a city water system.** Water starts at a reservoir (**source**), flows "
        "through pipes to a treatment plant that filters out the junk (**transform/clean**), gets "
        "stored in a tank (**load/store**), and finally comes out of your tap ready to drink "
        "(**dashboard/model/report**). A data pipeline is the same idea, but for information.\n\n"
        "**The typical stages (learn these words — you'll hear them in interviews):**\n\n"
        "1. **Source** — where data is born: apps, websites, sensors, spreadsheets, databases, APIs.\n"
        "2. **Extract** — pull the raw data out of those sources.\n"
        "3. **Transform / Clean** — fix types, remove duplicates, standardise messy values (exactly "
        "the Pandas cleaning you learned in Module 3!).\n"
        "4. **Load / Store** — save the clean result somewhere queryable (usually a database or "
        "'data warehouse').\n"
        "5. **Schedule** — run the whole thing automatically (e.g., every night at 2am).\n"
        "6. **Validate & Monitor** — automatically check the data looks right and alert someone if it "
        "breaks.\n"
        "7. **Serve** — feed the clean data into dashboards, reports, and models people actually use.\n\n"
        "**ETL vs ELT (a common interview term, demystified):**\n"
        "- **ETL** = Extract → **Transform** → Load. You clean the data *before* storing it.\n"
        "- **ELT** = Extract → Load → **Transform**. You store the raw data first, then clean it "
        "*inside* the database. Modern cloud tools made ELT popular.\n\n"
        "You don't need to *build* pipelines to be an analyst — but knowing this is where your clean "
        "data comes from (and being able to say 'ETL' with confidence) makes you far more effective "
        "and credible."
    )
    nb.realjob(
        "The Pandas `.str.strip().str.lower()`, `dropna()`, `fillna()`, and `merge()` you practised in "
        "Module 3 are the *exact* operations that run inside the **Transform** stage of real pipelines "
        "— just scheduled to run automatically on millions of rows instead of by hand. You already "
        "know the hardest part."
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** In **ETL**, what does the middle letter **T** stand for?\n\n"
        "- **A)** Transfer\n- **B)** Transform (clean/reshape the data)\n- **C)** Test\n"
    )
    nb.practice("career_q_etl", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'",
                hint="It's the stage where you clean and reshape — your Module 3 Pandas skills.",
                label="quiz: ETL")
    nb.mcq("career_q_etl", user="answer", correct="B",
           explanation="ETL = Extract, Transform (clean/reshape), Load.",
           hint="Think 'clean and reshape'.")


# --------------------------------------------------------------------------- #
def _real_job_caveats(nb: NB):
    nb.lesson("career-reality", "Notebook vs Reality: Honest Caveats")
    nb.md(
        "This notebook is a *teaching* environment. To keep it self-contained (runnable anywhere with "
        "no setup), a few things were simplified. Here's the honest gap between here and a real job — "
        "so you're never caught off guard:\n\n"
        "| In this notebook… | In a real job… |\n"
        "|---|---|\n"
        "| CSVs are typed as **text strings** (`io.StringIO`) so nothing needs downloading | Data comes "
        "from real **files, URLs, databases, cloud storage, and APIs** — often needing passwords/access |\n"
        "| Datasets are tiny, clean, and **generated to be tidy** | Data is **big, messy, incomplete, "
        "and poorly documented** — cleaning dominates the work |\n"
        "| Every answer has one exact right value | Real questions are **ambiguous**; you clarify what "
        "the stakeholder *really* means |\n"
        "| Models hit near-perfect scores on toy data | Real models are **imperfect**; a modest, honest "
        "score beats a suspiciously perfect one |\n"
        "| You work alone in one file | You collaborate using **Git/GitHub**, code review, and shared "
        "databases |\n\n"
        "**Three professional habits the toy setting can't teach — but that make you stand out:**\n"
        "- **Document your assumptions.** Write down what you assumed and why. Future-you (and your "
        "team) will thank you.\n"
        "- **Communicate uncertainty.** Say *“sales will likely rise 5–8%”*, not *“sales will be "
        "6.3%”*. Honesty about confidence builds trust.\n"
        "- **Make it reproducible.** Anyone should be able to re-run your work and get the same result "
        "— that's why analysts write **code** instead of clicking around in a spreadsheet."
    )
    nb.gotcha(
        "The single biggest rookie trap: presenting a **suspiciously perfect** result (100% accuracy, "
        "R² = 1.0). In the real world that almost always means a mistake — like accidentally letting "
        "the model peek at the answers ('data leakage'). Perfect scores should make you *suspicious*, "
        "not proud."
    )


# --------------------------------------------------------------------------- #
def _roadmap(nb: NB):
    nb.lesson("career-roadmap", "Your Roadmap: What To Learn Next")
    nb.md(
        "You've built a genuine **foundation**. Here's the honest, ordered path from here to "
        "job-ready. You don't need all of it before applying — but each step compounds.\n\n"
        "**1. SQL — do this next. 🎯** The #1 most-requested skill in analyst job ads. It's how you "
        "pull data out of databases (where real company data lives). You're already primed: a SQL "
        "table is just a DataFrame, and `WHERE`/`GROUP BY`/`JOIN` map directly onto the Pandas "
        "filtering, `groupby`, and `merge` you already know.\n\n"
        "**2. Statistics basics.** Median, variance/standard deviation, percentiles, correlation vs "
        "causation, and a gentle intro to significance / A-B testing. This is what separates a chart-"
        "maker from a trusted analyst.\n\n"
        "**3. A dashboard / BI tool.** Power BI, Tableau, or Looker — how businesses actually consume "
        "your analysis day-to-day.\n\n"
        "**4. Git & GitHub.** Version control for your code. Non-negotiable on any real team, and it's "
        "where your portfolio lives.\n\n"
        "**5. Excel / Google Sheets fluency.** Still everywhere. Pivot tables, `VLOOKUP`/`XLOOKUP`, "
        "basic formulas.\n\n"
        "**6. Build 2–3 portfolio projects.** Grab a **real** public dataset (Kaggle, "
        "data.gov, a city open-data portal), run the full workflow you learned, and write up what you "
        "found. This is what you show in interviews — it matters more than any certificate.\n\n"
        "**7. Practice interviewing.** Explaining your thinking out loud, simple SQL/Pandas questions, "
        "and 'tell me about a project' stories.\n\n"
        "**Deeper Pandas/stats topics worth circling back to** (you've met the foundations; these are "
        "the natural next layer): `pivot_table`, working with **dates/times**, left/right/outer "
        "**joins**, spotting **duplicates & outliers**, and model metrics like **MAE/RMSE** "
        "(regression) and **precision/recall & the confusion matrix** (classification)."
    )
    nb.md(
        "### 🎯 Your turn — commit to your next step\n"
        "No trick here — just lock in the plan. Set `my_next_step` to the string of the skill you "
        "should learn **immediately after** this notebook (hint: it's the #1 analyst skill above)."
    )
    nb.practice(
        "career_next",
        placeholder='my_next_step = None  # the ONE skill to learn next (a short string, e.g. "SQL")',
        solution='my_next_step = "SQL"',
        hint='It\'s three letters, pulls data from databases, and maps onto your Pandas skills: "SQL".',
        label="commit to next step",
    )
    nb.check("career_next", user='str(my_next_step).strip().upper()', expected="'SQL'",
             hint='Set my_next_step = "SQL" — your immediate next skill.')
    nb.md(
        "> 🌟 **A final word.** Nobody becomes job-ready from one notebook — and that's OK. What you've "
        "done is build the *foundation the whole career stands on*, and prove to yourself that you can "
        "learn this. That mindset — patient, curious, willing to see ❌ and try again — is the real "
        "job skill. Keep going. 🚀"
    )


# --------------------------------------------------------------------------- #
def _keyterms(nb: NB):
    nb.lesson("career-terms", "Career Primer — Key Terms")
    nb.keyterms([
        ("Data pipeline", "an automated, repeatable path that moves data from source to useful output."),
        ("ETL / ELT", "Extract-Transform-Load (clean then store) vs Extract-Load-Transform (store then clean)."),
        ("Data warehouse", "a big, queryable store where clean company data lives (you'll query it with SQL)."),
        ("Data Engineer", "builds and maintains the pipelines & storage that feed analysts and scientists."),
        ("Reproducibility", "anyone can re-run your work and get the same result — a core reason to use code."),
        ("Data leakage", "accidentally letting a model see the answers, causing fake-perfect scores."),
        ("Portfolio project", "an end-to-end analysis on real data that you show employers — your best proof."),
        ("Stakeholder", "the person who needs the answer; your job is to give them something they can act on."),
    ])

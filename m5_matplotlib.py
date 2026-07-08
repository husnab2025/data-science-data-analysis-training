"""
Module 5 — Matplotlib (+ brief Seaborn).

figure/axes · line · bar · pie (when appropriate) · histogram · scatter ·
labels/titles/legends · subplots · box plots · correlation heatmap (Seaborn) ·
choosing the right chart · Module 5 test.

Grading: plot code is verified by executing the filled build; each self-check
grades a plain data fact or a plot attribute (e.g. the title), all None-safe.
`plt`, `sns`, `np`, `pd` are imported by the setup cell.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_line(nb)
    _lesson_bar(nb)
    _lesson_pie(nb)
    _lesson_hist(nb)
    _lesson_scatter(nb)
    _lesson_labels(nb)
    _lesson_subplots(nb)
    _lesson_box(nb)
    _lesson_heatmap(nb)
    _lesson_choosing(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod5", "Module 5 · Matplotlib & Seaborn (Visualisation)")
    nb.md(
        "Numbers in a table rarely persuade anyone. **Charts** do. Matplotlib is Python's core "
        "plotting library; **Seaborn** is a friendly layer on top that makes statistical charts "
        "beautiful with less code.\n\n"
        "**Why it matters for the job:** a huge part of an analyst's value is *communication*. A "
        "clear chart in a slide or dashboard is what turns your analysis into a decision. Executives "
        "don't read DataFrames — they look at trends, comparisons, and outliers you visualise for "
        "them.\n\n"
        "**The mental model:** a **figure** is the whole canvas; an **axes** (`ax`) is one plot on "
        "it. You draw onto an `ax` (`ax.plot`, `ax.bar`, …), then label it and show it. Master that "
        "pattern and every chart type follows the same rhythm."
    )
    nb.role_note(
        "Charts are where **both** roles earn trust. A Data Analyst builds dashboards and report "
        "visuals so a business can see what happened; a Data Scientist adds charts that explain a "
        "*model's* behaviour. Either way, a clear chart is often more persuasive than any number."
    )


# --------------------------------------------------------------------------- #
def _lesson_line(nb: NB):
    nb.lesson("m5-line", "Lesson 5.1 — Figure/Axes Basics & the Line Chart")
    nb.md(
        "**What it is.** `fig, ax = plt.subplots()` creates a canvas and one plot. `ax.plot(x, y)` "
        "draws a **line** connecting points in order.\n\n"
        "**Why it exists.** Line charts are the go-to for a value **changing over time** — the shape "
        "of the line tells the story instantly.\n\n"
        "**Real-world analogy.** A heart-rate monitor or a stock ticker: a continuous line rising and "
        "falling over time.\n\n"
        "**On the job.** Revenue by month, active users by week, temperature by hour — any time series "
        "starts as a line chart."
    )
    nb.md("**Worked example:**")
    nb.code(
        'months = [1, 2, 3, 4, 5]\n'
        'revenue = [100, 130, 90, 160, 200]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.plot(months, revenue, marker="o")   # marker shows each data point\n'
        'ax.set_title("Monthly Revenue")\n'
        'ax.set_xlabel("Month")\n'
        'ax.set_ylabel("Revenue ($)")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Draw a line chart of `days` vs `visitors` (title it, label the axes), then store the peak "
        "value in `peak_visitors`."
    )
    nb.practice(
        "m5_line",
        placeholder=(
            'days = [1, 2, 3, 4, 5]\n'
            'visitors = [50, 80, 65, 120, 90]\n'
            '\n'
            '# YOUR CODE HERE — make a line chart (fig, ax = plt.subplots(); ax.plot(...); ...)\n'
            '\n'
            'peak_visitors = None  # the highest visitors value'
        ),
        solution=(
            'days = [1, 2, 3, 4, 5]\n'
            'visitors = [50, 80, 65, 120, 90]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.plot(days, visitors, marker="o")\n'
            'ax.set_title("Daily Visitors")\n'
            'ax.set_xlabel("Day")\n'
            'ax.set_ylabel("Visitors")\n'
            'plt.show()\n'
            '\n'
            'peak_visitors = max(visitors)'
        ),
        hint="plt.subplots(), ax.plot(days, visitors), then peak_visitors = max(visitors).",
        label="line chart",
    )
    nb.check("m5_line", user="peak_visitors", expected="120",
             hint="The largest visitor count is 120.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** Which chart best shows a value **changing over time**?\n\n"
        "- **A)** pie\n- **B)** line\n- **C)** scatter\n"
    )
    nb.practice("m5_q_line", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="Think of a stock ticker.", label="quiz: line")
    nb.mcq("m5_q_line", user="answer", correct="B",
           explanation="Line charts are the standard for trends over time.", hint="Trend over time.")


# --------------------------------------------------------------------------- #
def _lesson_bar(nb: NB):
    nb.lesson("m5-bar", "Lesson 5.2 — Bar Charts")
    nb.md(
        "**What it is.** `ax.bar(categories, values)` draws one bar per **category** — the height is "
        "the value.\n\n"
        "**Why it exists.** Bars are the clearest way to **compare distinct categories** (products, "
        "regions, teams). The eye compares bar heights effortlessly.\n\n"
        "**Real-world analogy.** A row of stacked-coin towers — the tallest tower wins at a glance.\n\n"
        "**On the job.** Sales by product, headcount by department, tickets by priority — comparisons "
        "across a handful of labels."
    )
    nb.md("**Worked example:**")
    nb.code(
        'products = ["A", "B", "C"]\n'
        'sales = [300, 150, 500]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.bar(products, sales, color="steelblue")\n'
        'ax.set_title("Sales by Product")\n'
        'ax.set_ylabel("Sales ($)")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Make a bar chart of `regions` vs `totals`, then store the name of the top region in "
        "`top_region`."
    )
    nb.practice(
        "m5_bar",
        placeholder=(
            'regions = ["North", "South", "East"]\n'
            'totals = [400, 250, 600]\n'
            '\n'
            '# YOUR CODE HERE — a bar chart of regions vs totals\n'
            '\n'
            'top_region = None  # the region with the highest total'
        ),
        solution=(
            'regions = ["North", "South", "East"]\n'
            'totals = [400, 250, 600]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.bar(regions, totals)\n'
            'ax.set_title("Sales by Region")\n'
            'ax.set_xlabel("Region")\n'
            'ax.set_ylabel("Sales")\n'
            'plt.show()\n'
            '\n'
            'top_region = regions[totals.index(max(totals))]'
        ),
        hint="ax.bar(regions, totals); the top is regions[totals.index(max(totals))].",
        label="bar chart",
    )
    nb.check("m5_bar", user="top_region", expected="'East'",
             hint="East has the tallest bar at 600.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** Bar charts are best for…?\n\n"
        "- **A)** comparing categories\n- **B)** showing a correlation\n- **C)** a single proportion\n"
    )
    nb.practice("m5_q_bar", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="One bar per label, compared by height.",
                label="quiz: bar")
    nb.mcq("m5_q_bar", user="answer", correct="A",
           explanation="Bars compare values across distinct categories.", hint="Category comparison.")


# --------------------------------------------------------------------------- #
def _lesson_pie(nb: NB):
    nb.lesson("m5-pie", "Lesson 5.3 — Pie Charts (and when NOT to use them)")
    nb.md(
        "**What it is.** `ax.pie(values, labels=...)` shows each value as a slice of a whole — good "
        "for **proportions that add up to 100%**.\n\n"
        "**⚠️ Use with care.** Humans are bad at comparing angles. Pie charts only work with a **few** "
        "slices of clearly different sizes. With many categories, or similar sizes, a **bar chart is "
        "almost always clearer**. Many data teams avoid pies entirely.\n\n"
        "**Real-world analogy.** Slices of an actual pie — obvious for 'half vs a quarter', useless "
        "for telling 11% from 12%.\n\n"
        "**On the job.** A single budget or market-share breakdown into 3–4 parts is a fair pie; for "
        "anything more, reach for bars."
    )
    nb.md("**Worked example:**")
    nb.code(
        'shares = [50, 30, 20]\n'
        'labels = ["Product A", "Product B", "Product C"]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.pie(shares, labels=labels, autopct="%1.0f%%")   # autopct shows the %\n'
        'ax.set_title("Market Share")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Make a pie chart of a monthly `budget`, then store the **total budget** in `total_budget` and "
        "the **label of the largest slice** in `largest_slice`."
    )
    nb.practice(
        "m5_pie",
        placeholder=(
            'budget = [1200, 800, 500, 300]\n'
            'categories = ["Rent", "Food", "Transport", "Fun"]\n'
            '\n'
            '# YOUR CODE HERE — a pie chart of budget with those labels\n'
            '\n'
            'total_budget = None    # sum of the budget\n'
            'largest_slice = None   # the category with the biggest amount'
        ),
        solution=(
            'budget = [1200, 800, 500, 300]\n'
            'categories = ["Rent", "Food", "Transport", "Fun"]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.pie(budget, labels=categories, autopct="%1.1f%%")\n'
            'ax.set_title("Budget Breakdown")\n'
            'plt.show()\n'
            '\n'
            'total_budget = sum(budget)\n'
            'largest_slice = categories[budget.index(max(budget))]'
        ),
        hint="ax.pie(budget, labels=categories); sum(budget); "
             "categories[budget.index(max(budget))].",
        label="pie chart",
    )
    nb.check("m5_pie", user="(total_budget, largest_slice)",
             expected="(2800, 'Rent')",
             hint="Budget totals 2800 and Rent (1200) is the biggest slice.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** A pie chart is **least** appropriate when…?\n\n"
        "- **A)** you have a few slices summing to a whole\n"
        "- **B)** you have many categories of similar size\n- **C)** you show a single proportion\n"
    )
    nb.practice("m5_q_pie", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'",
                hint="Angles are hard to compare when there are many similar slices.",
                label="quiz: pie limits")
    nb.mcq("m5_q_pie", user="answer", correct="B",
           explanation="Many similar-sized slices are unreadable as a pie — use bars.",
           hint="Similar sizes + many categories = bad pie.")


# --------------------------------------------------------------------------- #
def _lesson_hist(nb: NB):
    nb.lesson("m5-hist", "Lesson 5.4 — Histograms (the shape of one variable)")
    nb.md(
        "**What it is.** `ax.hist(values, bins=n)` splits a numeric variable into ranges ('bins') and "
        "shows how many values fall in each — revealing the **distribution**.\n\n"
        "**Histogram vs bar chart:** a bar chart compares *named categories*; a histogram shows the "
        "*spread of one numeric variable*. Different jobs!\n\n"
        "**Why it exists.** The average hides the story. A histogram shows whether data is centred, "
        "skewed, bimodal, or full of outliers.\n\n"
        "**Real-world analogy.** Sorting a class's test scores into grade bands and seeing how tall "
        "each band's stack is.\n\n"
        "**On the job.** Checking the distribution of order values, ages, or response times before "
        "choosing a metric or spotting anomalies."
    )
    nb.md("**Worked example:**")
    nb.code(
        'order_values = [12, 15, 18, 22, 23, 25, 25, 27, 30, 31, 34, 40, 41, 55]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.hist(order_values, bins=5, edgecolor="black")\n'
        'ax.set_title("Distribution of Order Values")\n'
        'ax.set_xlabel("Order value ($)")\n'
        'ax.set_ylabel("Frequency")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Draw a histogram of `scores`, then store how many scores are **80 or above** in "
        "`high_count`."
    )
    nb.practice(
        "m5_hist",
        placeholder=(
            'scores = [55, 62, 70, 71, 72, 80, 85, 88, 90, 95]\n'
            '\n'
            '# YOUR CODE HERE — a histogram of scores (try bins=5)\n'
            '\n'
            'high_count = None  # how many scores are >= 80'
        ),
        solution=(
            'scores = [55, 62, 70, 71, 72, 80, 85, 88, 90, 95]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.hist(scores, bins=5, edgecolor="black")\n'
            'ax.set_title("Score Distribution")\n'
            'ax.set_xlabel("Score")\n'
            'ax.set_ylabel("Frequency")\n'
            'plt.show()\n'
            '\n'
            'high_count = len([s for s in scores if s >= 80])'
        ),
        hint="ax.hist(scores, bins=5); then count with a comprehension: [s for s in scores if s >= 80].",
        label="histogram",
    )
    nb.check("m5_hist", user="high_count", expected="5",
             hint="80, 85, 88, 90, 95 → five scores at or above 80.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** A histogram shows…?\n\n"
        "- **A)** the distribution/spread of one numeric variable\n"
        "- **B)** comparisons between named categories\n- **C)** correlation between two variables\n"
    )
    nb.practice("m5_q_hist", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="It bins one numeric variable.",
                label="quiz: histogram")
    nb.mcq("m5_q_hist", user="answer", correct="A",
           explanation="Histograms reveal how one numeric variable is distributed.",
           hint="Spread of one variable.")


# --------------------------------------------------------------------------- #
def _lesson_scatter(nb: NB):
    nb.lesson("m5-scatter", "Lesson 5.5 — Scatter Plots (relationships)")
    nb.md(
        "**What it is.** `ax.scatter(x, y)` plots one dot per observation, using two numeric "
        "variables — revealing whether they **move together** (correlation).\n\n"
        "**Why it exists.** To answer 'does X relate to Y?' — does ad spend drive sales? do study "
        "hours raise scores? An upward cloud = positive relationship.\n\n"
        "**Real-world analogy.** Plotting each student as a dot of (hours studied, grade) and seeing "
        "the cloud tilt upward.\n\n"
        "**On the job.** The first look before any modelling: scatter your feature against your target "
        "to see if a relationship even exists."
    )
    nb.md("**Worked example:**")
    nb.code(
        'ad_spend = [10, 20, 30, 40, 50]\n'
        'sales = [100, 180, 260, 300, 380]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.scatter(ad_spend, sales)\n'
        'ax.set_title("Ad Spend vs Sales")\n'
        'ax.set_xlabel("Ad Spend ($)")\n'
        'ax.set_ylabel("Sales ($)")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Scatter `hours` against `score`. Then compute the correlation with "
        "`np.corrcoef(hours, score)[0, 1]` and store whether it's positive in "
        "`positive_relationship` (a `True`/`False`)."
    )
    nb.practice(
        "m5_scatter",
        placeholder=(
            'hours = [1, 2, 3, 4, 5, 6]\n'
            'score = [50, 55, 65, 70, 80, 85]\n'
            '\n'
            '# YOUR CODE HERE — a scatter plot of hours vs score\n'
            '\n'
            'positive_relationship = None  # True if the correlation is > 0'
        ),
        solution=(
            'hours = [1, 2, 3, 4, 5, 6]\n'
            'score = [50, 55, 65, 70, 80, 85]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.scatter(hours, score)\n'
            'ax.set_title("Study Hours vs Score")\n'
            'ax.set_xlabel("Hours")\n'
            'ax.set_ylabel("Score")\n'
            'plt.show()\n'
            '\n'
            'positive_relationship = bool(np.corrcoef(hours, score)[0, 1] > 0)'
        ),
        hint="ax.scatter(hours, score); then bool(np.corrcoef(hours, score)[0, 1] > 0).",
        label="scatter plot",
    )
    nb.check("m5_scatter", user="positive_relationship", expected="True",
             hint="More hours goes with higher scores → a positive correlation.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** To see whether two numeric variables move together, use a…?\n\n"
        "- **A)** scatter plot\n- **B)** pie chart\n- **C)** histogram\n"
    )
    nb.practice("m5_q_scatter", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="One dot per (x, y) observation.",
                label="quiz: scatter")
    nb.mcq("m5_q_scatter", user="answer", correct="A",
           explanation="Scatter plots reveal relationships between two numeric variables.",
           hint="Relationship between two variables.")
    nb.gotcha(
        "**Correlation is not causation.** A scatter plot showing ice-cream sales and drowning "
        "deaths rising together doesn't mean ice cream causes drowning — *summer* drives both. When "
        "two things move together, resist saying one *causes* the other. Proving causation needs a "
        "controlled experiment (like an A/B test), not just a chart. This is one of the most important "
        "professional habits you can build."
    )


# --------------------------------------------------------------------------- #
def _lesson_labels(nb: NB):
    nb.lesson("m5-labels", "Lesson 5.6 — Titles, Axis Labels & Legends")
    nb.md(
        "**What it is.** A chart without labels is a puzzle. Always add:\n\n"
        "- `ax.set_title(\"...\")` — what the chart shows.\n"
        "- `ax.set_xlabel(\"...\")` / `ax.set_ylabel(\"...\")` — what each axis means (with units).\n"
        "- `ax.legend()` — a key identifying each series (needs `label=\"...\"` on each plot call).\n\n"
        "**Why it exists.** Your audience wasn't in your head. Labels make a chart self-explanatory "
        "and trustworthy.\n\n"
        "**Real-world analogy.** A map with no legend or street names — pretty, but useless for "
        "navigation.\n\n"
        "**On the job.** Unlabelled charts get sent back. Labelling is the difference between "
        "'a picture' and 'a finding'."
    )
    nb.md("**Worked example — two series with a legend:**")
    nb.code(
        'x = [1, 2, 3, 4]\n'
        'a = [10, 20, 30, 40]\n'
        'b = [40, 30, 20, 10]\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.plot(x, a, label="Product A")\n'
        'ax.plot(x, b, label="Product B")\n'
        'ax.set_title("A vs B")\n'
        'ax.set_xlabel("Quarter")\n'
        'ax.set_ylabel("Sales")\n'
        'ax.legend()\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Plot the two teams, add a **legend**, and give the chart the exact title "
        "`\"Team Comparison\"`. Then store the chart's title with `ax.get_title()` in `title_text`."
    )
    nb.practice(
        "m5_labels",
        placeholder=(
            'x = [1, 2, 3]\n'
            'team_a = [5, 10, 15]\n'
            'team_b = [15, 10, 5]\n'
            '\n'
            '# YOUR CODE HERE — plot both teams (with label=...), set title "Team Comparison",\n'
            '# label axes, add ax.legend(), then read the title back:\n'
            'title_text = None  # ax.get_title()'
        ),
        solution=(
            'x = [1, 2, 3]\n'
            'team_a = [5, 10, 15]\n'
            'team_b = [15, 10, 5]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.plot(x, team_a, label="Team A")\n'
            'ax.plot(x, team_b, label="Team B")\n'
            'ax.set_title("Team Comparison")\n'
            'ax.set_xlabel("Round")\n'
            'ax.set_ylabel("Points")\n'
            'ax.legend()\n'
            'plt.show()\n'
            '\n'
            'title_text = ax.get_title()'
        ),
        hint='Set ax.set_title("Team Comparison"), call ax.legend(), then title_text = ax.get_title().',
        label="labels & legend",
    )
    nb.check("m5_labels", user="title_text", expected="'Team Comparison'",
             hint="The stored title must exactly match the string you set.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q6.** What does `ax.legend()` add to a chart?\n\n"
        "- **A)** a key identifying each series\n- **B)** the chart title\n- **C)** gridlines\n"
    )
    nb.practice("m5_q_labels", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="It explains which line/bar is which.",
                label="quiz: legend")
    nb.mcq("m5_q_labels", user="answer", correct="A",
           explanation="The legend maps each label= to its series.", hint="It's the key.")


# --------------------------------------------------------------------------- #
def _lesson_subplots(nb: NB):
    nb.lesson("m5-subplots", "Lesson 5.7 — Subplots (several charts, one figure)")
    nb.md(
        "**What it is.** `plt.subplots(rows, cols)` returns a figure and a **grid of axes**. Index "
        "into `axes` to draw on each one: `axes[0]`, `axes[1]`, …\n\n"
        "**Why it exists.** Dashboards show several related views side by side; subplots let you build "
        "them in one figure.\n\n"
        "**Real-world analogy.** A car dashboard: speed, fuel, and temperature gauges grouped on one "
        "panel.\n\n"
        "**On the job.** A single figure with 'trend', 'by-category', and 'distribution' panels is a "
        "compact, powerful summary for a report."
    )
    nb.md("**Worked example — 1 row, 2 columns:**")
    nb.code(
        'fig, axes = plt.subplots(1, 2, figsize=(10, 4))\n'
        '\n'
        'axes[0].plot([1, 2, 3], [1, 4, 9])\n'
        'axes[0].set_title("Left: line")\n'
        '\n'
        'axes[1].bar(["A", "B"], [3, 7])\n'
        'axes[1].set_title("Right: bar")\n'
        '\n'
        'plt.tight_layout()   # stop titles/labels overlapping\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Create a **1×2** subplot grid (a line on the left, a bar on the right), then store the number "
        "of axes with `len(axes)` in `n_axes`."
    )
    nb.practice(
        "m5_subplots",
        placeholder=(
            '# YOUR CODE HERE — fig, axes = plt.subplots(1, 2, ...); draw on axes[0] and axes[1]\n'
            '\n'
            'n_axes = None  # how many axes did you create? use len(axes)'
        ),
        solution=(
            'fig, axes = plt.subplots(1, 2, figsize=(10, 4))\n'
            'axes[0].plot([1, 2, 3], [2, 4, 6])\n'
            'axes[0].set_title("Line")\n'
            'axes[1].bar(["X", "Y", "Z"], [5, 3, 8])\n'
            'axes[1].set_title("Bar")\n'
            'plt.tight_layout()\n'
            'plt.show()\n'
            '\n'
            'n_axes = len(axes)'
        ),
        hint="plt.subplots(1, 2) gives two axes; n_axes = len(axes).",
        label="subplots",
    )
    nb.check("m5_subplots", user="n_axes", expected="2",
             hint="A 1×2 grid has 2 axes.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q7.** `plt.subplots(2, 3)` creates how many individual plots (axes)?\n\n"
        "- **A)** 5\n- **B)** 6\n- **C)** 1\n"
    )
    nb.practice("m5_q_subplots", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="Rows × columns.", label="quiz: subplots")
    nb.mcq("m5_q_subplots", user="answer", correct="B",
           explanation="2 rows × 3 columns = 6 axes.", hint="Multiply rows by columns.")


# --------------------------------------------------------------------------- #
def _lesson_box(nb: NB):
    nb.lesson("m5-box", "Lesson 5.8 — Box Plots (compare distributions)")
    nb.md(
        "**What it is.** A **box plot** summarises a distribution in one compact shape: the box spans "
        "the middle 50% (the quartiles), the line inside is the **median**, the whiskers reach out to "
        "the typical low and high values (roughly within 1.5× the box's height), and separate dots "
        "beyond them mark **outliers**.\n\n"
        "**Why it exists.** It compares the *spread* of several groups at a glance — far more "
        "informative than comparing their averages alone.\n\n"
        "**Real-world analogy.** Comparing exam results across three classes: not just who scored "
        "higher on average, but who was consistent vs all over the place.\n\n"
        "**On the job.** Comparing delivery times across warehouses, or salaries across teams — box "
        "plots instantly reveal spread and outliers side by side."
    )
    nb.md("**Worked example:**")
    nb.code(
        'group_a = [20, 22, 25, 27, 30, 35, 40]\n'
        'group_b = [15, 18, 20, 22, 24, 26, 50]   # note the outlier at 50\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.boxplot([group_a, group_b])\n'
        'ax.set_xticks([1, 2])\n'
        'ax.set_xticklabels(["Group A", "Group B"])\n'
        'ax.set_title("Distribution by Group")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Box-plot the two groups, then store the **median** of `group_a` in `median_a` "
        "(use `np.median`)."
    )
    nb.practice(
        "m5_box",
        placeholder=(
            'group_a = [10, 12, 14, 16, 18, 20, 22]\n'
            'group_b = [5, 10, 15, 20, 25, 30, 60]\n'
            '\n'
            '# YOUR CODE HERE — a box plot comparing group_a and group_b\n'
            '\n'
            'median_a = None  # the median of group_a (float(np.median(group_a)))'
        ),
        solution=(
            'group_a = [10, 12, 14, 16, 18, 20, 22]\n'
            'group_b = [5, 10, 15, 20, 25, 30, 60]\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.boxplot([group_a, group_b])\n'
            'ax.set_xticks([1, 2])\n'
            'ax.set_xticklabels(["A", "B"])\n'
            'ax.set_title("Group Comparison")\n'
            'plt.show()\n'
            '\n'
            'median_a = float(np.median(group_a))'
        ),
        hint="ax.boxplot([group_a, group_b]); median_a = float(np.median(group_a)).",
        label="box plot",
    )
    nb.check("m5_box", user="median_a", expected="16.0",
             hint="The middle value of group_a is 16.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q8.** A box plot is especially good for…?\n\n"
        "- **A)** comparing the spread/distribution of groups\n"
        "- **B)** reading exact individual values\n- **C)** showing parts of a whole\n"
    )
    nb.practice("m5_q_box", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Median, quartiles, outliers across groups.",
                label="quiz: box plot")
    nb.mcq("m5_q_box", user="answer", correct="A",
           explanation="Box plots summarise and compare the distribution of groups.",
           hint="Spread and outliers.")


# --------------------------------------------------------------------------- #
def _lesson_heatmap(nb: NB):
    nb.lesson("m5-heatmap", "Lesson 5.9 — Correlation Heatmap (Seaborn)")
    nb.md(
        "**What it is.** A **heatmap** colours a grid of numbers so patterns pop out. The most common "
        "analyst use is a **correlation heatmap**: `df.corr()` computes how strongly every pair of "
        "numeric columns moves together (−1 to +1), and `sns.heatmap(...)` colours it.\n\n"
        "**Why it exists.** With many columns, reading a correlation *table* is tedious; colour lets "
        "you spot the strong (dark) relationships instantly.\n\n"
        "**Real-world analogy.** A weather map where warm colours flag hot spots — here, strong "
        "relationships.\n\n"
        "**On the job.** Before modelling, a correlation heatmap shows which features relate to your "
        "target (and which are redundant with each other)."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({\n'
        '    "ad_spend": [10, 20, 30, 40, 50],\n'
        '    "sales":    [100, 180, 260, 300, 380],\n'
        '    "returns":  [5, 4, 3, 2, 1],\n'
        '})\n'
        '\n'
        'corr = df.corr()                       # correlation matrix\n'
        'fig, ax = plt.subplots()\n'
        'sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)   # annot writes the numbers\n'
        'ax.set_title("Correlation Heatmap")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Build the correlation matrix of `df` with `df.corr()` and draw a heatmap. Then store whether "
        "`hours` and `score` are **strongly positively** correlated (correlation > 0.9) in "
        "`strong_positive`."
    )
    nb.practice(
        "m5_heatmap",
        placeholder=(
            'df = pd.DataFrame({"hours": [1, 2, 3, 4, 5], "score": [52, 58, 63, 71, 79]})\n'
            '\n'
            '# YOUR CODE HERE — corr = df.corr(); sns.heatmap(corr, annot=True, ax=ax)\n'
            '\n'
            'strong_positive = None  # True if corr between hours and score is > 0.9'
        ),
        solution=(
            'df = pd.DataFrame({"hours": [1, 2, 3, 4, 5], "score": [52, 58, 63, 71, 79]})\n'
            '\n'
            'corr = df.corr()\n'
            'fig, ax = plt.subplots()\n'
            'sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)\n'
            'ax.set_title("Correlation")\n'
            'plt.show()\n'
            '\n'
            'strong_positive = bool(corr.loc["hours", "score"] > 0.9)'
        ),
        hint='corr = df.corr(); sns.heatmap(corr, annot=True, ax=ax); '
             'then bool(corr.loc["hours", "score"] > 0.9).',
        label="correlation heatmap",
    )
    nb.check("m5_heatmap", user="strong_positive", expected="True",
             hint="hours and score rise together almost perfectly.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q9.** A correlation heatmap uses colour to show…?\n\n"
        "- **A)** how strongly variables relate to each other\n- **B)** geographic locations\n"
        "- **C)** time trends\n"
    )
    nb.practice("m5_q_heatmap", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="It colours a correlation matrix.",
                label="quiz: heatmap")
    nb.mcq("m5_q_heatmap", user="answer", correct="A",
           explanation="Colour encodes correlation strength between variable pairs.",
           hint="Strength of relationships.")


# --------------------------------------------------------------------------- #
def _lesson_choosing(nb: NB):
    nb.lesson("m5-choose", "Lesson 5.10 — Choosing the Right Chart")
    nb.md(
        "**The analyst's cheat-sheet** — match the *question* to the chart:\n\n"
        "| Your question | Best chart |\n"
        "|---|---|\n"
        "| How does it change **over time**? | **line** |\n"
        "| How do **categories** compare? | **bar** |\n"
        "| What are the **parts of a whole** (few)? | **pie** (sparingly) |\n"
        "| What's the **spread** of one variable? | **histogram** or **box** |\n"
        "| Do two variables **relate**? | **scatter** |\n"
        "| How do **many variables** correlate? | **heatmap** |\n\n"
        "**Why it matters.** Choosing the wrong chart hides the story or, worse, misleads. Picking the "
        "right one is a core analyst skill — and a frequent interview question."
    )
    nb.md(
        "### 🎯 Your turn — pick the chart\n"
        "For each scenario, set the variable to the best chart type as a lowercase string "
        "(`\"line\"`, `\"bar\"`, `\"scatter\"`, `\"histogram\"`, `\"pie\"`, or `\"heatmap\"`)."
    )
    nb.practice(
        "m5_choose",
        placeholder=(
            '# Monthly revenue across a year:\n'
            'chart_for_revenue_trend = None\n'
            '# Comparing total sales of 5 products:\n'
            'chart_for_product_comparison = None\n'
            '# Whether advertising spend relates to sales:\n'
            'chart_for_spend_vs_sales = None'
        ),
        solution=(
            'chart_for_revenue_trend = "line"\n'
            'chart_for_product_comparison = "bar"\n'
            'chart_for_spend_vs_sales = "scatter"'
        ),
        hint="Over time → line; compare categories → bar; relationship between two numbers → scatter.",
        label="choose the chart",
    )
    nb.check("m5_choose",
             user="(chart_for_revenue_trend, chart_for_product_comparison, chart_for_spend_vs_sales)",
             expected="('line', 'bar', 'scatter')",
             hint="Trend=line, category comparison=bar, relationship=scatter.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q10.** Best chart to compare **average salary across 5 departments**?\n\n"
        "- **A)** bar\n- **B)** histogram\n- **C)** scatter\n"
    )
    nb.practice("m5_q_choose", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Comparing named categories.", label="quiz: choose")
    nb.mcq("m5_q_choose", user="answer", correct="A",
           explanation="Departments are categories → a bar chart.", hint="Categories → bar.")
    nb.tip(
        "Two habits that separate amateur charts from professional ones: (1) **always label** the "
        "title and both axes — an unlabelled chart is a puzzle; (2) **don't mislead** — start bar-chart "
        "y-axes at zero, or a tiny difference looks huge. An honest, clearly-labelled chart is a mark "
        "of a trustworthy analyst."
    )
    nb.keyterms([
        ("figure / axes", "the whole canvas / one individual plot on it (you draw on `ax`)."),
        ("line / bar / scatter", "trend over time / compare categories / relationship between two vars."),
        ("histogram", "the distribution (spread) of one numeric variable."),
        ("box plot", "median, quartiles and outliers — great for comparing groups' spread."),
        ("correlation heatmap", "colour-coded grid of how strongly variables relate."),
        ("legend", "the key that says which line/bar is which (needs label= on each plot)."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m5-test", "🧪 Module 5 Test — Build & Read a Chart")
    nb.md(
        "Given a small monthly dataset, make a bar chart **and** answer three analytical questions. "
        "Each variable is worth a point.\n\n"
        "> `show_hint('m5_test')` / `show_solution('m5_test')` available."
    )
    nb.practice(
        "m5_test",
        placeholder=(
            'data = pd.DataFrame({\n'
            '    "month": ["Jan", "Feb", "Mar", "Apr"],\n'
            '    "revenue": [200, 250, 180, 300],\n'
            '    "ad_spend": [20, 25, 18, 30],\n'
            '})\n'
            '\n'
            '# YOUR CODE HERE — draw a bar chart of month vs revenue with the EXACT title\n'
            '# "Revenue by Month", then fill the variables:\n'
            'test_chart_for_trend = None  # best chart type for revenue OVER TIME (a string)\n'
            'test_top_month = None        # the month with the highest revenue\n'
            'test_total_revenue = None    # total revenue across all months\n'
            'test_chart_title = None      # after building your chart: ax.get_title()'
        ),
        solution=(
            'data = pd.DataFrame({\n'
            '    "month": ["Jan", "Feb", "Mar", "Apr"],\n'
            '    "revenue": [200, 250, 180, 300],\n'
            '    "ad_spend": [20, 25, 18, 30],\n'
            '})\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.bar(data["month"], data["revenue"])\n'
            'ax.set_title("Revenue by Month")\n'
            'ax.set_xlabel("Month")\n'
            'ax.set_ylabel("Revenue")\n'
            'plt.show()\n'
            '\n'
            'test_chart_for_trend = "line"\n'
            'test_top_month = data.sort_values("revenue", ascending=False).iloc[0]["month"]\n'
            'test_total_revenue = data["revenue"].sum()\n'
            'test_chart_title = ax.get_title()'
        ),
        hint='Bar chart with ax.bar(data["month"], data["revenue"]) and '
             'ax.set_title("Revenue by Month"); trend over time = "line"; sort by revenue for the top '
             'month; .sum() for the total; test_chart_title = ax.get_title().',
        label="Module 5 test",
    )
    nb.check("m5_test_trend", user="test_chart_for_trend", expected="'line'",
             hint="For a value over time, a line chart is best.")
    nb.check("m5_test_top", user="test_top_month", expected="'Apr'",
             hint="April has the highest revenue (300).")
    nb.check("m5_test_total", user="test_total_revenue", expected="930",
             hint="200 + 250 + 180 + 300 = 930.")
    nb.check("m5_test_title", user="test_chart_title", expected="'Revenue by Month'",
             hint='Build the chart and set ax.set_title("Revenue by Month"), then '
                  'test_chart_title = ax.get_title().')
    nb.md(
        "🎉 **Module 5 done.** You can visualise trends, comparisons, distributions, relationships, "
        "and correlations — and, crucially, **choose the right chart**. Final stop: teaching the "
        "computer to *predict* — **scikit-learn**."
    )

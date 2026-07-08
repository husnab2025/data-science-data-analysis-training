"""
Capstone project — one guided case study combining every module.

Deterministic synthetic dataset (revenue == marketing * 10, messy region case)
so every answer is exactly gradeable. Steps: explore (Pandas) -> clean (Pandas) ->
aggregate (groupby) -> visualise (Matplotlib) -> summarise (NumPy) -> model (sklearn).
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    nb.module("capstone", "🏆 Capstone Project · MegaShop Sales Analysis")
    nb.md(
        "Time to be the analyst. **MegaShop** hands you a year of monthly data and three questions:\n\n"
        "1. Which region earns the most?\n"
        "2. Which month was best?\n"
        "3. Can we **predict** revenue from marketing spend?\n\n"
        "You'll answer all three by combining **everything**: Pandas cleaning & grouping, a "
        "Matplotlib chart, a NumPy summary, and a scikit-learn model. This is **guided** — each step "
        "has instructions and a hint — but the code is yours to write. Each step self-grades.\n\n"
        "> The dataset is generated below (no file needed). Run it, then work through the steps."
    )
    nb.code(
        '# The MegaShop dataset (given — just run this cell)\n'
        'sales = pd.DataFrame({\n'
        '    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",\n'
        '              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],\n'
        '    "region": ["North", "south", "NORTH", "South", "north", "SOUTH",\n'
        '               "North", "south", "North", "South", "north", "south"],\n'
        '    "marketing": [10, 12, 15, 14, 18, 20, 22, 19, 24, 26, 31, 28],\n'
        '    "revenue":   [100, 120, 150, 140, 180, 200, 220, 190, 240, 260, 310, 280],\n'
        '})\n'
        'print(sales)'
    )

    # ---- Step 1: Explore -------------------------------------------------
    nb.md(
        "### Step 1 — Explore (Pandas)\n"
        "How big is the data? Store the number of rows in `n_rows` and the number of columns in "
        "`n_cols`."
    )
    nb.practice(
        "cap_shape",
        placeholder=(
            'n_rows = None  # YOUR CODE HERE — how many rows?\n'
            'n_cols = None  # YOUR CODE HERE — how many columns?'
        ),
        solution=(
            'n_rows = len(sales)\n'
            'n_cols = sales.shape[1]'
        ),
        hint="len(sales) for rows; sales.shape[1] for columns.",
        label="capstone: explore",
    )
    nb.check("cap_shape", user="(n_rows, n_cols)", expected="(12, 4)",
             hint="12 months × 4 columns.")

    # ---- Step 2: Clean ---------------------------------------------------
    nb.md(
        "### Step 2 — Clean the `region` column (Pandas)\n"
        "The `region` values have inconsistent capitalisation (`North`, `north`, `NORTH`…). Clean the "
        "`sales[\"region\"]` column so all values are **stripped and lowercase**, then store the "
        "**sorted list of distinct regions** in `clean_regions`."
    )
    nb.practice(
        "cap_clean",
        placeholder=(
            '# YOUR CODE HERE — overwrite sales["region"] with a cleaned version, then:\n'
            'clean_regions = None  # sorted list of the distinct cleaned regions'
        ),
        solution=(
            'sales["region"] = sales["region"].str.strip().str.lower()\n'
            'clean_regions = sorted(sales["region"].unique().tolist())'
        ),
        hint='sales["region"] = sales["region"].str.strip().str.lower(); '
             'then sorted(sales["region"].unique().tolist()).',
        label="capstone: clean",
    )
    nb.check("cap_clean", user="clean_regions", expected="['north', 'south']",
             hint="After cleaning there are just two: north and south.")

    # ---- Step 3: Aggregate ----------------------------------------------
    nb.md(
        "### Step 3 — Revenue by region (Pandas groupby)\n"
        "Using the **cleaned** data, store total revenue per region as a dictionary in "
        "`region_revenue`, and the single top-earning region in `top_region`."
    )
    nb.practice(
        "cap_region",
        placeholder=(
            'region_revenue = None  # {region: total revenue} dict\n'
            'top_region = None      # the region with the highest total'
        ),
        solution=(
            'region_revenue = sales.groupby("region")["revenue"].sum().to_dict()\n'
            'top_region = sales.groupby("region")["revenue"].sum().idxmax()'
        ),
        hint='sales.groupby("region")["revenue"].sum(); then .to_dict() and .idxmax().',
        label="capstone: aggregate",
    )
    nb.check("cap_region", user="region_revenue",
             expected="{'north': 1200, 'south': 1190}",
             hint="North = 100+150+180+220+240+310 = 1200; South = 1190.")
    nb.check("cap_top", user="top_region", expected="'north'",
             hint="North (1200) edges out South (1190).")

    # ---- Step 4: Visualise ----------------------------------------------
    nb.md(
        "### Step 4 — Visualise revenue by month (Matplotlib)\n"
        "Draw a **bar chart** of `month` (x) vs `revenue` (y), with a title and axis labels. Then "
        "store the best-selling month in `best_month`."
    )
    nb.practice(
        "cap_viz",
        placeholder=(
            '# YOUR CODE HERE — a labelled bar chart of month vs revenue\n'
            '\n'
            'best_month = None  # the month with the highest revenue'
        ),
        solution=(
            'fig, ax = plt.subplots(figsize=(9, 4))\n'
            'ax.bar(sales["month"], sales["revenue"], color="teal")\n'
            'ax.set_title("MegaShop Revenue by Month")\n'
            'ax.set_xlabel("Month")\n'
            'ax.set_ylabel("Revenue ($)")\n'
            'plt.show()\n'
            '\n'
            'best_month = sales.sort_values("revenue", ascending=False).iloc[0]["month"]'
        ),
        hint='ax.bar(sales["month"], sales["revenue"]); best_month via sort_values(...).iloc[0].',
        label="capstone: visualise",
    )
    nb.check("cap_best", user="best_month", expected="'Nov'",
             hint="November has the tallest bar (310).")

    # ---- Step 5: NumPy summary ------------------------------------------
    nb.md(
        "### Step 5 — Summary statistics (NumPy)\n"
        "Convert the `revenue` column to a NumPy array with `.to_numpy()`. Store the **total** revenue "
        "in `total_revenue` and the **average** monthly revenue (rounded to 1 dp) in `avg_revenue`."
    )
    nb.practice(
        "cap_summary",
        placeholder=(
            'revenue_array = None   # sales["revenue"].to_numpy()\n'
            'total_revenue = None   # the sum (as an int)\n'
            'avg_revenue = None     # the mean, rounded to 1 decimal place'
        ),
        solution=(
            'revenue_array = sales["revenue"].to_numpy()\n'
            'total_revenue = int(revenue_array.sum())\n'
            'avg_revenue = round(float(revenue_array.mean()), 1)'
        ),
        hint="sales['revenue'].to_numpy(); int(arr.sum()); round(float(arr.mean()), 1).",
        label="capstone: summary",
    )
    nb.check("cap_total", user="total_revenue", expected="2390",
             hint="All twelve months sum to 2390.")
    nb.check("cap_avg", user="avg_revenue", expected="round(2390 / 12, 1)",
             hint="2390 ÷ 12 ≈ 199.2.")

    # ---- Step 6: Model ---------------------------------------------------
    nb.md(
        "### Step 6 — Predict revenue from marketing (scikit-learn)\n"
        "Fit a `LinearRegression` with **marketing** as the feature and **revenue** as the target "
        "(hint: `X = sales[[\"marketing\"]].to_numpy()`, `y = sales[\"revenue\"]`). Store the learned "
        "slope (rounded to 1 dp) in `model_slope`, and the predicted revenue for a marketing spend of "
        "`40` (rounded to 1 dp) in `pred_40`."
    )
    nb.practice(
        "cap_model",
        placeholder=(
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            '# YOUR CODE HERE — build X and y, do a train/test split, fit on the training set, then:\n'
            'model_slope = None  # round(model.coef_[0], 1)\n'
            'pred_40 = None      # round(model.predict([[40]])[0], 1)'
        ),
        solution=(
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = sales[["marketing"]].to_numpy()\n'
            'y = sales["revenue"].to_numpy()\n'
            'X_train, X_test, y_train, y_test = train_test_split(\n'
            '    X, y, test_size=0.25, random_state=42)\n'
            'model = LinearRegression().fit(X_train, y_train)\n'
            'model_slope = round(model.coef_[0], 1)\n'
            'pred_40 = round(model.predict([[40]])[0], 1)'
        ),
        hint="Split with train_test_split(X, y, test_size=0.25, random_state=42); fit on X_train, "
             "y_train; then round(model.coef_[0], 1) and round(model.predict([[40]])[0], 1).",
        label="capstone: model",
    )
    nb.check("cap_slope", user="model_slope", expected="10.0",
             hint="Revenue is exactly 10× marketing, so the slope is 10.0.")
    nb.check("cap_pred", user="pred_40", expected="400.0",
             hint="At marketing = 40: 10 × 40 = 400.")
    nb.gotcha(
        "Notice the model came out **suspiciously perfect** (slope exactly 10, R² ≈ 1.0). That's only "
        "because this teaching data was built to be flawless. **Real** marketing-vs-revenue data would "
        "be scattered — a realistic R² of 0.6–0.8 is genuinely *good*. In the real world, a perfect "
        "score is a red flag to investigate, not a trophy to celebrate."
    )

    nb.md(
        "### 🏁 Capstone complete!\n"
        "You just ran a full analysis end-to-end: explored, cleaned, aggregated, visualised, "
        "summarised, and **modelled** — the exact workflow of a real data analyst. MegaShop's answers: "
        "**North** earns most, **November** was the best month, and revenue is a clean **10×** of "
        "marketing spend. 👏\n\n"
        "Run the **📈 Final Report** next to see your overall score."
    )

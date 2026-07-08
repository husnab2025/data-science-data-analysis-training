"""
Module 3 — Pandas (the heart of data analysis).

Series vs DataFrame · reading data (dict & CSV via in-memory string) ·
inspecting · .loc/.iloc · filtering · sorting · deriving columns ·
groupby + aggregation · missing values · cleaning messy data · merging ·
Module 3 test.

Design note: every self-check compares a PLAIN value (int/float/list/dict) that
the learner stores into a variable. Placeholders set those variables to None, so
the check cells never dereference a None DataFrame and always run cleanly.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_series_df(nb)
    _lesson_read(nb)
    _lesson_inspect(nb)
    _lesson_select(nb)
    _lesson_filter(nb)
    _lesson_sort(nb)
    _lesson_derive(nb)
    _lesson_groupby(nb)
    _lesson_missing(nb)
    _lesson_clean(nb)
    _lesson_merge(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod3", "Module 3 · Pandas")
    nb.md(
        "This is the module that turns you into an analyst. **Pandas** is the library every data "
        "professional lives in — it gives you the **DataFrame**, a spreadsheet-like table you can "
        "filter, sort, group, clean, and combine with a few lines of code.\n\n"
        "**Why it matters for the job:** 80% of real analytics work is *wrangling* data — loading it, "
        "cleaning the mess, slicing it the way stakeholders ask, and summarising it. Excel breaks "
        "down at scale and isn't reproducible; Pandas handles millions of rows and every step is "
        "written down as code you can re-run.\n\n"
        "**The mental bridge:** remember Module 2? A DataFrame is basically a collection of those "
        "dictionaries (one per row) lined up into a table, with turbo-charged tools bolted on. "
        "Everything you learned about keys, loops, and comprehensions pays off here."
    )
    nb.role_note(
        "Pandas is the **home turf of the Data Analyst** — most analyst work is Pandas (or its SQL "
        "equivalent). Data Scientists use all of it too, then push further into modelling (Module 6). "
        "If you master one module in this notebook, make it this one."
    )


# --------------------------------------------------------------------------- #
def _lesson_series_df(nb: NB):
    nb.lesson("m3-series", "Lesson 3.1 — Series vs DataFrame")
    nb.md(
        "**What they are.**\n"
        "- A **Series** is a single labelled column of data (like one list with an index).\n"
        "- A **DataFrame** is a whole table — many Series sharing one index. Each **column** is a "
        "Series.\n\n"
        "**Why it exists.** Raw Python lists don't know their own column names, can't align by index, "
        "and have no built-in filtering/grouping. Series/DataFrame add all of that.\n\n"
        "**Real-world analogy.** A DataFrame is a spreadsheet tab; a Series is a single column in it.\n\n"
        "**On the job.** You'll create DataFrames from Python dictionaries constantly — every quick "
        "'let me just tabulate this' moment starts with `pd.DataFrame({...})`."
    )
    nb.md("**Worked example:**")
    nb.code(
        's = pd.Series([10, 20, 30], name="sales")   # one labelled column\n'
        'print(s)\n'
        '\n'
        'df = pd.DataFrame({                          # a table from a dict of columns\n'
        '    "product": ["A", "B", "C"],\n'
        '    "price": [10, 20, 30],\n'
        '    "qty": [100, 50, 75],\n'
        '})\n'
        'print(df)\n'
        'print(type(s).__name__, "|", type(df).__name__)   # Series | DataFrame'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Build a DataFrame `store` from a dictionary with columns `city` = `[\"NY\", \"LA\"]` and "
        "`revenue` = `[500, 300]`. Then store the **row count** in `n_rows` and the **total revenue** "
        "in `total_revenue`."
    )
    nb.practice(
        "m3_create",
        placeholder=(
            'store = None          # YOUR CODE HERE — pd.DataFrame({...})\n'
            'n_rows = None         # YOUR CODE HERE — how many rows? (len)\n'
            'total_revenue = None  # YOUR CODE HERE — sum of the revenue column'
        ),
        solution=(
            'store = pd.DataFrame({"city": ["NY", "LA"], "revenue": [500, 300]})\n'
            'n_rows = len(store)\n'
            'total_revenue = store["revenue"].sum()'
        ),
        hint='pd.DataFrame({"city": [...], "revenue": [...]}); len(store); store["revenue"].sum().',
        label="build a DataFrame",
    )
    nb.check("m3_create", user="(n_rows, total_revenue)", expected="(2, 800)",
             hint="Two rows, and 500 + 300 = 800.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** A single column of a DataFrame is a…?\n\n"
        "- **A)** Series\n- **B)** DataFrame\n- **C)** list\n"
    )
    nb.practice("m3_q_series", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'",
                hint="It's the one-dimensional labelled structure.", label="quiz: Series")
    nb.mcq("m3_q_series", user="answer", correct="A",
           explanation="Each DataFrame column is a Series.", hint="One column = one Series.")


# --------------------------------------------------------------------------- #
def _lesson_read(nb: NB):
    nb.lesson("m3-read", "Lesson 3.2 — Reading Data (CSV, kept self-contained)")
    nb.md(
        "**What it is.** The everyday way to load data is `pd.read_csv(\"file.csv\")`. Because this "
        "notebook must run anywhere with **no attached files**, we read from an **in-memory string** "
        "with `io.StringIO(...)` — the *exact same* `read_csv` function, just pointed at text instead "
        "of a file on disk.\n\n"
        "**Why it exists.** CSV ('comma-separated values') is the universal data-exchange format. "
        "`read_csv` turns that raw text into a tidy DataFrame in one call, inferring columns and types.\n\n"
        "**Real-world analogy.** Importing a `.csv` export from your sales system into a spreadsheet — "
        "except reproducible and scriptable.\n\n"
        "**On the job.** Day one, someone hands you a CSV. `pd.read_csv` is how the analysis begins. "
        "(In Colab you'd upload the file or read from a URL; the function is identical.)"
    )
    nb.md("**Worked example** — read a CSV that lives in a string:")
    nb.code(
        'import io\n'
        'csv_text = """product,price,qty\n'
        'Pen,2,100\n'
        'Book,5,40\n'
        'Bag,20,10"""\n'
        '\n'
        'df = pd.read_csv(io.StringIO(csv_text))   # same call you\'d use on a real file\n'
        'print(df)\n'
        'print("shape:", df.shape)'
    )
    nb.realjob(
        "**A caveat worth reading twice.** We load CSVs from a **text string** via `io.StringIO(...)` "
        "for one reason only: so this notebook is 100% self-contained and needs *no downloaded files*. "
        "In a real job you'd almost never do that — instead you'd write "
        "`df = pd.read_csv(\"sales.csv\")` (a file on your computer), or "
        "`pd.read_csv(\"https://.../sales.csv\")` (a web link), or pull from a database with SQL. The "
        "`pd.read_csv` function is **identical** — only the thing inside the brackets changes. So "
        "everything you practise here transfers directly; just picture a real filename where you see "
        "`io.StringIO`."
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Read the CSV in `csv_text` into `sales_df`, then store the **sum of the `orders` column** in "
        "`total_orders`."
    )
    nb.practice(
        "m3_read",
        placeholder=(
            'import io\n'
            'csv_text = """city,orders\n'
            'NY,120\n'
            'LA,90\n'
            'SF,60"""\n'
            '\n'
            'sales_df = None      # YOUR CODE HERE — pd.read_csv(io.StringIO(csv_text))\n'
            'total_orders = None  # YOUR CODE HERE — sum of the orders column'
        ),
        solution=(
            'import io\n'
            'csv_text = """city,orders\n'
            'NY,120\n'
            'LA,90\n'
            'SF,60"""\n'
            '\n'
            'sales_df = pd.read_csv(io.StringIO(csv_text))\n'
            'total_orders = sales_df["orders"].sum()'
        ),
        hint='pd.read_csv(io.StringIO(csv_text)); then sales_df["orders"].sum().',
        label="read_csv",
    )
    nb.check("m3_read", user="total_orders", expected="270",
             hint="120 + 90 + 60 = 270.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** `pd.read_csv` expects data that is…?\n\n"
        "- **A)** comma-separated text\n- **B)** a Python dictionary\n- **C)** an Excel formula\n"
    )
    nb.practice("m3_q_read", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="CSV = Comma-Separated Values.", label="quiz: read_csv")
    nb.mcq("m3_q_read", user="answer", correct="A",
           explanation="CSV means comma-separated values — plain text.", hint="What does CSV stand for?")


# --------------------------------------------------------------------------- #
def _lesson_inspect(nb: NB):
    nb.lesson("m3-inspect", "Lesson 3.3 — Inspecting a DataFrame")
    nb.md(
        "**What it is.** Before analysing, you *look*: how big is it, what are the columns, what do "
        "the first rows look like?\n\n"
        "- `df.shape` → `(rows, columns)`\n"
        "- `df.columns` → the column names\n"
        "- `df.head(n)` → the first `n` rows; `df.tail(n)` → the last\n"
        "- `df.dtypes` → the type of each column\n"
        "- `df.describe()` → quick stats (count, mean, min, max…) for numeric columns\n\n"
        "**Why it exists.** You can't trust data you haven't looked at. These are your first five "
        "moves on *any* new dataset.\n\n"
        "**Real-world analogy.** Flipping through the first pages of a report and checking the table "
        "of contents before diving in.\n\n"
        "**On the job.** The instant you load data, you run `df.head()` and `df.shape` to sanity-check "
        "that it loaded correctly and matches what the stakeholder described."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"product": ["Pen", "Book", "Bag"],\n'
        '                   "price": [2, 5, 20], "qty": [100, 40, 10]})\n'
        'print("shape  :", df.shape)\n'
        'print("columns:", list(df.columns))\n'
        'print(df.head(2))\n'
        'print(df.describe())'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "The DataFrame `df` is already built for you. Store its **shape** in `shape_tuple` and the "
        "**list of column names** in `cols`."
    )
    nb.practice(
        "m3_inspect",
        placeholder=(
            'df = pd.DataFrame({"product": ["Pen", "Book", "Bag"],\n'
            '                   "price": [2, 5, 20], "qty": [100, 40, 10]})\n'
            '\n'
            'shape_tuple = None  # YOUR CODE HERE — df.shape\n'
            'cols = None         # YOUR CODE HERE — list of column names'
        ),
        solution=(
            'df = pd.DataFrame({"product": ["Pen", "Book", "Bag"],\n'
            '                   "price": [2, 5, 20], "qty": [100, 40, 10]})\n'
            '\n'
            'shape_tuple = df.shape\n'
            'cols = list(df.columns)'
        ),
        hint="df.shape gives (rows, cols); list(df.columns) gives the names.",
        label="inspect shape & columns",
    )
    nb.check("m3_inspect", user="(shape_tuple, cols)",
             expected="((3, 3), ['product', 'price', 'qty'])",
             hint="3 rows × 3 columns, named product, price, qty.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** `df.shape` returns…?\n\n"
        "- **A)** just the number of rows\n- **B)** a `(rows, columns)` tuple\n- **C)** the column names\n"
    )
    nb.practice("m3_q_inspect", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="It's two numbers.", label="quiz: shape")
    nb.mcq("m3_q_inspect", user="answer", correct="B",
           explanation="`.shape` is a (rows, columns) tuple.", hint="Rows and columns together.")


# --------------------------------------------------------------------------- #
def _lesson_select(nb: NB):
    nb.lesson("m3-select", "Lesson 3.4 — Selecting with .loc and .iloc")
    nb.md(
        "**What it is.** Two precise ways to grab rows/columns:\n\n"
        "- `df[\"col\"]` → one column (a Series).\n"
        "- `df.loc[row_label, \"col\"]` → select by **label** (the index value / column name).\n"
        "- `df.iloc[row_pos, col_pos]` → select by **integer position** (0-based, like a list).\n\n"
        "With the default index (0, 1, 2…) label and position look the same, but they diverge the "
        "moment you sort or set a custom index — so the distinction matters.\n\n"
        "**Why it exists.** You constantly need 'the value in this row and column' or 'these specific "
        "rows'. `.loc`/`.iloc` make that unambiguous.\n\n"
        "**Real-world analogy.** `.loc` is asking for the row *named* 'Order #1005'; `.iloc` is asking "
        "for 'the 3rd row from the top' regardless of its name.\n\n"
        "**On the job.** `.iloc[0]` to peek at the first record; `.loc[mask, 'revenue']` to read a "
        "specific column for filtered rows."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"name": ["Ana", "Ben", "Cara"],\n'
        '                   "age": [25, 30, 35], "city": ["NY", "LA", "SF"]})\n'
        '\n'
        'print("df[\'age\'] column:\\n", df["age"], sep="")\n'
        'print("loc[0, name]  :", df.loc[0, "name"])    # by label\n'
        'print("iloc[2][age]  :", df.iloc[2]["age"])    # by position\n'
        'print("first row     :\\n", df.iloc[0], sep="")'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Using `df` below, store: the name in the **first** row (`first_name`), the age in the "
        "**third** row (`third_age`), and the whole `city` column as a list (`cities`)."
    )
    nb.practice(
        "m3_select",
        placeholder=(
            'df = pd.DataFrame({"name": ["Ana", "Ben", "Cara"],\n'
            '                   "age": [25, 30, 35], "city": ["NY", "LA", "SF"]})\n'
            '\n'
            'first_name = None  # YOUR CODE HERE — name in row 0\n'
            'third_age = None   # YOUR CODE HERE — age in row 2\n'
            'cities = None      # YOUR CODE HERE — the city column as a list'
        ),
        solution=(
            'df = pd.DataFrame({"name": ["Ana", "Ben", "Cara"],\n'
            '                   "age": [25, 30, 35], "city": ["NY", "LA", "SF"]})\n'
            '\n'
            'first_name = df.loc[0, "name"]\n'
            'third_age = df.iloc[2]["age"]\n'
            'cities = df["city"].tolist()'
        ),
        hint='df.loc[0, "name"]; df.iloc[2]["age"]; df["city"].tolist().',
        label=".loc / .iloc",
    )
    nb.check("m3_select", user="(first_name, third_age, cities)",
             expected="('Ana', 35, ['NY', 'LA', 'SF'])",
             hint="Ana is first; the third age is 35; cities are NY, LA, SF.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** `.loc` selects by ___ and `.iloc` selects by ___.\n\n"
        "- **A)** position; label\n- **B)** label; position\n- **C)** both by position\n"
    )
    nb.practice("m3_q_select", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="The 'i' in iloc stands for integer position.",
                label="quiz: loc vs iloc")
    nb.mcq("m3_q_select", user="answer", correct="B",
           explanation="`.loc` = labels, `.iloc` = integer positions.", hint="iloc → integer.")


# --------------------------------------------------------------------------- #
def _lesson_filter(nb: NB):
    nb.lesson("m3-filter", "Lesson 3.5 — Filtering Rows (boolean masks)")
    nb.md(
        "**What it is.** You keep the rows that meet a condition by putting a **boolean mask** inside "
        "`df[...]`:\n\n"
        "```python\n"
        'df[df["amount"] >= 100]                       # rows where amount >= 100\n'
        'df[(df["amount"] >= 100) & (df["region"] == "N")]   # AND: note & and parentheses\n'
        "```\n\n"
        "`df[\"amount\"] >= 100` produces a Series of `True`/`False`; `df[mask]` keeps the `True` rows. "
        "Combine conditions with `&` (and) and `|` (or) — **each condition in parentheses**.\n\n"
        "**Why it exists.** 'Show me only the big orders / the North region / last month' is the most "
        "common analytical request there is.\n\n"
        "**Real-world analogy.** The filter dropdown in a spreadsheet — but exact and repeatable.\n\n"
        "**On the job.** Filtering is step one of nearly every analysis: narrow to the relevant slice, "
        "then summarise it."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({\n'
        '    "customer": ["Ana", "Ben", "Cara", "Dan", "Eve"],\n'
        '    "amount": [120, 45, 300, 80, 210],\n'
        '    "region": ["N", "S", "N", "S", "N"],\n'
        '})\n'
        '\n'
        'big = df[df["amount"] >= 100]                 # single condition\n'
        'print(big)\n'
        'big_north = df[(df["amount"] >= 100) & (df["region"] == "N")]   # combined\n'
        'print(big_north)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "From `df`, store the **list of customers** whose amount is **≥ 100** in `big_customers`, and "
        "the **total amount** for region `\"N\"` in `north_total`."
    )
    nb.practice(
        "m3_filter",
        placeholder=(
            'df = pd.DataFrame({\n'
            '    "customer": ["Ana", "Ben", "Cara", "Dan", "Eve"],\n'
            '    "amount": [120, 45, 300, 80, 210],\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '})\n'
            '\n'
            'big_customers = None  # YOUR CODE HERE — list of customers with amount >= 100\n'
            'north_total = None    # YOUR CODE HERE — total amount where region == "N"'
        ),
        solution=(
            'df = pd.DataFrame({\n'
            '    "customer": ["Ana", "Ben", "Cara", "Dan", "Eve"],\n'
            '    "amount": [120, 45, 300, 80, 210],\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '})\n'
            '\n'
            'big_customers = df[df["amount"] >= 100]["customer"].tolist()\n'
            'north_total = df[df["region"] == "N"]["amount"].sum()'
        ),
        hint='Mask then select: df[df["amount"] >= 100]["customer"].tolist(); '
             'df[df["region"] == "N"]["amount"].sum().',
        label="filter rows",
    )
    nb.check("m3_filter", user="(big_customers, north_total)",
             expected="(['Ana', 'Cara', 'Eve'], 630)",
             hint="Ana, Cara, Eve clear 100; North amounts 120+300+210 = 630.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** To keep rows where `amount > 100` **AND** `region == \"N\"`, the correct syntax is:\n\n"
        '- **A)** `df[df.amount > 100 and df.region == "N"]`\n'
        '- **B)** `df[(df.amount > 100) & (df.region == "N")]`\n'
        '- **C)** `df[df.amount > 100, df.region == "N"]`\n'
    )
    nb.practice("m3_q_filter", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'",
                hint="Use & with each condition wrapped in parentheses (plain `and` fails on Series).",
                label="quiz: combined filter")
    nb.mcq("m3_q_filter", user="answer", correct="B",
           explanation="Element-wise AND uses `&`, and each condition needs parentheses.",
           hint="`and` doesn't work element-wise on Series.")
    nb.gotcha(
        "When combining filter conditions, you must use `&` (and) / `|` (or) — **not** the plain words "
        "`and` / `or` — and wrap **each condition in parentheses**: "
        "`df[(df[\"a\"] > 1) & (df[\"b\"] < 5)]`. Forgetting the parentheses, or using `and`, is one of "
        "the most common Pandas errors you'll ever hit."
    )


# --------------------------------------------------------------------------- #
def _lesson_sort(nb: NB):
    nb.lesson("m3-sort", "Lesson 3.6 — Sorting")
    nb.md(
        "**What it is.** `df.sort_values(\"col\")` reorders rows by a column — ascending by default, "
        "`ascending=False` for descending.\n\n"
        "**Why it exists.** Ranking is everywhere: top products, worst-performing regions, most recent "
        "orders.\n\n"
        "**Real-world analogy.** Clicking a spreadsheet column header to sort — but you can chain it "
        "with everything else.\n\n"
        "**On the job.** `sort_values(..., ascending=False).head(10)` is the classic 'give me the top "
        "10' one-liner."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"product": ["A", "B", "C", "D"], "sales": [300, 150, 500, 250]})\n'
        '\n'
        'print(df.sort_values("sales"))                    # ascending\n'
        'print(df.sort_values("sales", ascending=False))   # descending (top first)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Store the product with the **highest** sales in `top_product`, and the `sales` column sorted "
        "**ascending** as a list in `sorted_sales`."
    )
    nb.practice(
        "m3_sort",
        placeholder=(
            'df = pd.DataFrame({"product": ["A", "B", "C", "D"], "sales": [300, 150, 500, 250]})\n'
            '\n'
            'top_product = None    # YOUR CODE HERE — product with the highest sales\n'
            'sorted_sales = None   # YOUR CODE HERE — the sales values, ascending, as a list'
        ),
        solution=(
            'df = pd.DataFrame({"product": ["A", "B", "C", "D"], "sales": [300, 150, 500, 250]})\n'
            '\n'
            'top_product = df.sort_values("sales", ascending=False).iloc[0]["product"]\n'
            'sorted_sales = df.sort_values("sales")["sales"].tolist()'
        ),
        hint='Sort descending then take .iloc[0]["product"]; sort ascending then ["sales"].tolist().',
        label="sort_values",
    )
    nb.check("m3_sort", user="(top_product, sorted_sales)",
             expected="('C', [150, 250, 300, 500])",
             hint="C has the most (500); ascending order is 150, 250, 300, 500.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q6.** By default, `sort_values` sorts in which order?\n\n"
        "- **A)** descending\n- **B)** ascending\n- **C)** random\n"
    )
    nb.practice("m3_q_sort", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="Smallest first, unless you say otherwise.",
                label="quiz: sort order")
    nb.mcq("m3_q_sort", user="answer", correct="B",
           explanation="Ascending is the default; pass ascending=False to flip it.",
           hint="Smallest to largest by default.")


# --------------------------------------------------------------------------- #
def _lesson_derive(nb: NB):
    nb.lesson("m3-derive", "Lesson 3.7 — Creating New Columns")
    nb.md(
        "**What it is.** Assign to a new column name and Pandas computes it **row-by-row** "
        "(vectorised — no loop needed):\n\n"
        "```python\n"
        'df["revenue"] = df["price"] * df["qty"]\n'
        "```\n\n"
        "**Why it exists.** Analysis is mostly *deriving* new facts from raw columns — revenue from "
        "price×qty, profit margin, flags like 'is_high_value'.\n\n"
        "**Real-world analogy.** A spreadsheet formula column — but applied to the whole column at "
        "once, instantly.\n\n"
        "**On the job.** Nearly every dataset needs derived metrics before it can answer the real "
        "business question."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"product": ["A", "B", "C"], "price": [10, 20, 30], "qty": [5, 3, 2]})\n'
        '\n'
        'df["revenue"] = df["price"] * df["qty"]      # vectorised, row-by-row\n'
        'df["pricey"] = df["price"] > 15              # a boolean flag column\n'
        'print(df)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Add a `revenue` column (`price * qty`). Then store its values as a list in `rev_list` and "
        "the grand total in `total_revenue`."
    )
    nb.practice(
        "m3_derive",
        placeholder=(
            'df = pd.DataFrame({"product": ["A", "B", "C"], "price": [10, 20, 30], "qty": [5, 3, 2]})\n'
            '\n'
            '# YOUR CODE HERE — add a "revenue" column = price * qty, then fill the two variables\n'
            'rev_list = None       # the revenue values as a list\n'
            'total_revenue = None  # the sum of revenue'
        ),
        solution=(
            'df = pd.DataFrame({"product": ["A", "B", "C"], "price": [10, 20, 30], "qty": [5, 3, 2]})\n'
            '\n'
            'df["revenue"] = df["price"] * df["qty"]\n'
            'rev_list = df["revenue"].tolist()\n'
            'total_revenue = df["revenue"].sum()'
        ),
        hint='df["revenue"] = df["price"] * df["qty"]; then .tolist() and .sum().',
        label="derive a column",
    )
    nb.check("m3_derive", user="(rev_list, total_revenue)",
             expected="([50, 60, 60], 170)",
             hint="10*5=50, 20*3=60, 30*2=60 → total 170.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q7.** `df[\"c\"] = df[\"a\"] * df[\"b\"]` does what?\n\n"
        "- **A)** multiplies the two columns row-by-row into a new column `c`\n"
        "- **B)** raises an error\n- **C)** multiplies only the first row\n"
    )
    nb.practice("m3_q_derive", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Column math is vectorised across every row.",
                label="quiz: vectorised column")
    nb.mcq("m3_q_derive", user="answer", correct="A",
           explanation="Operations on columns apply to every row at once.", hint="It's element-wise.")


# --------------------------------------------------------------------------- #
def _lesson_groupby(nb: NB):
    nb.lesson("m3-groupby", "Lesson 3.8 — GroupBy & Aggregation")
    nb.md(
        "**What it is.** `groupby` implements **split → apply → combine**: split rows into groups, "
        "apply an aggregation (sum, mean, count…), combine into a summary.\n\n"
        "```python\n"
        'df.groupby("region")["sales"].sum()   # total sales per region\n'
        "```\n\n"
        "**Why it exists.** This is the single most-requested analysis pattern: *totals/averages by "
        "category*.\n\n"
        "**Real-world analogy.** Sorting a pile of receipts into labelled envelopes (one per region), "
        "then adding up each envelope.\n\n"
        "**On the job.** When your manager says *“What are total sales by region?”* or *“average order "
        "value per customer?”*, this is the answer — and it's the beating heart of dashboards and "
        "reports."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({\n'
        '    "region": ["N", "S", "N", "S", "N"],\n'
        '    "product": ["A", "A", "B", "B", "A"],\n'
        '    "sales": [100, 200, 150, 50, 120],\n'
        '})\n'
        '\n'
        'print(df.groupby("region")["sales"].sum())    # total per region\n'
        'print(df.groupby("region")["sales"].mean())   # average per region\n'
        'print(df.groupby("product")["sales"].count())  # how many rows per product'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Store total sales **per region** as a dictionary in `region_totals` "
        "(hint: `...sum().to_dict()`), and the single region with the highest total in `top_region` "
        "(hint: `...sum().idxmax()`)."
    )
    nb.practice(
        "m3_groupby",
        placeholder=(
            'df = pd.DataFrame({\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '    "product": ["A", "A", "B", "B", "A"],\n'
            '    "sales": [100, 200, 150, 50, 120],\n'
            '})\n'
            '\n'
            'region_totals = None  # YOUR CODE HERE — {region: total sales} dict\n'
            'top_region = None     # YOUR CODE HERE — region with the highest total'
        ),
        solution=(
            'df = pd.DataFrame({\n'
            '    "region": ["N", "S", "N", "S", "N"],\n'
            '    "product": ["A", "A", "B", "B", "A"],\n'
            '    "sales": [100, 200, 150, 50, 120],\n'
            '})\n'
            '\n'
            'region_totals = df.groupby("region")["sales"].sum().to_dict()\n'
            'top_region = df.groupby("region")["sales"].sum().idxmax()'
        ),
        hint='df.groupby("region")["sales"].sum() then .to_dict() / .idxmax().',
        label="groupby + aggregate",
    )
    nb.check("m3_groupby", user="(region_totals, top_region)",
             expected="({'N': 370, 'S': 250}, 'N')",
             hint="North = 100+150+120 = 370; South = 200+50 = 250; North wins.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q8.** `df.groupby(\"region\")[\"sales\"].sum()` returns…?\n\n"
        "- **A)** total sales per region\n- **B)** total sales overall\n- **C)** the sales sorted\n"
    )
    nb.practice("m3_q_groupby", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Group first, then sum within each group.",
                label="quiz: groupby")
    nb.mcq("m3_q_groupby", user="answer", correct="A",
           explanation="It sums sales within each region separately.", hint="One total per group.")


# --------------------------------------------------------------------------- #
def _lesson_missing(nb: NB):
    nb.lesson("m3-missing", "Lesson 3.9 — Handling Missing Values")
    nb.md(
        "**What it is.** Real data has holes — shown as `NaN` ('Not a Number'). Your tools:\n\n"
        "- `df.isna()` → `True`/`False` per cell; `df[\"c\"].isna().sum()` counts missing.\n"
        "- `df.dropna()` → drop rows containing any `NaN`.\n"
        "- `df[\"c\"].fillna(value)` → replace `NaN` with something (0, the mean, 'Unknown'…).\n\n"
        "**Why it exists.** Missing data is inevitable, and most calculations choke on it. You must "
        "decide, deliberately, whether to **drop** or **fill**.\n\n"
        "**Real-world analogy.** A survey where some people skipped questions — do you exclude those "
        "responses, or fill blanks with a sensible default?\n\n"
        "**On the job.** Deciding drop-vs-fill is a judgement call that affects your results, so "
        "you'll do it consciously on nearly every dataset — and be ready to explain your choice."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"name": ["A", "B", "C", "D"], "score": [10, None, 30, None]})\n'
        '\n'
        'print("missing scores:", df["score"].isna().sum())   # 2\n'
        'print("after dropna:\\n", df.dropna(), sep="")\n'
        'print("after fillna(0):\\n", df["score"].fillna(0), sep="")'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "For `df` below, store: the count of missing scores (`n_missing`), the number of rows left "
        "after `dropna()` (`rows_after_drop`), and the `score` column with `NaN` replaced by `0` as a "
        "list (`filled_list`)."
    )
    nb.practice(
        "m3_missing",
        placeholder=(
            'df = pd.DataFrame({"name": ["A", "B", "C", "D"], "score": [10, None, 30, None]})\n'
            '\n'
            'n_missing = None        # YOUR CODE HERE — how many scores are missing\n'
            'rows_after_drop = None  # YOUR CODE HERE — row count after dropping NaN rows\n'
            'filled_list = None      # YOUR CODE HERE — score column, NaN->0, as a list'
        ),
        solution=(
            'df = pd.DataFrame({"name": ["A", "B", "C", "D"], "score": [10, None, 30, None]})\n'
            '\n'
            'n_missing = df["score"].isna().sum()\n'
            'rows_after_drop = len(df.dropna())\n'
            'filled_list = df["score"].fillna(0).tolist()'
        ),
        hint='df["score"].isna().sum(); len(df.dropna()); df["score"].fillna(0).tolist().',
        label="missing values",
    )
    nb.check("m3_missing", user="(n_missing, rows_after_drop, filled_list)",
             expected="(2, 2, [10.0, 0.0, 30.0, 0.0])",
             hint="Two scores are missing; two rows survive dropna; blanks become 0.0.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q9.** `df.dropna()` does what?\n\n"
        "- **A)** fills missing values with 0\n- **B)** removes rows that contain any missing value\n"
        "- **C)** ignores missing values silently\n"
    )
    nb.practice("m3_q_missing", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="'drop' + 'na' = drop the NA rows.",
                label="quiz: dropna")
    nb.mcq("m3_q_missing", user="answer", correct="B",
           explanation="dropna removes rows with NaN; fillna is the one that fills.",
           hint="The name is literal.")


# --------------------------------------------------------------------------- #
def _lesson_clean(nb: NB):
    nb.lesson("m3-clean", "Lesson 3.10 — Cleaning Messy, Inconsistent Data")
    nb.md(
        "**What it is.** Real text data is inconsistent: stray spaces, mixed capitalisation, numbers "
        "stored as text, duplicates. Your cleanup toolkit:\n\n"
        "- `df[\"c\"].str.strip()` → remove leading/trailing spaces.\n"
        "- `df[\"c\"].str.lower()` (or `.str.upper()`) → standardise case.\n"
        "- `df[\"c\"].astype(int)` → convert a column's type (text → number).\n"
        "- `df[\"c\"].unique()` → the distinct values; `df.drop_duplicates()` → remove repeat rows.\n\n"
        "**Why it exists.** `\" NY \"`, `\"ny\"` and `\"NY\"` look the same to a human but are three "
        "*different* values to a computer — they'd split your groupby into three fake groups. Cleaning "
        "makes them one.\n\n"
        "**Real-world analogy.** Tidying a contact list where the same city is typed five different "
        "ways before you can count anything reliably.\n\n"
        "**On the job.** This is the unglamorous 80% of the work — and getting it right is what "
        "separates a trustworthy analysis from a misleading one."
    )
    nb.md("**Worked example:**")
    nb.code(
        'df = pd.DataFrame({"city": [" NY ", "ny", "LA"], "sales": ["100", "200", "150"]})\n'
        '\n'
        'df["city"] = df["city"].str.strip().str.lower()   # " NY " and "ny" -> "ny"\n'
        'df["sales"] = df["sales"].astype(int)             # text -> integer\n'
        'print(df)\n'
        'print("distinct cities:", df["city"].unique().tolist())'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Clean the `city` column (strip spaces **and** lowercase), convert `sales` to integers, then "
        "store the **sorted list of distinct cities** in `unique_cities` and the **total sales** in "
        "`total_sales`."
    )
    nb.practice(
        "m3_clean",
        placeholder=(
            'df = pd.DataFrame({"city": [" ny ", "LA", "ny", "Sf ", "la"],\n'
            '                   "sales": ["100", "200", "150", "50", "300"]})\n'
            '\n'
            '# YOUR CODE HERE — clean df["city"] and df["sales"], then fill the two variables\n'
            'unique_cities = None  # sorted list of distinct cleaned cities\n'
            'total_sales = None    # sum of sales as integers'
        ),
        solution=(
            'df = pd.DataFrame({"city": [" ny ", "LA", "ny", "Sf ", "la"],\n'
            '                   "sales": ["100", "200", "150", "50", "300"]})\n'
            '\n'
            'df["city"] = df["city"].str.strip().str.lower()\n'
            'df["sales"] = df["sales"].astype(int)\n'
            'unique_cities = sorted(df["city"].unique().tolist())\n'
            'total_sales = df["sales"].sum()'
        ),
        hint='.str.strip().str.lower() on city; .astype(int) on sales; sorted(...unique().tolist()).',
        label="clean messy data",
    )
    nb.check("m3_clean", user="(unique_cities, total_sales)",
             expected="(['la', 'ny', 'sf'], 800)",
             hint="After cleaning there are 3 cities (la, ny, sf) and sales total 800.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q10.** To make `\" NY \"` and `\"ny\"` count as the same value, you'd use…?\n\n"
        "- **A)** `.str.strip().str.lower()`\n- **B)** `.astype(int)`\n- **C)** `.dropna()`\n"
    )
    nb.practice("m3_q_clean", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="You need to remove spaces and unify the case.",
                label="quiz: cleaning")
    nb.mcq("m3_q_clean", user="answer", correct="A",
           explanation="strip() removes spaces, lower() unifies case.", hint="Spaces + capitalisation.")
    nb.gotcha(
        "When you want a *separate* table from a filtered slice, add `.copy()`: "
        "`vip = df[df[\"spend\"] > 1000].copy()`. If you edit a slice without `.copy()`, Pandas may warn "
        "`SettingWithCopyWarning` and your change might not stick. Rule of thumb: **filter, then "
        "`.copy()`, then edit.**"
    )


# --------------------------------------------------------------------------- #
def _lesson_merge(nb: NB):
    nb.lesson("m3-merge", "Lesson 3.11 — Merging / Joining Tables")
    nb.md(
        "**What it is.** `left.merge(right, on=\"key\")` stitches two tables together where a shared "
        "**key** column matches — exactly like a SQL join.\n\n"
        "**Why it exists.** Data lives in separate tables: customers in one, orders in another. To "
        "answer 'how much did *Ana* spend?', you must combine them on `customer_id`.\n\n"
        "**Real-world analogy.** Matching a guest list to an RSVP list by name to build one combined "
        "sheet.\n\n"
        "**Join types (brief):** the default is an **inner** join — it keeps only keys present in "
        "*both* tables. (There are also left/right/outer joins for keeping unmatched rows.)\n\n"
        "**On the job.** Real analysis almost always spans multiple tables; merging is how you bring "
        "them together before summarising."
    )
    nb.md("**Worked example:**")
    nb.code(
        'customers = pd.DataFrame({"cust_id": [1, 2, 3], "name": ["Ana", "Ben", "Cara"]})\n'
        'orders = pd.DataFrame({"cust_id": [1, 1, 3], "amount": [100, 50, 200]})\n'
        '\n'
        'merged = orders.merge(customers, on="cust_id")   # inner join on cust_id\n'
        'print(merged)\n'
        '# Ben (id 2) has no orders, so he does not appear in an inner join.'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Merge `orders` with `customers` on `cust_id`. Store the **number of rows** in the result "
        "(`n_merged`) and **Ana's total amount** (`ana_total`)."
    )
    nb.practice(
        "m3_merge",
        placeholder=(
            'customers = pd.DataFrame({"cust_id": [1, 2, 3], "name": ["Ana", "Ben", "Cara"]})\n'
            'orders = pd.DataFrame({"cust_id": [1, 1, 3], "amount": [100, 50, 200]})\n'
            '\n'
            'n_merged = None   # YOUR CODE HERE — rows after merging on cust_id\n'
            'ana_total = None  # YOUR CODE HERE — total amount for the customer named "Ana"'
        ),
        solution=(
            'customers = pd.DataFrame({"cust_id": [1, 2, 3], "name": ["Ana", "Ben", "Cara"]})\n'
            'orders = pd.DataFrame({"cust_id": [1, 1, 3], "amount": [100, 50, 200]})\n'
            '\n'
            'merged = orders.merge(customers, on="cust_id")\n'
            'n_merged = len(merged)\n'
            'ana_total = merged[merged["name"] == "Ana"]["amount"].sum()'
        ),
        hint='orders.merge(customers, on="cust_id"); len(...); filter name=="Ana" then sum amount.',
        label="merge tables",
    )
    nb.check("m3_merge", user="(n_merged, ana_total)", expected="(3, 150)",
             hint="Three order rows match a customer; Ana's two orders total 150.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q11.** `df1.merge(df2, on=\"id\")` (default) keeps rows where…?\n\n"
        "- **A)** `id` matches in **both** tables\n- **B)** all rows regardless of matching\n"
        "- **C)** the columns are identical\n"
    )
    nb.practice("m3_q_merge", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="The default inner join needs the key in both.",
                label="quiz: merge")
    nb.mcq("m3_q_merge", user="answer", correct="A",
           explanation="An inner join keeps only keys found in both tables.",
           hint="Inner join = intersection of keys.")
    nb.realjob(
        "There are more join types you'll meet on the job: a **left join** keeps *all* rows of the "
        "left table (filling blanks where the right has no match) — vital when you don't want to lose "
        "customers who happen to have no orders yet. You'll also soon use `pivot_table` (spreadsheet-"
        "style summaries), handle **dates/times**, and hunt down **duplicates & outliers**. You've got "
        "the foundation; these are the natural next layer."
    )
    nb.keyterms([
        ("DataFrame", "a table of rows and columns — your main analysis object."),
        ("Series", "a single column of a DataFrame."),
        ("index", "the row labels of a DataFrame."),
        (".loc / .iloc", "select by label / by integer position."),
        ("boolean mask", "a True/False Series used to filter rows: df[df[\"x\"] > 5]."),
        ("groupby", "split rows into groups and aggregate (total/average) each — 'by category'."),
        ("NaN / missing value", "an empty cell; handle with isna / fillna / dropna."),
        ("merge / join", "combine two tables on a shared key column."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m3-test", "🧪 Module 3 Test — A Real Wrangling Workflow")
    nb.md(
        "A realistic mini-pipeline: the `region` column is messy (mixed case). Clean it, then answer "
        "four questions. Each correct variable scores a point.\n\n"
        "> `show_hint('m3_test')` for guidance, `show_solution('m3_test')` for the full answer."
    )
    nb.practice(
        "m3_test",
        placeholder=(
            'data = pd.DataFrame({\n'
            '    "region": ["North", "south", "NORTH", "South", "north"],\n'
            '    "product": ["A", "B", "A", "B", "C"],\n'
            '    "revenue": [1000, 500, 1500, 800, 300],\n'
            '})\n'
            '\n'
            '# YOUR CODE HERE — clean region (strip + lower), then fill each variable:\n'
            'test_clean_regions = None  # sorted list of distinct cleaned regions\n'
            'test_total_revenue = None  # total revenue across all rows\n'
            'test_region_totals = None  # {cleaned_region: total revenue} dict\n'
            'test_top_region = None     # cleaned region with the highest total revenue'
        ),
        solution=(
            'data = pd.DataFrame({\n'
            '    "region": ["North", "south", "NORTH", "South", "north"],\n'
            '    "product": ["A", "B", "A", "B", "C"],\n'
            '    "revenue": [1000, 500, 1500, 800, 300],\n'
            '})\n'
            '\n'
            'data["region"] = data["region"].str.strip().str.lower()\n'
            'test_clean_regions = sorted(data["region"].unique().tolist())\n'
            'test_total_revenue = data["revenue"].sum()\n'
            'test_region_totals = data.groupby("region")["revenue"].sum().to_dict()\n'
            'test_top_region = data.groupby("region")["revenue"].sum().idxmax()'
        ),
        hint="Clean with .str.strip().str.lower(); then unique/sorted, sum, "
             "groupby(...).sum().to_dict(), and .idxmax().",
        label="Module 3 test",
    )
    nb.check("m3_test_regions", user="test_clean_regions", expected="['north', 'south']",
             hint="After cleaning, only 'north' and 'south' remain.")
    nb.check("m3_test_total", user="test_total_revenue", expected="4100",
             hint="1000+500+1500+800+300 = 4100.")
    nb.check("m3_test_group", user="test_region_totals",
             expected="{'north': 2800, 'south': 1300}",
             hint="north = 1000+1500+300 = 2800; south = 500+800 = 1300.")
    nb.check("m3_test_top", user="test_top_region", expected="'north'",
             hint="North's total (2800) beats South's (1300).")
    nb.md(
        "🎉 **Module 3 complete — this is the core of the job.** You can load, inspect, select, "
        "filter, sort, derive, group, clean, and merge data. Next we go one level deeper into the "
        "fast numeric engine under Pandas: **NumPy**."
    )

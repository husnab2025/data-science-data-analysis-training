"""
Module 4 — NumPy (the fast numeric engine under Pandas).

arrays vs lists · creation · indexing/slicing (1D & 2D) · vectorized operations ·
broadcasting · useful methods & dtypes · NumPy vs Pandas · Module 4 test.

`np` and `pd` are imported by the notebook's setup cell. Checks compare bare
variables (None-safe) against expected arrays/scalars.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_arrays(nb)
    _lesson_index(nb)
    _lesson_vector(nb)
    _lesson_broadcast(nb)
    _lesson_methods(nb)
    _lesson_vs_pandas(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod4", "Module 4 · NumPy")
    nb.md(
        "You've been using Pandas — and most Pandas columns are backed by a **NumPy-like array** under "
        "the hood. NumPy is the number-crunching engine of the entire Python data world.\n\n"
        "**Why it matters for the job:** when you need raw speed on numbers — feature matrices for "
        "machine learning, image pixels, simulations, or fast math across millions of values — you "
        "reach for NumPy. It's typically **10–100× faster** than plain Python loops, and scikit-learn "
        "(Module 6) expects its inputs as NumPy arrays.\n\n"
        "**The big idea:** a NumPy **array** looks like a list, but it does math on the *whole array "
        "at once* (no loops) and usually stores everything as one compact type (often numeric)."
    )
    nb.role_note(
        "NumPy leans a little more **Data Scientist**: it's the array format that machine-learning "
        "tools (Module 6) expect. Analysts touch it less directly, but every fast numeric operation "
        "in Pandas is really NumPy doing the work underneath."
    )


# --------------------------------------------------------------------------- #
def _lesson_arrays(nb: NB):
    nb.lesson("m4-arrays", "Lesson 4.1 — Arrays vs Lists (and how to create them)")
    nb.md(
        "**What it is.** `np.array([...])` turns a list into an **ndarray**. Key differences from a "
        "list:\n\n"
        "- **Homogeneous:** usually one shared data type (often numeric) — which keeps it fast + compact.\n"
        "- **Vectorised math:** `arr * 2` doubles every element; `list * 2` just repeats the list!\n"
        "- **Multi-dimensional:** arrays can be 2D (matrices), 3D, and beyond.\n\n"
        "Handy creators: `np.zeros(n)`, `np.ones(n)`, `np.arange(start, stop, step)`, "
        "`np.linspace(start, stop, count)`.\n\n"
        "**Why it exists.** Python lists are flexible but slow for math. NumPy trades that flexibility "
        "for blazing numeric performance.\n\n"
        "**Real-world analogy.** A list is a mixed drawer of odds and ends; a NumPy array is a "
        "purpose-built egg carton — uniform slots, easy to process all at once.\n\n"
        "**On the job.** You'll create arrays for numeric features, sequences of time steps, and grids "
        "of values feeding models and charts."
    )
    nb.md("**Worked example:**")
    nb.code(
        'a = np.array([1, 2, 3, 4])\n'
        'print("array   :", a, "| dtype:", a.dtype, "| shape:", a.shape)\n'
        'print("zeros   :", np.zeros(3))\n'
        'print("arange  :", np.arange(0, 10, 2))     # 0,2,4,6,8\n'
        'print("linspace:", np.linspace(0, 1, 5))    # 0,0.25,0.5,0.75,1\n'
        '\n'
        'print("list * 2 :", [1, 2, 3] * 2)          # repeats -> [1,2,3,1,2,3]\n'
        'print("array * 2:", np.array([1, 2, 3]) * 2)  # doubles  -> [2 4 6]'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Create a NumPy array `prices` holding `[10, 20, 30, 40]`, and an array `seq` holding "
        "`0, 1, 2, 3, 4` using `np.arange`."
    )
    nb.practice(
        "m4_create",
        placeholder=(
            'prices = None  # YOUR CODE HERE — np.array([...])\n'
            'seq = None     # YOUR CODE HERE — np.arange(...) giving 0,1,2,3,4'
        ),
        solution=(
            'prices = np.array([10, 20, 30, 40])\n'
            'seq = np.arange(5)'
        ),
        hint="np.array([10, 20, 30, 40]); np.arange(5) counts 0..4.",
        label="create arrays",
    )
    nb.check("m4_create", user="(prices, seq)",
             expected="(np.array([10, 20, 30, 40]), np.array([0, 1, 2, 3, 4]))",
             hint="prices is [10 20 30 40]; seq is [0 1 2 3 4].")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** A key advantage of a NumPy array over a list is that it…?\n\n"
        "- **A)** can freely hold mixed types\n- **B)** does fast math on the whole array at once\n"
        "- **C)** cannot be indexed\n"
    )
    nb.practice("m4_q_arrays", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="Think about `arr * 2` vs `list * 2`.",
                label="quiz: arrays")
    nb.mcq("m4_q_arrays", user="answer", correct="B",
           explanation="Vectorised math on the whole array is NumPy's superpower.",
           hint="It's about speed and whole-array math.")


# --------------------------------------------------------------------------- #
def _lesson_index(nb: NB):
    nb.lesson("m4-index", "Lesson 4.2 — Indexing & Slicing (1D and 2D)")
    nb.md(
        "**What it is.** Indexing works like lists — plus a clean 2D syntax:\n\n"
        "- 1D: `a[0]`, `a[-1]`, `a[1:4]` (a slice).\n"
        "- 2D: `m[row, col]` for one cell; `m[:, 0]` for a whole **column**; `m[1, :]` for a **row**.\n\n"
        "**Why it exists.** Data is often a grid (rows × features). The `[row, col]` notation makes "
        "grabbing rows, columns, and cells effortless.\n\n"
        "**Real-world analogy.** A chessboard: `m[row, col]` names one square; `m[:, 0]` is the whole "
        "left file (column).\n\n"
        "**On the job.** You'll slice feature columns out of a data matrix and pull individual rows as "
        "samples to inspect."
    )
    nb.md("**Worked example:**")
    nb.code(
        'a = np.array([10, 20, 30, 40, 50])\n'
        'print(a[0], a[-1], a[1:4])          # 10 50 [20 30 40]\n'
        '\n'
        'm = np.array([[1, 2, 3],\n'
        '              [4, 5, 6]])\n'
        'print("cell [0,2]  :", m[0, 2])     # 3\n'
        'print("column 1    :", m[:, 1])     # [2 5]\n'
        'print("row 1       :", m[1, :])     # [4 5 6]'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "From the arrays below, store the **middle three** values of `a` in `middle_three`, the "
        "**last** value of `a` in `last`, and the bottom-right cell of `grid` in `corner`."
    )
    nb.practice(
        "m4_index",
        placeholder=(
            'a = np.array([5, 10, 15, 20, 25])\n'
            'grid = np.array([[1, 2], [3, 4]])\n'
            '\n'
            'middle_three = None  # YOUR CODE HERE — a[1:4]\n'
            'last = None          # YOUR CODE HERE — the last element of a\n'
            'corner = None        # YOUR CODE HERE — grid bottom-right (row 1, col 1)'
        ),
        solution=(
            'a = np.array([5, 10, 15, 20, 25])\n'
            'grid = np.array([[1, 2], [3, 4]])\n'
            '\n'
            'middle_three = a[1:4]\n'
            'last = a[-1]\n'
            'corner = grid[1, 1]'
        ),
        hint="a[1:4] for the middle; a[-1] for last; grid[1, 1] for bottom-right.",
        label="index & slice",
    )
    nb.check("m4_index", user="(middle_three, last, corner)",
             expected="(np.array([10, 15, 20]), 25, 4)",
             hint="Middle three are 10,15,20; last is 25; corner is 4.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** For a 2D array `m`, what does `m[:, 0]` select?\n\n"
        "- **A)** the first row\n- **B)** the first column\n- **C)** the single first element\n"
    )
    nb.practice("m4_q_index", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="The `:` means 'all rows', the 0 means 'column 0'.",
                label="quiz: 2D indexing")
    nb.mcq("m4_q_index", user="answer", correct="B",
           explanation="`m[:, 0]` = all rows, column 0 → the first column.",
           hint="Colon = all rows.")


# --------------------------------------------------------------------------- #
def _lesson_vector(nb: NB):
    nb.lesson("m4-vector", "Lesson 4.3 — Vectorized Operations (math without loops)")
    nb.md(
        "**What it is.** Arithmetic and comparisons apply to **every element at once**:\n\n"
        "```python\n"
        "a + 10     a * 2     a ** 2     a + b     a > 3\n"
        "```\n\n"
        "No `for` loop, no `.append` — and it runs in optimised C under the hood.\n\n"
        "**Why it exists.** Looping over millions of numbers in pure Python is painfully slow. "
        "Vectorisation is both faster to run *and* faster to write/read.\n\n"
        "**Real-world analogy.** Instead of applying a 10% discount to each price by hand, you stamp "
        "'×0.9' across the whole catalogue in one motion.\n\n"
        "**On the job.** Scaling features, computing revenue = price×qty across a whole column, "
        "normalising data — all one-liners thanks to vectorisation."
    )
    nb.md("**Worked example:**")
    nb.code(
        'a = np.array([1, 2, 3, 4])\n'
        'print("a + 10 :", a + 10)     # [11 12 13 14]\n'
        'print("a * 2  :", a * 2)      # [2 4 6 8]\n'
        'print("a ** 2 :", a ** 2)     # [1 4 9 16]\n'
        '\n'
        'b = np.array([10, 20, 30, 40])\n'
        'print("a + b  :", a + b)      # elementwise add\n'
        'print("a > 2  :", a > 2)      # [False False True True]'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "From `costs`, compute `totals` = each cost **plus 10% tax** (`* 1.1`), and `discounted` = "
        "each cost **minus 50**."
    )
    nb.practice(
        "m4_vector",
        placeholder=(
            'costs = np.array([100, 200, 300])\n'
            '\n'
            'totals = None      # YOUR CODE HERE — costs with 10% tax added\n'
            'discounted = None  # YOUR CODE HERE — costs reduced by 50'
        ),
        solution=(
            'costs = np.array([100, 200, 300])\n'
            '\n'
            'totals = costs * 1.1\n'
            'discounted = costs - 50'
        ),
        hint="costs * 1.1 adds 10%; costs - 50 subtracts from every element.",
        label="vectorized math",
    )
    nb.check("m4_vector", user="(totals, discounted)",
             expected="(np.array([110.0, 220.0, 330.0]), np.array([50, 150, 250]))",
             hint="totals = [110, 220, 330]; discounted = [50, 150, 250].")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** What does `np.array([1, 2, 3]) * 2` produce?\n\n"
        "- **A)** `[1, 2, 3, 1, 2, 3]`\n- **B)** `[2, 4, 6]`\n- **C)** an error\n"
    )
    nb.practice("m4_q_vector", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'",
                hint="Unlike a list, an array multiplies each element (it doesn't repeat).",
                label="quiz: vectorized")
    nb.mcq("m4_q_vector", user="answer", correct="B",
           explanation="Arrays do element-wise math → [2, 4, 6]. (A list would repeat instead.)",
           hint="Element-wise, not repetition.")
    nb.tip(
        "Golden rule of fast data code: **if you're writing a `for` loop over numbers, ask whether a "
        "vectorised operation could do it instead.** `arr * 1.1` beats looping element by element — "
        "it's shorter, clearer, and often 10–100× faster. Loops aren't wrong, but vectorising is the "
        "pro move."
    )


# --------------------------------------------------------------------------- #
def _lesson_broadcast(nb: NB):
    nb.lesson("m4-broadcast", "Lesson 4.4 — Broadcasting")
    nb.md(
        "**What it is.** **Broadcasting** lets NumPy combine arrays of *compatible but different* "
        "shapes by automatically stretching the smaller one. The simplest case is array-with-scalar "
        "(`arr * 10`); it also works row-with-matrix, column-with-matrix, etc.\n\n"
        "**Why it exists.** It saves you from manually tiling/reshaping data just to line shapes up — "
        "the math 'just works' when shapes are compatible.\n\n"
        "**Real-world analogy.** Applying one tax rate to every cell of a spreadsheet: you write the "
        "rate once and it 'broadcasts' across the whole grid.\n\n"
        "**On the job.** Normalising each column of a feature matrix by subtracting its mean, or "
        "scaling a whole table by a vector of factors — broadcasting makes these one-liners."
    )
    nb.md("**Worked example:**")
    nb.code(
        'matrix = np.array([[1, 2, 3],\n'
        '                   [4, 5, 6]])\n'
        '\n'
        'print("matrix * 10:\\n", matrix * 10)        # scalar broadcast\n'
        '\n'
        'add_row = np.array([10, 20, 30])            # shape (3,)\n'
        'print("matrix + row:\\n", matrix + add_row)  # row added to EVERY row'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Using `matrix` and `add_row`, compute `result` = `matrix + add_row` and `scaled` = "
        "`matrix * 10`."
    )
    nb.practice(
        "m4_broadcast",
        placeholder=(
            'matrix = np.array([[1, 2, 3], [4, 5, 6]])\n'
            'add_row = np.array([10, 20, 30])\n'
            '\n'
            'result = None  # YOUR CODE HERE — matrix + add_row (broadcast the row)\n'
            'scaled = None  # YOUR CODE HERE — every element times 10'
        ),
        solution=(
            'matrix = np.array([[1, 2, 3], [4, 5, 6]])\n'
            'add_row = np.array([10, 20, 30])\n'
            '\n'
            'result = matrix + add_row\n'
            'scaled = matrix * 10'
        ),
        hint="Just write matrix + add_row and matrix * 10 — broadcasting handles the shapes.",
        label="broadcasting",
    )
    nb.check("m4_broadcast", user="(result, scaled)",
             expected="(np.array([[11, 22, 33], [14, 25, 36]]), "
                      "np.array([[10, 20, 30], [40, 50, 60]]))",
             hint="The row adds to each matrix row; scaling multiplies every cell by 10.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** Broadcasting lets you…?\n\n"
        "- **A)** combine arrays of compatible but different shapes\n"
        "- **B)** only add arrays of the exact same shape\n- **C)** sort an array\n"
    )
    nb.practice("m4_q_broadcast", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="It's about auto-stretching shapes to fit.",
                label="quiz: broadcasting")
    nb.mcq("m4_q_broadcast", user="answer", correct="A",
           explanation="Broadcasting stretches compatible shapes so they can combine.",
           hint="Different-but-compatible shapes.")


# --------------------------------------------------------------------------- #
def _lesson_methods(nb: NB):
    nb.lesson("m4-methods", "Lesson 4.5 — Useful Methods & Data Types")
    nb.md(
        "**What it is.** Arrays come with fast built-in summaries and a **dtype** (data type):\n\n"
        "- `a.sum()`, `a.mean()`, `a.min()`, `a.max()`, `a.std()` → one-shot statistics.\n"
        "- `a.argmax()` / `a.argmin()` → the **index** of the max/min (great for 'which one?').\n"
        "- `a.dtype` → the element type (`int64`, `float64`…); `a.astype(float)` → convert it.\n\n"
        "**Why it exists.** These are the numeric summaries every analysis needs, computed in "
        "optimised C.\n\n"
        "**Real-world analogy.** A calculator's M+ memory that instantly reports the total, average, "
        "and biggest of everything you punched in.\n\n"
        "**On the job.** `argmax` answers 'which month was best?'; `mean`/`std` describe a distribution; "
        "`astype` fixes a column that loaded as the wrong type before modelling."
    )
    nb.md("**Worked example:**")
    nb.code(
        'a = np.array([3, 1, 4, 1, 5, 9, 2])\n'
        'print("sum :", a.sum(), "| mean:", a.mean(), "| max:", a.max())\n'
        'print("argmax (index of max):", a.argmax())   # 5\n'
        'print("dtype:", a.dtype)\n'
        'print("as float:", a.astype(float).dtype)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "For `arr`, store the **mean** in `arr_mean`, the **max** in `arr_max`, and the **index of the "
        "max** in `arr_argmax`."
    )
    nb.practice(
        "m4_methods",
        placeholder=(
            'arr = np.array([4, 8, 15, 16, 23, 42])\n'
            '\n'
            'arr_mean = None    # YOUR CODE HERE — the average\n'
            'arr_max = None     # YOUR CODE HERE — the largest value\n'
            'arr_argmax = None  # YOUR CODE HERE — the INDEX of the largest value'
        ),
        solution=(
            'arr = np.array([4, 8, 15, 16, 23, 42])\n'
            '\n'
            'arr_mean = arr.mean()\n'
            'arr_max = arr.max()\n'
            'arr_argmax = arr.argmax()'
        ),
        hint="arr.mean(); arr.max(); arr.argmax() gives the position, not the value.",
        label="array methods",
    )
    nb.check("m4_methods", user="(arr_mean, arr_max, arr_argmax)",
             expected="(18.0, 42, 5)",
             hint="Mean is 108/6 = 18.0; max is 42; it sits at index 5.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** `a.argmax()` returns…?\n\n"
        "- **A)** the maximum value\n- **B)** the index (position) of the maximum\n- **C)** the count\n"
    )
    nb.practice("m4_q_methods", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="'arg' means 'the argument/position that gives...'.",
                label="quiz: argmax")
    nb.mcq("m4_q_methods", user="answer", correct="B",
           explanation="argmax gives the position of the max; use a.max() for the value itself.",
           hint="Position, not value.")


# --------------------------------------------------------------------------- #
def _lesson_vs_pandas(nb: NB):
    nb.lesson("m4-vs", "Lesson 4.6 — NumPy vs Pandas: When to Use Which")
    nb.md(
        "**The short version:**\n\n"
        "| | **NumPy** | **Pandas** |\n"
        "|---|---|---|\n"
        "| Best for | pure numeric math, matrices, ML features | labelled tables, mixed types, cleaning |\n"
        "| Structure | `ndarray` (positions only) | `DataFrame` (named rows & columns) |\n"
        "| Missing data | clunky | first-class (`NaN`, `fillna`, `dropna`) |\n"
        "| Under the hood | *is* the engine | **built on NumPy** |\n\n"
        "**They're teammates, not rivals.** A Pandas column is usually backed by a NumPy-like array — "
        "`df[\"x\"].to_numpy()` hands it to you. You'll **clean and explore in Pandas**, then "
        "**hand a NumPy array to scikit-learn** for modelling.\n\n"
        "**On the job.** Use Pandas for the messy, labelled, real-world data wrangling; drop to NumPy "
        "for heavy numeric computation and to feed models."
    )
    nb.md("**Worked example — the bridge between them:**")
    nb.code(
        's = pd.Series([1, 2, 3, 4])\n'
        'arr = s.to_numpy()                 # Pandas -> NumPy\n'
        'print(type(arr).__name__, arr, "sum:", arr.sum())\n'
        '\n'
        'back = pd.Series(arr)              # NumPy -> Pandas\n'
        'print(type(back).__name__)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Convert the Series `s` to a NumPy array and store its **sum** in `arr_sum`."
    )
    nb.practice(
        "m4_bridge",
        placeholder=(
            's = pd.Series([1, 2, 3, 4])\n'
            '\n'
            'arr = None      # YOUR CODE HERE — s as a NumPy array (s.to_numpy())\n'
            'arr_sum = None  # YOUR CODE HERE — the sum of that array'
        ),
        solution=(
            's = pd.Series([1, 2, 3, 4])\n'
            '\n'
            'arr = s.to_numpy()\n'
            'arr_sum = arr.sum()'
        ),
        hint="s.to_numpy() converts it; then arr.sum().",
        label="Pandas ↔ NumPy",
    )
    nb.check("m4_bridge", user="arr_sum", expected="10",
             hint="1 + 2 + 3 + 4 = 10.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q6.** You have a labelled table with mixed-type columns and missing values to clean. Best "
        "tool?\n\n"
        "- **A)** NumPy\n- **B)** Pandas\n- **C)** plain Python lists\n"
    )
    nb.practice("m4_q_vs", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'B'", hint="Labels + mixed types + missing data = its speciality.",
                label="quiz: which tool")
    nb.mcq("m4_q_vs", user="answer", correct="B",
           explanation="Pandas is built for labelled, messy, mixed-type tabular data.",
           hint="Think named columns and NaN handling.")
    nb.keyterms([
        ("array (ndarray)", "NumPy's fast, fixed-type container — like a list built for math."),
        ("vectorized operation", "math applied to the whole array at once, no loop (e.g. arr * 2)."),
        ("broadcasting", "auto-stretching compatible shapes so they can combine."),
        ("dtype", "the data type of an array's elements (int64, float64, ...)."),
        ("argmax / argmin", "the index (position) of the max / min value."),
        (".to_numpy()", "convert a Pandas Series/DataFrame into a NumPy array for modelling."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m4-test", "🧪 Module 4 Test — Vectorized Sales Math")
    nb.md(
        "Monthly **units sold** are in a NumPy array, at a fixed `price`. Answer four questions with "
        "vectorised NumPy — each is worth a point.\n\n"
        "> `show_hint('m4_test')` / `show_solution('m4_test')` are available."
    )
    nb.practice(
        "m4_test",
        placeholder=(
            'units = np.array([120, 85, 200, 150, 90, 175])\n'
            'price = 12.5\n'
            '\n'
            '# YOUR CODE HERE:\n'
            'test_total_units = None       # total units across all months\n'
            'test_avg_units = None         # average units per month\n'
            'test_revenue = None           # array of revenue per month (units * price)\n'
            'test_best_month_index = None  # index of the month with the most units'
        ),
        solution=(
            'units = np.array([120, 85, 200, 150, 90, 175])\n'
            'price = 12.5\n'
            '\n'
            'test_total_units = units.sum()\n'
            'test_avg_units = units.mean()\n'
            'test_revenue = units * price\n'
            'test_best_month_index = units.argmax()'
        ),
        hint="units.sum(); units.mean(); units * price (vectorised); units.argmax() for the index.",
        label="Module 4 test",
    )
    nb.check("m4_test_total", user="test_total_units", expected="820",
             hint="Add all six months of units.")
    nb.check("m4_test_avg", user="test_avg_units", expected="820 / 6",
             hint="Total units divided by 6 months.")
    nb.check("m4_test_revenue", user="test_revenue",
             expected="np.array([1500.0, 1062.5, 2500.0, 1875.0, 1125.0, 2187.5])",
             hint="Multiply the whole units array by price at once.")
    nb.check("m4_test_best", user="test_best_month_index", expected="2",
             hint="The biggest value (200) is at index 2.")
    nb.md(
        "🎉 **Module 4 done.** You can create arrays, index in 1D/2D, run vectorised math, broadcast, "
        "summarise with methods, and move between NumPy and Pandas. Now let's make data *visible* — "
        "on to **Matplotlib**."
    )

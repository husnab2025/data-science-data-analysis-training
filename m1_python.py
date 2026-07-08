"""
Module 1 — Python Fundamentals, Continued.

Builds straight on top of what the learner already knows (variables, types,
arithmetic, comparisons, if/elif/else, and/or/not, lists, indexing, len, sum).

Sub-lessons: max/min/mean · list operations · looping · list comprehensions ·
reversing lists · then a hands-on Module 1 test.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_stats(nb)
    _lesson_list_ops(nb)
    _lesson_looping(nb)
    _lesson_comprehensions(nb)
    _lesson_reversing(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod1", "Module 1 · Python Fundamentals, Continued")
    nb.md(
        "You can already create lists and add them up with `sum()`. In this module we turn "
        "those raw skills into the everyday toolkit of a working analyst: finding the biggest "
        "and smallest values, reshaping lists, **looping** through data to compute things, and "
        "writing compact **list comprehensions**.\n\n"
        "**Why this matters for the job:** almost every analysis starts as a plain Python list of "
        "numbers — daily sales, website clicks, sensor readings — *before* it ever becomes a fancy "
        "Pandas table. Being fluent here means you can answer a manager's question in seconds "
        "instead of reaching for a spreadsheet.\n\n"
        "> 🧭 Work top-to-bottom. Run each **worked example**, then do the **🎯 your turn** cell and "
        "run the **✅ self-check** right below it."
    )
    nb.recap(
        "You've finished the welcome. Now we sharpen your raw Python — the muscles you'll flex before "
        "every Pandas analysis later."
    )
    nb.role_note(
        "These fundamentals are shared bedrock for **both** roles. A Data Analyst uses them to quickly "
        "tally and reshape data; a Data Scientist uses the very same loops and comprehensions to "
        "prepare features for models."
    )


# --------------------------------------------------------------------------- #
def _lesson_stats(nb: NB):
    nb.lesson("m1-stats", "Lesson 1.1 — Max, Min & Average (the analyst's first questions)")
    nb.md(
        "**What it is.** Three tiny functions that answer three huge business questions:\n"
        "- `max(values)` → the **largest** number ('What was our best day?')\n"
        "- `min(values)` → the **smallest** number ('What was our worst day?')\n"
        "- **mean / average** → the *typical* value = `sum(values) / len(values)` "
        "('What do we do on a normal day?')\n\n"
        "**Why it exists.** A list of 500 numbers is impossible to eyeball. These collapse a whole "
        "column of data into a single, decision-ready number.\n\n"
        "**Real-world analogy.** Think of your monthly bank statement. You don't read all 200 "
        "transactions — you look at your *biggest* expense, your *smallest*, and your *average* "
        "daily spend. That's `max`, `min`, and mean.\n\n"
        "**A non-code example.** A teacher with 30 test scores instantly reports the top score, the "
        "lowest score, and the class average — without adding anything up by hand for the audience.\n\n"
        "**On the job.** When your manager asks *“What were our best and worst sales days last week, "
        "and what's the daily average?”*, this is literally the code you'd write. The average is also "
        "the foundation of nearly every metric you'll ever report."
    )
    nb.md("**Worked example** — one week of store sales:")
    nb.code(
        'weekly_sales = [1200, 980, 1450, 1610, 1305, 720, 1890]\n'
        '\n'
        'print("Best day  :", max(weekly_sales))   # largest value\n'
        'print("Worst day :", min(weekly_sales))   # smallest value\n'
        '\n'
        'total = sum(weekly_sales)                 # add everything up\n'
        'average = total / len(weekly_sales)       # divide by how many days\n'
        'print("Total week:", total)\n'
        'print("Daily avg :", round(average, 2))\n'
        '\n'
        '# Python\'s statistics module gives the same mean without doing it by hand:\n'
        'print("mean() check:", round(statistics.mean(weekly_sales), 2))'
    )
    nb.realjob(
        "The **average** can mislead when data is lopsided. If one customer spends $1,000,000 and nine "
        "spend $10, the 'average' spend is ~$100,009 — a nonsense number describing nobody. That's why "
        "analysts also use the **median** (the middle value), the **standard deviation** (how spread "
        "out the numbers are), and **percentiles**. You'll study these in statistics next; for now, "
        "just remember the average is only the *start* of the story."
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Here are one week's **store visits**. Fill in the three variables using `max`, `min`, and "
        "`sum(...)/len(...)`."
    )
    nb.practice(
        "m1_stats",
        placeholder=(
            'store_visits = [340, 512, 289, 601, 455]\n'
            '\n'
            'peak = None        # YOUR CODE HERE — the busiest day\n'
            'quietest = None    # YOUR CODE HERE — the slowest day\n'
            'avg_visits = None  # YOUR CODE HERE — the average visits per day'
        ),
        solution=(
            'store_visits = [340, 512, 289, 601, 455]\n'
            '\n'
            'peak = max(store_visits)\n'
            'quietest = min(store_visits)\n'
            'avg_visits = sum(store_visits) / len(store_visits)'
        ),
        hint="peak → max(), quietest → min(), average → sum(store_visits) / len(store_visits).",
        label="max / min / average",
    )
    nb.check(
        "m1_stats",
        user="(peak, quietest, avg_visits)",
        expected="(601, 289, 2197 / 5)",
        hint="Busiest is 601, quietest is 289, and the average is the total (2197) divided by 5.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** Which expression correctly computes the **average** of a list `xs`?\n\n"
        "- **A)** `max(xs) / len(xs)`\n"
        "- **B)** `sum(xs) / len(xs)`\n"
        "- **C)** `min(xs) + max(xs)`\n\n"
        "Set `answer` to `'A'`, `'B'`, or `'C'`."
    )
    nb.practice(
        "m1_q_stats",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Average = everything added up, divided by how many there are.",
        label="quiz: average",
    )
    nb.mcq("m1_q_stats", user="answer", correct="B",
           explanation="Average = sum ÷ count = sum(xs) / len(xs).",
           hint="It's the total divided by the count.")


# --------------------------------------------------------------------------- #
def _lesson_list_ops(nb: NB):
    nb.lesson("m1-listops", "Lesson 1.2 — Growing, Shrinking & Slicing Lists")
    nb.md(
        "**What it is.** A list isn't frozen — you can add, insert, and remove items, and grab "
        "sub-sections ('slices'). The core moves:\n\n"
        "| Operation | What it does |\n"
        "|---|---|\n"
        "| `lst.append(x)` | add `x` to the **end** |\n"
        "| `lst.insert(0, x)` | add `x` to the **front** (prepend) |\n"
        "| `lst.insert(i, x)` | insert `x` **at position `i`** |\n"
        "| `lst.remove(x)` | remove the **first `x`** by value |\n"
        "| `lst.pop()` / `lst.pop(i)` | remove & **return** the last item / item at `i` |\n"
        "| `del lst[i]` | delete the item at index `i` |\n"
        "| `lst[a:b]` | a **slice** — items from `a` up to (not including) `b` |\n"
        "| `lst[-1]` | **negative index** — count from the end |\n\n"
        "**Why it exists.** Real data changes: a new sale arrives, a cancelled order is removed, you "
        "need only the *top 10* rows. Lists let you model that movement.\n\n"
        "**Real-world analogy.** A shopping cart: you `append` items as you shop, `remove` the milk "
        "you changed your mind about, and `pop` items at the checkout one by one.\n\n"
        "**On the job.** You'll `append` results as you process records in a loop, `slice` to preview "
        "'the first 5 rows', and use **negative indexing** to grab 'the most recent entry' — the same "
        "idea Pandas uses for `.head()` and `.tail()` later."
    )
    nb.md("**Worked example** — watch the cart change step by step:")
    nb.code(
        'cart = ["milk", "bread", "eggs"]\n'
        'cart.append("butter")     # end      -> [..., "butter"]\n'
        'cart.insert(0, "coffee")  # front    -> ["coffee", ...]\n'
        'cart.insert(2, "sugar")   # position -> index 2 becomes "sugar"\n'
        'print("after adds :", cart)\n'
        '\n'
        'cart.remove("bread")      # by value\n'
        'last = cart.pop()         # removes & returns the last item\n'
        'first = cart.pop(0)       # removes & returns index 0\n'
        'del cart[0]               # deletes index 0 (no return value)\n'
        'print("after removes:", cart)\n'
        'print("popped last :", last, "| popped first:", first)\n'
        '\n'
        'print("first two   :", cart[:2])   # slice\n'
        'print("last item   :", cart[-1])   # negative index'
    )
    nb.md(
        "### 🎯 Your turn — edit an inventory list\n"
        "Starting from `products`, make these three changes **in order**:\n"
        "1. add `\"sprocket\"` to the **end**, 2. add `\"bolt\"` to the **front**, 3. remove `\"gadget\"`."
    )
    nb.practice(
        "m1_listops",
        placeholder=(
            'products = ["widget", "gadget", "gizmo"]\n'
            '\n'
            '# YOUR CODE HERE (modify `products` in place):\n'
            '# 1) append "sprocket"\n'
            '# 2) insert "bolt" at the front (index 0)\n'
            '# 3) remove "gadget"'
        ),
        solution=(
            'products = ["widget", "gadget", "gizmo"]\n'
            '\n'
            'products.append("sprocket")\n'
            'products.insert(0, "bolt")\n'
            'products.remove("gadget")'
        ),
        hint='Use products.append(...), products.insert(0, ...), then products.remove("gadget").',
        label="append / insert / remove",
    )
    nb.check(
        "m1_listops",
        user="products",
        expected="['bolt', 'widget', 'gizmo', 'sprocket']",
        hint="After all three steps the order should be bolt, widget, gizmo, sprocket.",
    )
    nb.md(
        "### 🎯 Your turn — slicing & negative indexing\n"
        "From `q`, grab the first three items, the last two items, and the very last item."
    )
    nb.practice(
        "m1_slicing",
        placeholder=(
            'q = [10, 20, 30, 40, 50, 60]\n'
            '\n'
            'first_three = None  # YOUR CODE HERE — a slice\n'
            'last_two = None     # YOUR CODE HERE — a slice using a negative start\n'
            'last_item = None    # YOUR CODE HERE — a single negative index'
        ),
        solution=(
            'q = [10, 20, 30, 40, 50, 60]\n'
            '\n'
            'first_three = q[:3]\n'
            'last_two = q[-2:]\n'
            'last_item = q[-1]'
        ),
        hint="q[:3] = first three; q[-2:] = last two; q[-1] = last item.",
        label="slicing & negative index",
    )
    nb.check(
        "m1_slicing",
        user="(first_three, last_two, last_item)",
        expected="([10, 20, 30], [50, 60], 60)",
        hint="first_three=[10,20,30], last_two=[50,60], last_item=60.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** Which reliably gives the **last** element of a non-empty list `xs`?\n\n"
        "- **A)** `xs[0]`\n"
        "- **B)** `xs[-1]`\n"
        "- **C)** `xs[len(xs)]`\n"
    )
    nb.practice(
        "m1_q_listops",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Indexing starts at 0, so the last valid index is len(xs) - 1 — or just -1.",
        label="quiz: last element",
    )
    nb.mcq("m1_q_listops", user="answer", correct="B",
           explanation="`xs[-1]` counts from the end; `xs[len(xs)]` is off-by-one and errors.",
           hint="Counting from the end is safest.")


# --------------------------------------------------------------------------- #
def _lesson_looping(nb: NB):
    nb.lesson("m1-loops", "Lesson 1.3 — Looping: Doing Something to Every Item")
    nb.md(
        "**What it is.** A **loop** repeats an action for each item in a collection so you don't "
        "write the same line 500 times.\n\n"
        "- `for item in things:` → run the body **once per item** (the workhorse).\n"
        "- `for i in range(n):` → loop `n` times with a counter `0, 1, ... n-1`.\n"
        "- `while condition:` → keep looping **until** something becomes false.\n"
        "- `enumerate(things)` → loop and get **both the position and the item**.\n"
        "- `continue` → **skip** the rest of this round; `break` → **stop** the loop entirely.\n"
        "- **nested loops** → a loop inside a loop (e.g., every region × every product).\n\n"
        "**Why it exists.** Data comes in bulk. Loops are how you apply one rule — 'add up the "
        "evens', 'flag orders over \\$100' — to an entire dataset automatically.\n\n"
        "**Real-world analogy.** A cashier scanning a cart: the same action (beep, add to total) "
        "repeated for every item. `break` = a price-check halts the line; `continue` = skip a "
        "damaged item and move on.\n\n"
        "**On the job.** Before Pandas does it for you in one line, you'll loop to compute running "
        "totals, filter records, and transform values. Understanding the loop is what makes the "
        "one-line Pandas version make sense."
    )
    nb.md("**Worked example** — every looping tool in one place:")
    nb.code(
        'prices = [9.99, 19.99, 4.50]\n'
        'for p in prices:                      # for-each\n'
        '    print("price:", p)\n'
        '\n'
        'for i in range(3):                    # counted loop: 0,1,2\n'
        '    print("step", i)\n'
        '\n'
        'balance = 100\n'
        'while balance > 0:                    # repeat until condition fails\n'
        '    balance -= 40\n'
        'print("final balance:", balance)      # 100 -> 60 -> 20 -> -20\n'
        '\n'
        'for idx, name in enumerate(["Ann", "Bob", "Cara"]):   # position + value\n'
        '    print(idx, name)\n'
        '\n'
        'for n in range(1, 11):                # continue + break\n'
        '    if n % 2 == 0:\n'
        '        continue                      # skip even numbers\n'
        '    if n > 7:\n'
        '        break                         # stop once past 7\n'
        '    print("odd kept:", n)             # 1, 3, 5, 7'
    )
    nb.md(
        "### 🎯 Your turn — sum only the even numbers\n"
        "Loop over `nums` and add up **only the even** values into `even_total` "
        "(a number is even when `n % 2 == 0`)."
    )
    nb.practice(
        "m1_loop_sum",
        placeholder=(
            'nums = [3, 8, 11, 4, 7, 10]\n'
            'even_total = 0\n'
            '\n'
            '# YOUR CODE HERE — loop over nums and add the even ones to even_total'
        ),
        solution=(
            'nums = [3, 8, 11, 4, 7, 10]\n'
            'even_total = 0\n'
            '\n'
            'for n in nums:\n'
            '    if n % 2 == 0:\n'
            '        even_total += n'
        ),
        hint="Inside the loop, use `if n % 2 == 0:` then `even_total += n`.",
        label="loop + filter sum",
    )
    nb.check("m1_loop_sum", user="even_total", expected="22",
             hint="The evens are 8, 4 and 10, which total 22.")
    nb.md(
        "### 🎯 Your turn — number the items with `enumerate`\n"
        "Build a list `labeled` where each entry is the string `\"<index>: <fruit>\"`."
    )
    nb.practice(
        "m1_loop_enum",
        placeholder=(
            'fruits = ["apple", "pear"]\n'
            'labeled = []\n'
            '\n'
            '# YOUR CODE HERE — use enumerate to append "0: apple", "1: pear", ...'
        ),
        solution=(
            'fruits = ["apple", "pear"]\n'
            'labeled = []\n'
            '\n'
            'for i, fruit in enumerate(fruits):\n'
            '    labeled.append(f"{i}: {fruit}")'
        ),
        hint='Loop `for i, fruit in enumerate(fruits):` and append an f-string `f"{i}: {fruit}"`.',
        label="enumerate",
    )
    nb.check("m1_loop_enum", user="labeled", expected="['0: apple', '1: pear']",
             hint="Each item is the index, a colon-space, then the fruit.")
    nb.md(
        "### 🎯 Your turn — a `while` loop\n"
        "A `while` loop repeats *until a condition becomes false*. Starting from `countdown = 5`, keep "
        "subtracting 1 until it reaches 0, counting how many steps you take in `steps`."
    )
    nb.practice(
        "m1_loop_while",
        placeholder=(
            'countdown = 5\n'
            'steps = 0\n'
            '\n'
            '# YOUR CODE HERE — while countdown > 0: subtract 1 and add 1 to steps'
        ),
        solution=(
            'countdown = 5\n'
            'steps = 0\n'
            '\n'
            'while countdown > 0:\n'
            '    countdown -= 1\n'
            '    steps += 1'
        ),
        hint="`while countdown > 0:` then inside do `countdown -= 1` and `steps += 1`.",
        label="while loop",
    )
    nb.check("m1_loop_while", user="steps", expected="5",
             hint="Going 5→0 one step at a time takes exactly 5 steps.")
    nb.md(
        "### 🎯 Your turn — loop with `range()`\n"
        "Use `range(1, 6)` (the numbers 1,2,3,4,5) to add them up into `total`."
    )
    nb.practice(
        "m1_loop_range",
        placeholder=(
            'total = 0\n'
            '\n'
            '# YOUR CODE HERE — for n in range(1, 6): add n to total'
        ),
        solution=(
            'total = 0\n'
            '\n'
            'for n in range(1, 6):\n'
            '    total += n'
        ),
        hint="`for n in range(1, 6):` then `total += n`. Note range(1, 6) stops BEFORE 6.",
        label="range loop",
    )
    nb.check("m1_loop_range", user="total", expected="15",
             hint="1+2+3+4+5 = 15 (range(1, 6) does not include 6).")
    nb.gotcha(
        "`range(1, 6)` gives 1,2,3,4,5 — it **stops before** the second number, so 6 is not included. "
        "This 'up to but not including' rule trips up nearly every beginner. `range(5)` gives "
        "0,1,2,3,4."
    )
    nb.md(
        "### 🎯 Your turn — `break` early\n"
        "Loop through `values` and stop **the moment** you hit a number greater than 100, storing "
        "that first big number in `first_big` (use `break`)."
    )
    nb.practice(
        "m1_loop_break",
        placeholder=(
            'values = [10, 50, 90, 130, 70, 200]\n'
            'first_big = None\n'
            '\n'
            '# YOUR CODE HERE — loop; when a value > 100, set first_big = value and break'
        ),
        solution=(
            'values = [10, 50, 90, 130, 70, 200]\n'
            'first_big = None\n'
            '\n'
            'for v in values:\n'
            '    if v > 100:\n'
            '        first_big = v\n'
            '        break'
        ),
        hint="Inside the loop: `if v > 100:` set `first_big = v` then `break` to stop immediately.",
        label="break",
    )
    nb.check("m1_loop_break", user="first_big", expected="130",
             hint="The first value over 100 is 130; break stops before reaching 200.")
    nb.md(
        "### 🎯 Your turn — a nested loop\n"
        "A **nested** loop is a loop inside a loop. Build every combination of `sizes` and `colors` as "
        "strings like `\"S-red\"` into the list `combos`."
    )
    nb.practice(
        "m1_loop_nested",
        placeholder=(
            'sizes = ["S", "M"]\n'
            'colors = ["red", "blue"]\n'
            'combos = []\n'
            '\n'
            '# YOUR CODE HERE — for each size, for each color, append f"{size}-{color}"'
        ),
        solution=(
            'sizes = ["S", "M"]\n'
            'colors = ["red", "blue"]\n'
            'combos = []\n'
            '\n'
            'for size in sizes:\n'
            '    for color in colors:\n'
            '        combos.append(f"{size}-{color}")'
        ),
        hint="Put one `for` loop inside another; the inner append uses an f-string f\"{size}-{color}\".",
        label="nested loop",
    )
    nb.check("m1_loop_nested", user="combos",
             expected="['S-red', 'S-blue', 'M-red', 'M-blue']",
             hint="2 sizes × 2 colors = 4 combinations, in that order.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** Inside a loop, what does `continue` do?\n\n"
        "- **A)** stops the loop completely\n"
        "- **B)** skips straight to the next iteration\n"
        "- **C)** restarts the loop from the beginning\n"
    )
    nb.practice(
        "m1_q_loop",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="`break` stops; `continue` just skips the rest of the current round.",
        label="quiz: continue",
    )
    nb.mcq("m1_q_loop", user="answer", correct="B",
           explanation="`continue` abandons the current iteration and moves to the next item.",
           hint="It does NOT stop the whole loop — that's break.")


# --------------------------------------------------------------------------- #
def _lesson_comprehensions(nb: NB):
    nb.lesson("m1-comp", "Lesson 1.4 — List Comprehensions (loops in one line)")
    nb.md(
        "**What it is.** A **list comprehension** builds a new list in a single readable line:\n\n"
        "```python\n"
        "[ expression   for item in things   if condition ]\n"
        "```\n\n"
        "Read it as: *“give me `expression` for each `item` in `things` (optionally only when "
        "`condition` is true).”*\n\n"
        "**Why it exists.** The 'make an empty list, loop, `append`' pattern is so common that Python "
        "gives you a compact shorthand for it — less code, fewer bugs, easier to read once it clicks.\n\n"
        "**Real-world analogy.** An assembly line with a filter: raw parts go in, each gets the *same* "
        "transformation, and a quality gate lets only the good ones through.\n\n"
        "**On the job.** You'll use these constantly for quick data shaping: apply a 10% discount to "
        "every price, keep only orders above a threshold, convert every name to uppercase. It's the "
        "pure-Python cousin of a Pandas column operation."
    )
    nb.md("**Worked example** — basic, filtered, and conditional:")
    nb.code(
        'nums = [1, 2, 3, 4, 5]\n'
        '\n'
        'squares = [n * n for n in nums]                 # transform every item\n'
        'evens = [n for n in nums if n % 2 == 0]         # keep only some items\n'
        'labels = ["hot" if t > 25 else "cold"           # choose per item\n'
        '          for t in [30, 18, 27]]\n'
        '\n'
        'print("squares:", squares)   # [1, 4, 9, 16, 25]\n'
        'print("evens  :", evens)     # [2, 4]\n'
        'print("labels :", labels)    # [\'hot\', \'cold\', \'hot\']'
    )
    nb.md(
        "### 🎯 Your turn — apply a 10% discount\n"
        "Use a comprehension to build `discounted`, where every price in `prices` is multiplied by "
        "`0.9` (a 10% discount)."
    )
    nb.practice(
        "m1_comp",
        placeholder=(
            'prices = [12, 45, 7, 89, 33]\n'
            '\n'
            'discounted = None  # YOUR CODE HERE — [ ... for p in prices ]'
        ),
        solution=(
            'prices = [12, 45, 7, 89, 33]\n'
            '\n'
            'discounted = [p * 0.9 for p in prices]'
        ),
        hint="Pattern: [p * 0.9 for p in prices].",
        label="comprehension: transform",
    )
    nb.check("m1_comp", user="discounted", expected="[p * 0.9 for p in [12, 45, 7, 89, 33]]",
             hint="Multiply each price by 0.9 inside the brackets.")
    nb.md(
        "### 🎯 Your turn — keep only the big orders\n"
        "Build `big_orders` containing only the values in `orders` that are **100 or more**."
    )
    nb.practice(
        "m1_comp_cond",
        placeholder=(
            'orders = [120, 45, 300, 80, 210]\n'
            '\n'
            'big_orders = None  # YOUR CODE HERE — [ o for o in orders if ... ]'
        ),
        solution=(
            'orders = [120, 45, 300, 80, 210]\n'
            '\n'
            'big_orders = [o for o in orders if o >= 100]'
        ),
        hint="Add a filter: [o for o in orders if o >= 100].",
        label="comprehension: filter",
    )
    nb.check("m1_comp_cond", user="big_orders", expected="[120, 300, 210]",
             hint="Only 120, 300 and 210 clear the 100 threshold.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** What does `[n * 2 for n in [1, 2, 3]]` produce?\n\n"
        "- **A)** `[1, 2, 3]`\n"
        "- **B)** `[2, 4, 6]`\n"
        "- **C)** `[1, 4, 9]`\n"
    )
    nb.practice(
        "m1_q_comp",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Each item is doubled.",
        label="quiz: comprehension",
    )
    nb.mcq("m1_q_comp", user="answer", correct="B",
           explanation="Each element is multiplied by 2 → [2, 4, 6].",
           hint="Double every number.")


# --------------------------------------------------------------------------- #
def _lesson_reversing(nb: NB):
    nb.lesson("m1-reverse", "Lesson 1.5 — Reversing a List (three ways)")
    nb.md(
        "**What it is.** Three ways to reverse order, with one important difference:\n\n"
        "- `lst.reverse()` — reverses **in place** (changes the original list, returns `None`).\n"
        "- `lst[::-1]` — a slice that returns a **new reversed list** (original untouched).\n"
        "- `list(reversed(lst))` — `reversed()` gives a reverse *iterator*; wrap in `list(...)`.\n\n"
        "**Why the difference matters.** 'In place' vs 'new copy' is one of the most common sources "
        "of bugs for beginners. If you still need the original order later, **don't** use "
        "`.reverse()` — make a reversed copy with `[::-1]`.\n\n"
        "**Real-world analogy.** `reverse()` is flipping the actual stack of documents on your desk. "
        "`[::-1]` is photocopying them in reverse order while leaving the original stack alone.\n\n"
        "**On the job.** You'll reverse to show **most-recent-first** timelines, or to sort then flip "
        "for a 'top to bottom' ranking. Knowing which method preserves the original saves you from "
        "silently corrupting your data."
    )
    nb.md("**Worked example:**")
    nb.code(
        'a = [1, 2, 3]\n'
        'a.reverse()                       # in place\n'
        'print("a after reverse():", a)    # [3, 2, 1]\n'
        '\n'
        'b = [1, 2, 3]\n'
        'b_rev = b[::-1]                   # new list\n'
        'print("b:", b, "| b_rev:", b_rev) # b unchanged, b_rev reversed\n'
        '\n'
        'c_rev = list(reversed([1, 2, 3]))\n'
        'print("reversed():", c_rev)       # [3, 2, 1]'
    )
    nb.md(
        "### 🎯 Your turn — most recent first\n"
        "Make `recent_first` a **reversed copy** of `timeline` **without changing** `timeline` itself."
    )
    nb.practice(
        "m1_reverse",
        placeholder=(
            'timeline = ["Q1", "Q2", "Q3", "Q4"]\n'
            '\n'
            'recent_first = None  # YOUR CODE HERE — reversed COPY (do not modify timeline)'
        ),
        solution=(
            'timeline = ["Q1", "Q2", "Q3", "Q4"]\n'
            '\n'
            'recent_first = timeline[::-1]'
        ),
        hint="The copy-that-doesn't-touch-the-original way is the slice `timeline[::-1]`.",
        label="reverse (copy)",
    )
    nb.check("m1_reverse", user="recent_first", expected="['Q4', 'Q3', 'Q2', 'Q1']",
             hint="Q4 should come first, Q1 last.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** Which reverses a list **without modifying the original**?\n\n"
        "- **A)** `lst.reverse()`\n"
        "- **B)** `lst[::-1]`\n"
        "- **C)** `del lst[:]`\n"
    )
    nb.practice(
        "m1_q_reverse",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="One of these makes a brand-new list and leaves the original alone.",
        label="quiz: reverse copy",
    )
    nb.mcq("m1_q_reverse", user="answer", correct="B",
           explanation="`lst[::-1]` returns a new reversed list; `.reverse()` mutates in place.",
           hint="Slicing builds a new list.")
    nb.keyterms([
        ("max() / min()", "the largest / smallest value in a collection."),
        ("mean (average)", "sum of the values divided by how many there are."),
        ("append / insert / pop", "add to the end / add at a position / remove-and-return an item."),
        ("slice (lst[a:b])", "a sub-section of a list, from a up to (not including) b."),
        ("negative index (lst[-1])", "count from the end; -1 is the last item."),
        ("for / while loop", "repeat an action for each item / until a condition is false."),
        ("list comprehension", "build a new list in one line: [expr for item in things if cond]."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m1-test", "🧪 Module 1 Test — Put It All Together")
    nb.md(
        "A mini analyst task combining everything above. Here is a company's **monthly revenue** for "
        "a year. Fill in all five variables. Each correct answer scores a point — run the check cell "
        "after each one (or all at once).\n\n"
        "> Stuck on any part? `show_hint('m1_test')` for guidance, or `show_solution('m1_test')` to "
        "reveal the full worked answer."
    )
    nb.practice(
        "m1_test",
        placeholder=(
            'monthly_revenue = [42000, 38500, 51000, 47250, 60300, 55800,\n'
            '                   49900, 62100, 58400, 71200, 68000, 80500]\n'
            '\n'
            '# YOUR CODE HERE — fill each variable:\n'
            'test_best = None       # highest single month\n'
            'test_worst = None      # lowest single month\n'
            'test_avg = None        # average across all 12 months\n'
            'test_h2 = None         # TOTAL revenue of the second half (months 7-12)\n'
            'test_above_avg = None  # list of month-values strictly greater than the average'
        ),
        solution=(
            'monthly_revenue = [42000, 38500, 51000, 47250, 60300, 55800,\n'
            '                   49900, 62100, 58400, 71200, 68000, 80500]\n'
            '\n'
            'test_best = max(monthly_revenue)\n'
            'test_worst = min(monthly_revenue)\n'
            'test_avg = sum(monthly_revenue) / len(monthly_revenue)\n'
            'test_h2 = sum(monthly_revenue[6:])\n'
            'test_above_avg = [m for m in monthly_revenue if m > test_avg]'
        ),
        hint="best→max, worst→min, avg→sum/len, second half→slice [6:] then sum, "
             "above-average→a comprehension with `if m > test_avg`.",
        label="Module 1 test",
    )
    nb.check("m1_test_best", user="test_best", expected="80500",
             hint="Use max() on the whole list.")
    nb.check("m1_test_worst", user="test_worst", expected="38500",
             hint="Use min() on the whole list.")
    nb.check("m1_test_avg", user="test_avg", expected="684950 / 12",
             hint="sum(monthly_revenue) / len(monthly_revenue).")
    nb.check("m1_test_h2", user="test_h2", expected="390100",
             hint="The second half is monthly_revenue[6:]; sum that slice.")
    nb.check("m1_test_above_avg", user="test_above_avg",
             expected="[60300, 62100, 58400, 71200, 68000, 80500]",
             hint="Keep every month greater than test_avg (~57079).")
    nb.md(
        "🎉 **That's Module 1.** You can now summarise data (max/min/mean), reshape lists, loop with "
        "purpose, write comprehensions, and reverse safely — the raw-Python muscles every analyst "
        "uses before reaching for Pandas. Next up: **Dictionaries**."
    )

"""
Module 2 — Dictionaries.

Creation & access · add/update/remove · looping (keys/values/items) ·
nested dictionaries · dictionary comprehensions · Module 2 test.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_create(nb)
    _lesson_mutate(nb)
    _lesson_loop(nb)
    _lesson_nested(nb)
    _lesson_comprehensions(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod2", "Module 2 · Dictionaries")
    nb.md(
        "Lists are great when order and position matter. But a huge amount of real data is really "
        "about **labels**: this customer's name, that product's price, this region's total. For "
        "labelled data, Python gives us the **dictionary** — a set of `key: value` pairs.\n\n"
        "**Why this matters for the job:** a single row of a spreadsheet — one customer, one order — "
        "is naturally a dictionary (`{'name': ..., 'total': ...}`). In fact, a Pandas DataFrame (the "
        "star of Module 3) is essentially a collection of dictionaries with superpowers. Master "
        "dictionaries now and Pandas will feel familiar.\n\n"
        "**Everyday analyst uses:** representing one record, counting things (word → count), mapping "
        "codes to names (`'US' → 'United States'`), storing config/settings, and quick lookups."
    )
    nb.role_note(
        "Dictionaries are how real data *arrives*. Analysts and scientists both pull data from web "
        "**APIs**, which return **JSON** — which is essentially nested dictionaries. Getting fluent "
        "here means API data won't scare you later."
    )


# --------------------------------------------------------------------------- #
def _lesson_create(nb: NB):
    nb.lesson("m2-create", "Lesson 2.1 — Creating & Reading a Dictionary")
    nb.md(
        "**What it is.** A dictionary stores pairs: each **key** points to a **value**.\n\n"
        "```python\n"
        'product = {"name": "Laptop", "price": 1200, "in_stock": True}\n'
        "```\n\n"
        "You look things up **by key**, not by position: `product[\"price\"]` → `1200`.\n\n"
        "**Why it exists.** With a list of `[\"Laptop\", 1200, True]` you'd have to *remember* that "
        "position 1 is the price. A dictionary labels each value so your code reads like plain "
        "English and never breaks when the order changes.\n\n"
        "**Real-world analogy.** A dictionary (the book!): you don't read every page to find a word — "
        "you jump straight to it. Or your phone contacts: look up a *name* to get a *number*.\n\n"
        "**Two ways to read a value:**\n"
        "- `d[\"key\"]` — direct, but **errors** if the key is missing.\n"
        "- `d.get(\"key\", default)` — **safe**, returns `default` (or `None`) if the key is missing.\n\n"
        "**On the job.** You'll build a dictionary for each record you process, and use `.get()` "
        "constantly to handle missing fields without crashing your whole script."
    )
    nb.md("**Worked example:**")
    nb.code(
        'product = {"name": "Laptop", "price": 1200, "in_stock": True}\n'
        '\n'
        'print("name       :", product["name"])            # direct access\n'
        'print("price       :", product["price"])\n'
        'print("color (safe):", product.get("color", "unknown"))  # missing -> default\n'
        'print("has price?  :", "price" in product)         # membership test'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Create a dictionary `employee` with `name` = `\"Ravi\"`, `role` = `\"Analyst\"`, and "
        "`salary` = `75000`. Then read the salary into `emp_salary`."
    )
    nb.practice(
        "m2_create",
        placeholder=(
            'employee = None    # YOUR CODE HERE — the dictionary described above\n'
            'emp_salary = None  # YOUR CODE HERE — read the salary out of employee'
        ),
        solution=(
            'employee = {"name": "Ravi", "role": "Analyst", "salary": 75000}\n'
            'emp_salary = employee["salary"]'
        ),
        hint='Build it with { } and colons, e.g. {"name": "Ravi", ...}; then employee["salary"].',
        label="create & read",
    )
    nb.check(
        "m2_create",
        user="(employee, emp_salary)",
        expected="({'name': 'Ravi', 'role': 'Analyst', 'salary': 75000}, 75000)",
        hint="Keys are strings in quotes; salary should read back as 75000.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** How do you read key `\"x\"` from dict `d` **safely**, getting `None` if it's missing?\n\n"
        "- **A)** `d[\"x\"]`\n"
        "- **B)** `d.get(\"x\")`\n"
        "- **C)** `d.x`\n"
    )
    nb.practice(
        "m2_q_create",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="One of these never raises an error when the key is absent.",
        label="quiz: safe access",
    )
    nb.mcq("m2_q_create", user="answer", correct="B",
           explanation="`.get()` returns None (or a default) instead of raising KeyError.",
           hint="Square brackets crash on a missing key.")
    nb.gotcha(
        "Asking for a key that doesn't exist with square brackets — `d[\"missing\"]` — raises a "
        "`KeyError` and stops your code. When you're not 100% sure a key exists, use "
        "`d.get(\"missing\")` (returns `None`) or `d.get(\"missing\", 0)` (returns a default). This one "
        "habit prevents a huge share of beginner crashes."
    )


# --------------------------------------------------------------------------- #
def _lesson_mutate(nb: NB):
    nb.lesson("m2-mutate", "Lesson 2.2 — Adding, Updating & Removing Entries")
    nb.md(
        "**What it is.** Dictionaries are editable:\n\n"
        "- `d[\"new\"] = value` — **add** a new pair *or* **update** an existing key.\n"
        "- `d[\"k\"] += 1` — read-then-update (great for counting).\n"
        "- `d.pop(\"k\")` — **remove** key `\"k\"` and **return** its value.\n"
        "- `del d[\"k\"]` — delete key `\"k\"` (no return value).\n\n"
        "**Why it exists.** Data is alive — inventory goes up and down, a customer cancels, a running "
        "tally grows. You need to change the dictionary as events happen.\n\n"
        "**Real-world analogy.** A whiteboard scoreboard: you write a new team on, update a score, or "
        "wipe a team that dropped out.\n\n"
        "**On the job.** The `d[key] += 1` pattern is the classic way to **count** occurrences (how "
        "many orders per customer, how many visits per page) before you learn the Pandas shortcut."
    )
    nb.md("**Worked example:**")
    nb.code(
        'inventory = {"apples": 50}\n'
        'inventory["bananas"] = 30     # add a brand-new key\n'
        'inventory["apples"] = 45      # overwrite an existing key\n'
        'inventory["apples"] += 5      # read 45, add 5 -> 50\n'
        '\n'
        'removed = inventory.pop("bananas")   # remove and capture the value\n'
        'print("inventory:", inventory, "| removed:", removed)'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Starting from `scores`, make three edits: **add** `\"science\"` = `90`, **update** "
        "`\"english\"` to `75`, and **remove** `\"math\"`."
    )
    nb.practice(
        "m2_update",
        placeholder=(
            'scores = {"math": 80, "english": 70}\n'
            '\n'
            '# YOUR CODE HERE:\n'
            '# 1) add "science" = 90\n'
            '# 2) update "english" to 75\n'
            '# 3) remove "math"'
        ),
        solution=(
            'scores = {"math": 80, "english": 70}\n'
            '\n'
            'scores["science"] = 90\n'
            'scores["english"] = 75\n'
            'del scores["math"]'
        ),
        hint='scores["science"] = 90 ; scores["english"] = 75 ; del scores["math"].',
        label="add / update / remove",
    )
    nb.check(
        "m2_update",
        user="scores",
        expected="{'english': 75, 'science': 90}",
        hint="Only english (75) and science (90) should remain — math is gone.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** Which removes key `\"k\"` from dict `d` **and returns** its value?\n\n"
        "- **A)** `del d[\"k\"]`\n"
        "- **B)** `d.pop(\"k\")`\n"
        "- **C)** `d.remove(\"k\")`\n"
    )
    nb.practice(
        "m2_q_update",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="`del` removes but returns nothing; `.remove()` isn't a dict method at all.",
        label="quiz: pop vs del",
    )
    nb.mcq("m2_q_update", user="answer", correct="B",
           explanation="`d.pop('k')` deletes the key and hands you back its value.",
           hint="Only one of these gives you the value back.")


# --------------------------------------------------------------------------- #
def _lesson_loop(nb: NB):
    nb.lesson("m2-loop", "Lesson 2.3 — Looping Over a Dictionary")
    nb.md(
        "**What it is.** Three views let you loop over a dictionary:\n\n"
        "- `for key in d:` (or `d.keys()`) → the **keys**.\n"
        "- `for value in d.values():` → the **values**.\n"
        "- `for key, value in d.items():` → **both at once** (the most useful).\n\n"
        "`sum(d.values())` totals the numbers; `max(d, key=d.get)` finds the key with the biggest "
        "value.\n\n"
        "**Why it exists.** A dictionary is often a whole table of results. Looping lets you total "
        "it, find the winner, or reshape it.\n\n"
        "**Real-world analogy.** Reading a scoreboard row by row: for each team (key) you see its "
        "score (value), and you can tell who's winning.\n\n"
        "**On the job.** *“Total sales across all regions and tell me the top region”* is a two-line "
        "answer: `sum(sales.values())` and `max(sales, key=sales.get)`."
    )
    nb.md("**Worked example:**")
    nb.code(
        'prices = {"pen": 2, "notebook": 5, "eraser": 1}\n'
        '\n'
        'for item, cost in prices.items():     # both key and value\n'
        '    print(item, "costs", cost)\n'
        '\n'
        'print("total value :", sum(prices.values()))       # 8\n'
        'print("priciest    :", max(prices, key=prices.get)) # "notebook"'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "From `sales`, compute `total_sales` (the sum of all months) and `best_month` (the key with "
        "the highest value)."
    )
    nb.practice(
        "m2_loop",
        placeholder=(
            'sales = {"jan": 1000, "feb": 1500, "mar": 1200}\n'
            '\n'
            'total_sales = None  # YOUR CODE HERE — sum of all the values\n'
            'best_month = None   # YOUR CODE HERE — the month with the highest sales'
        ),
        solution=(
            'sales = {"jan": 1000, "feb": 1500, "mar": 1200}\n'
            '\n'
            'total_sales = sum(sales.values())\n'
            'best_month = max(sales, key=sales.get)'
        ),
        hint="Total → sum(sales.values()); best → max(sales, key=sales.get).",
        label="sum & argmax over dict",
    )
    nb.check(
        "m2_loop",
        user="(total_sales, best_month)",
        expected="(3700, 'feb')",
        hint="The three months total 3700, and February is the highest at 1500.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** Which view gives you **both** the key and value on each loop?\n\n"
        "- **A)** `d.keys()`\n"
        "- **B)** `d.values()`\n"
        "- **C)** `d.items()`\n"
    )
    nb.practice(
        "m2_q_loop",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'C'",
        hint="You want the pairs, not just one side.",
        label="quiz: items()",
    )
    nb.mcq("m2_q_loop", user="answer", correct="C",
           explanation="`.items()` yields (key, value) pairs.",
           hint="Think 'items' = pairs.")


# --------------------------------------------------------------------------- #
def _lesson_nested(nb: NB):
    nb.lesson("m2-nested", "Lesson 2.4 — Nested Dictionaries (a table of records)")
    nb.md(
        "**What it is.** A dictionary whose **values are themselves dictionaries**. This models a "
        "table where each row (record) has several fields:\n\n"
        "```python\n"
        'customers = {\n'
        '    "c1": {"name": "Ana", "orders": 3, "total": 250.0},\n'
        '    "c2": {"name": "Ben", "orders": 1, "total": 90.0},\n'
        '}\n'
        "```\n\n"
        "Reach an inner value by chaining keys: `customers[\"c1\"][\"name\"]` → `\"Ana\"`.\n\n"
        "**Why it exists.** Real records have many fields. Nesting keeps everything about one entity "
        "together and lets you look it up by an id.\n\n"
        "**Real-world analogy.** A filing cabinet: each **drawer** (outer key) holds a **folder** of "
        "details (inner dict).\n\n"
        "**On the job.** JSON data from APIs is almost always nested dictionaries. This is exactly "
        "the shape you'll `pd.DataFrame(...)` into a table in Module 3."
    )
    nb.md("**Worked example:**")
    nb.code(
        'customers = {\n'
        '    "c1": {"name": "Ana", "orders": 3, "total": 250.0},\n'
        '    "c2": {"name": "Ben", "orders": 1, "total": 90.0},\n'
        '}\n'
        '\n'
        'print("c1 name  :", customers["c1"]["name"])   # drill two levels in\n'
        'print("c2 total :", customers["c2"]["total"])\n'
        '\n'
        'customers["c1"]["orders"] += 1                 # update a nested value\n'
        'print("c1 orders:", customers["c1"]["orders"])'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "From `catalog`, read the price of `\"widget\"` into `widget_price`, then set `\"gadget\"`'s "
        "`stock` to `0` (it just sold out)."
    )
    nb.practice(
        "m2_nested",
        placeholder=(
            'catalog = {\n'
            '    "widget": {"price": 9.99, "stock": 120},\n'
            '    "gadget": {"price": 24.50, "stock": 8},\n'
            '}\n'
            '\n'
            'widget_price = None  # YOUR CODE HERE — widget\'s price\n'
            '# then set gadget\'s stock to 0'
        ),
        solution=(
            'catalog = {\n'
            '    "widget": {"price": 9.99, "stock": 120},\n'
            '    "gadget": {"price": 24.50, "stock": 8},\n'
            '}\n'
            '\n'
            'widget_price = catalog["widget"]["price"]\n'
            'catalog["gadget"]["stock"] = 0'
        ),
        hint='Chain the keys: catalog["widget"]["price"]; then catalog["gadget"]["stock"] = 0.',
        label="nested read & update",
    )
    nb.check(
        "m2_nested",
        user="(widget_price, catalog['gadget']['stock'])",
        expected="(9.99, 0)",
        hint="widget_price is 9.99 and gadget's stock should now be 0.",
    )
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** In `customers`, how do you reach the `name` inside record `\"c1\"`?\n\n"
        "- **A)** `customers[\"c1\", \"name\"]`\n"
        "- **B)** `customers[\"c1\"][\"name\"]`\n"
        "- **C)** `customers.c1.name`\n"
    )
    nb.practice(
        "m2_q_nested",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'B'",
        hint="Two separate square-bracket lookups, one per level.",
        label="quiz: nested access",
    )
    nb.mcq("m2_q_nested", user="answer", correct="B",
           explanation="Chain the brackets: outer key, then inner key.",
           hint="One bracket per level of nesting.")


# --------------------------------------------------------------------------- #
def _lesson_comprehensions(nb: NB):
    nb.lesson("m2-comp", "Lesson 2.5 — Dictionary Comprehensions")
    nb.md(
        "**What it is.** Just like list comprehensions, but they build a **dictionary**:\n\n"
        "```python\n"
        "{ key_expr: value_expr   for item in things   if condition }\n"
        "```\n\n"
        "**Why it exists.** Building a lookup table pair-by-pair is tedious; this does it in one "
        "readable line — and can filter at the same time.\n\n"
        "**Real-world analogy.** Printing a price tag for every product at once, instead of writing "
        "each tag by hand.\n\n"
        "**On the job.** Turn two lists into a lookup (`{code: name}`), apply tax to every price, or "
        "keep only the in-stock items — all in a single expression."
    )
    nb.md("**Worked example:**")
    nb.code(
        'nums = [1, 2, 3, 4]\n'
        'squares = {n: n * n for n in nums}                 # {1:1, 2:4, 3:9, 4:16}\n'
        '\n'
        'prices = {"pen": 2, "book": 5}\n'
        'with_tax = {item: cost * 1.1 for item, cost in prices.items()}\n'
        'expensive = {k: v for k, v in prices.items() if v > 3}  # filter -> {"book": 5}\n'
        '\n'
        'print(squares)\n'
        'print(with_tax)\n'
        'print(expensive)'
    )
    nb.md(
        "### 🎯 Your turn — word lengths\n"
        "Build `lengths`, a dictionary mapping each word in `products` to its length "
        "(`len(word)`)."
    )
    nb.practice(
        "m2_comp",
        placeholder=(
            'products = ["a", "bb", "ccc"]\n'
            '\n'
            'lengths = None  # YOUR CODE HERE — { word: len(word) for ... }'
        ),
        solution=(
            'products = ["a", "bb", "ccc"]\n'
            '\n'
            'lengths = {word: len(word) for word in products}'
        ),
        hint="Pattern: {word: len(word) for word in products}.",
        label="dict comprehension",
    )
    nb.check("m2_comp", user="lengths", expected="{'a': 1, 'bb': 2, 'ccc': 3}",
             hint="Each word maps to how many characters it has.")
    nb.md(
        "### 🎯 Your turn — keep only what's in stock\n"
        "From `inventory`, build `in_stock` containing only items whose quantity is **greater than 0**."
    )
    nb.practice(
        "m2_comp_cond",
        placeholder=(
            'inventory = {"apple": 50, "banana": 0, "cherry": 8}\n'
            '\n'
            'in_stock = None  # YOUR CODE HERE — filter with an if'
        ),
        solution=(
            'inventory = {"apple": 50, "banana": 0, "cherry": 8}\n'
            '\n'
            'in_stock = {k: v for k, v in inventory.items() if v > 0}'
        ),
        hint="{k: v for k, v in inventory.items() if v > 0}.",
        label="dict comprehension + filter",
    )
    nb.check("m2_comp_cond", user="in_stock", expected="{'apple': 50, 'cherry': 8}",
             hint="Banana has 0 units, so it should be dropped.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** What does `{n: n * 2 for n in [1, 2]}` produce?\n\n"
        "- **A)** `{1: 2, 2: 4}`\n"
        "- **B)** `[2, 4]`\n"
        "- **C)** `{2, 4}`\n"
    )
    nb.practice(
        "m2_q_comp",
        placeholder="answer = None  # 'A', 'B', or 'C'",
        solution="answer = 'A'",
        hint="The result is a dictionary of key→value pairs.",
        label="quiz: dict comprehension",
    )
    nb.mcq("m2_q_comp", user="answer", correct="A",
           explanation="Keys are the numbers, values are doubled → {1: 2, 2: 4}.",
           hint="It keeps the original number as the key.")
    nb.keyterms([
        ("key : value", "a dictionary pairs a label (key) with data (value)."),
        (".get(key, default)", "safe lookup — returns default instead of crashing on a missing key."),
        ("keys() / values() / items()", "loop over the labels / the data / both together."),
        ("nested dictionary", "a dict whose values are themselves dicts — models a table of records."),
        ("dict comprehension", "build a dict in one line: {k: v for item in things}."),
        ("JSON", "the text format APIs return — essentially nested dictionaries and lists."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m2-test", "🧪 Module 2 Test — Regional Sales Dashboard")
    nb.md(
        "You're handed regional sales as a dictionary. Fill in the four variables — each is worth a "
        "point.\n\n"
        "> Hint available via `show_hint('m2_test')`; full answer via `show_solution('m2_test')`."
    )
    nb.practice(
        "m2_test",
        placeholder=(
            'region_sales = {"north": 45000, "south": 38000, "east": 52000, "west": 41000}\n'
            '\n'
            '# YOUR CODE HERE:\n'
            'test_total = None    # sum of all regions\n'
            'test_best = None     # the region (key) with the highest sales\n'
            'test_avg = None      # average sales across the regions\n'
            'test_over_40k = None # dict of ONLY the regions with sales > 40000'
        ),
        solution=(
            'region_sales = {"north": 45000, "south": 38000, "east": 52000, "west": 41000}\n'
            '\n'
            'test_total = sum(region_sales.values())\n'
            'test_best = max(region_sales, key=region_sales.get)\n'
            'test_avg = test_total / len(region_sales)\n'
            'test_over_40k = {k: v for k, v in region_sales.items() if v > 40000}'
        ),
        hint="total→sum(values); best→max(d, key=d.get); avg→total/len(d); "
             "over-40k→a dict comprehension with `if v > 40000`.",
        label="Module 2 test",
    )
    nb.check("m2_test_total", user="test_total", expected="176000",
             hint="Add the four region values.")
    nb.check("m2_test_best", user="test_best", expected="'east'",
             hint="East is the largest at 52000.")
    nb.check("m2_test_avg", user="test_avg", expected="176000 / 4",
             hint="Total divided by the number of regions (4).")
    nb.check("m2_test_over_40k", user="test_over_40k",
             expected="{'north': 45000, 'east': 52000, 'west': 41000}",
             hint="South (38000) is the only one that doesn't clear 40000.")
    nb.md(
        "🎉 **Module 2 done.** Dictionaries are the shape of a *record*, and you can now build, edit, "
        "loop, nest, and comprehend them. That's the perfect mental model for what's next: "
        "**Pandas**, where each row is essentially one of these dictionaries."
    )

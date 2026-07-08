"""
Module 6 — Scikit-learn (machine learning).

what ML is + theory (train/test, over/under-fitting, metrics) · train/test split ·
regression · interpreting + visualising regression · classification ·
decision-region plot · an experiment cell (play with a knob) · Module 6 test.

Determinism: clean synthetic data + fixed random_state; checks compare rounded
values or boolean thresholds so tiny float differences never break grading.
"""
from __future__ import annotations

from nbcore import NB


def build(nb: NB):
    _intro(nb)
    _lesson_concept(nb)
    _lesson_split(nb)
    _lesson_regression(nb)
    _lesson_reg_viz(nb)
    _lesson_classification(nb)
    _lesson_class_viz(nb)
    _lesson_experiment(nb)
    _module_test(nb)


# --------------------------------------------------------------------------- #
def _intro(nb: NB):
    nb.module("mod6", "Module 6 · Scikit-learn (Machine Learning)")
    nb.md(
        "You can now wrangle and visualise data. The final leap is teaching the computer to "
        "**predict**. **Scikit-learn** is Python's standard machine-learning library, and it makes "
        "training a model a three-step ritual: **fit → predict → score**.\n\n"
        "**Why it matters for the job:** prediction is where analytics becomes *forecasting* — "
        "next quarter's sales, which customers will churn, which transactions look fraudulent. Even "
        "'analyst' roles increasingly expect you to build a simple model and, just as importantly, "
        "**explain what it means**.\n\n"
        "**We'll keep it honest and conceptual:** small, clean datasets so the ideas (not the maths) "
        "shine, and a big focus on the *theory you must know* to not fool yourself — training vs "
        "testing, and over- vs under-fitting."
    )
    nb.role_note(
        "This module is where the **Data Scientist** role goes beyond the analyst. Analysts increasingly "
        "build simple models too, but *predictive modelling, experiments, and statistics* are the DS "
        "core. Getting comfortable here is your first real step across that line."
    )


# --------------------------------------------------------------------------- #
def _lesson_concept(nb: NB):
    nb.lesson("m6-concept", "Lesson 6.1 — What Machine Learning Actually Is")
    nb.md(
        "**The core idea.** Instead of *you* writing the rules, you show the computer lots of "
        "examples and it **learns the pattern** itself. Then it applies that pattern to new, unseen "
        "cases.\n\n"
        "**The vocabulary (learn this):**\n"
        "- **Features (X)** — the inputs/clues (e.g., house size, #bedrooms).\n"
        "- **Target (y)** — what you're predicting (e.g., house price).\n"
        "- **Supervised learning** — learning from examples where the answer (`y`) is known.\n"
        "- **Regression** — predict a **number** (price, temperature).\n"
        "- **Classification** — predict a **category** (spam / not-spam).\n\n"
        "**The theory that keeps you honest:**\n"
        "- **Train/test split** — you *train* on one slice of data and *test* on a different, unseen "
        "slice. Why? Because scoring on data the model already saw is like grading a student on the "
        "exact questions they studied — it proves nothing about the real world.\n"
        "- **Overfitting** — the model *memorises* the training data (including its noise) and flops "
        "on new data. **Underfitting** — the model is too simple and misses the real pattern. Good "
        "models sit in between.\n\n"
        "**Real-world analogy.** Studying with practice exams (train) then sitting the real exam "
        "(test). Memorising the practice answers word-for-word (overfitting) fails when the real "
        "questions differ."
    )
    nb.md(
        "### 🎯 Your turn — regression or classification?\n"
        "Label each task as the string `\"regression\"` or `\"classification\"`."
    )
    nb.practice(
        "m6_tasktype",
        placeholder=(
            "# Predicting tomorrow's temperature in degrees:\n"
            'task1_type = None\n'
            "# Predicting whether an email is spam or not:\n"
            'task2_type = None'
        ),
        solution=(
            'task1_type = "regression"\n'
            'task2_type = "classification"'
        ),
        hint="Predicting a number → regression; predicting a category → classification.",
        label="task type",
    )
    nb.check("m6_tasktype", user="(task1_type, task2_type)",
             expected="('regression', 'classification')",
             hint="Temperature is a number; spam-or-not is a category.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q1.** Why do we split data into **train** and **test** sets?\n\n"
        "- **A)** to measure performance on **unseen** data\n- **B)** to make training faster\n"
        "- **C)** to remove missing values\n"
    )
    nb.practice("m6_q_concept", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'",
                hint="Testing on data the model already saw would flatter it unfairly.",
                label="quiz: train/test")
    nb.mcq("m6_q_concept", user="answer", correct="A",
           explanation="The test set estimates real-world performance on data the model never saw.",
           hint="It's about honesty on new data.")
    nb.gotcha(
        "**Models inherit the biases in their data.** If past hiring data favoured one group, a model "
        "trained on it will quietly repeat that unfairness — while looking 'objective'. *“The model "
        "decided”* is never an excuse. A responsible analyst/scientist always asks: is my data fair, "
        "and could this prediction harm someone?"
    )


# --------------------------------------------------------------------------- #
def _lesson_split(nb: NB):
    nb.lesson("m6-split", "Lesson 6.2 — The Train/Test Split")
    nb.md(
        "**What it is.** `train_test_split` randomly divides your data into a training portion and a "
        "testing portion.\n\n"
        "```python\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n"
        "```\n\n"
        "- `test_size=0.2` → hold out **20%** for testing.\n"
        "- `random_state=42` → a fixed seed so the split is **reproducible** (same rows every run).\n\n"
        "**Why it exists.** It's the guardrail against fooling yourself. Train on one part, judge on "
        "the other.\n\n"
        "**On the job.** Every honest model evaluation starts here. Skipping it is the #1 rookie "
        "mistake that makes a model look great in a notebook and fail in production."
    )
    nb.md("**Worked example:**")
    nb.code(
        'from sklearn.model_selection import train_test_split\n'
        '\n'
        'X = np.arange(10).reshape(-1, 1)   # 10 samples, 1 feature\n'
        'y = np.arange(10)\n'
        'X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n'
        'print("train:", len(X_train), "| test:", len(X_test))   # 8 | 2'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Split the 20-sample data with **30%** held out for testing and `random_state=0`. Store the "
        "training and test row counts in `n_train` and `n_test`."
    )
    nb.practice(
        "m6_split",
        placeholder=(
            'from sklearn.model_selection import train_test_split\n'
            '\n'
            'X = np.arange(20).reshape(-1, 1)\n'
            'y = np.arange(20)\n'
            '\n'
            '# YOUR CODE HERE — split with test_size=0.3, random_state=0\n'
            'n_train = None  # len of the training set\n'
            'n_test = None   # len of the test set'
        ),
        solution=(
            'from sklearn.model_selection import train_test_split\n'
            '\n'
            'X = np.arange(20).reshape(-1, 1)\n'
            'y = np.arange(20)\n'
            '\n'
            'X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)\n'
            'n_train = len(X_train)\n'
            'n_test = len(X_test)'
        ),
        hint="train_test_split(X, y, test_size=0.3, random_state=0); then len(X_train), len(X_test).",
        label="train/test split",
    )
    nb.check("m6_split", user="(n_train, n_test)", expected="(14, 6)",
             hint="30% of 20 = 6 test rows, leaving 14 for training.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q2.** `test_size=0.2` means…?\n\n"
        "- **A)** 20% of the data is held out for testing\n- **B)** 20% is used for training\n"
        "- **C)** exactly 2 rows are tested\n"
    )
    nb.practice("m6_q_split", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="test_size is the fraction reserved for testing.",
                label="quiz: test_size")
    nb.mcq("m6_q_split", user="answer", correct="A",
           explanation="test_size=0.2 reserves 20% for the test set.", hint="It's a fraction to test.")
    nb.gotcha(
        "**Never judge a model on the data it trained on.** A model can score 100% on its training "
        "data just by memorising — that proves nothing. Real performance is the score on the **unseen "
        "test set**. (A few teaching cells below score on the training data for simplicity and clean "
        "numbers — in real work, always report the *test* score.)"
    )


# --------------------------------------------------------------------------- #
def _lesson_regression(nb: NB):
    nb.lesson("m6-regression", "Lesson 6.3 — Your First Model: Linear Regression")
    nb.md(
        "**What it is.** `LinearRegression` fits the best straight line through your data. The ritual:\n\n"
        "1. `model = LinearRegression()` — create it.\n"
        "2. `model.fit(X, y)` — **learn** from the examples.\n"
        "3. `model.predict(X_new)` — **forecast** new values.\n"
        "4. `model.score(X, y)` — grade the fit (R², where 1.0 is perfect).\n\n"
        "After fitting, `model.coef_` is the slope(s) and `model.intercept_` is the offset — the "
        "learned line `y = slope·x + intercept`.\n\n"
        "**Real-world analogy.** Drawing the best-fit line through a scatter of points by eye — but "
        "the computer finds the mathematically optimal one.\n\n"
        "**On the job.** 'Given ad spend, predict sales' or 'given size, predict price' — the classic "
        "first model, and often a surprisingly strong baseline."
    )
    nb.md("**Worked example** — data that follows `y = 3x + 5`:")
    nb.code(
        'from sklearn.linear_model import LinearRegression\n'
        '\n'
        'X = np.array([[1], [2], [3], [4], [5]])\n'
        'y = np.array([8, 11, 14, 17, 20])         # exactly 3x + 5\n'
        '\n'
        'model = LinearRegression()\n'
        'model.fit(X, y)\n'
        'print("slope    :", round(model.coef_[0], 2))       # 3.0\n'
        'print("intercept:", round(model.intercept_, 2))     # 5.0\n'
        'print("predict 6:", round(model.predict([[6]])[0], 2))  # 23.0\n'
        'print("R2 score :", model.score(X, y))              # 1.0'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Fit a `LinearRegression` on data that follows `y = 2x + 1`. Store the learned slope (rounded "
        "to 1 dp) in `slope`, and the prediction for `x = 10` (rounded to 1 dp) in `pred_10`."
    )
    nb.practice(
        "m6_regression",
        placeholder=(
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5]])\n'
            'y = np.array([3, 5, 7, 9, 11])   # y = 2x + 1\n'
            '\n'
            '# YOUR CODE HERE — create, fit, then read slope and predict x=10\n'
            'slope = None    # round(model.coef_[0], 1)\n'
            'pred_10 = None  # round(model.predict([[10]])[0], 1)'
        ),
        solution=(
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5]])\n'
            'y = np.array([3, 5, 7, 9, 11])\n'
            '\n'
            'model = LinearRegression()\n'
            'model.fit(X, y)\n'
            'slope = round(model.coef_[0], 1)\n'
            'pred_10 = round(model.predict([[10]])[0], 1)'
        ),
        hint="Fit the model, then round(model.coef_[0], 1) and round(model.predict([[10]])[0], 1).",
        label="linear regression",
    )
    nb.check("m6_regression", user="(slope, pred_10)", expected="(2.0, 21.0)",
             hint="Slope is 2.0; at x=10, y = 2·10 + 1 = 21.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q3.** A regression model predicts…?\n\n"
        "- **A)** a continuous number\n- **B)** a category label\n- **C)** nothing until told\n"
    )
    nb.practice("m6_q_regression", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Think house price or temperature.",
                label="quiz: regression")
    nb.mcq("m6_q_regression", user="answer", correct="A",
           explanation="Regression outputs a continuous numeric value.", hint="A number.")


# --------------------------------------------------------------------------- #
def _lesson_reg_viz(nb: NB):
    nb.lesson("m6-regviz", "Lesson 6.4 — Interpreting & Visualising a Regression")
    nb.md(
        "**What it is.** Two ways to judge a model:\n\n"
        "- **The score (R²):** `model.score(X, y)` is **1.0** for a perfect fit and near **0** for a "
        "weak one — and it can even go **negative** if the model does worse than simply guessing the "
        "average every time. Higher is better.\n"
        "- **The picture:** scatter the **actual** points and overlay the model's **predicted** line. "
        "If the line hugs the points, it's a good fit; systematic gaps reveal problems.\n\n"
        "**Why it matters.** A single score can hide issues; the plot of *actual vs predicted* is how "
        "you sanity-check and how you explain the model to non-technical stakeholders.\n\n"
        "**On the job.** You'll pair 'R² = 0.87' with an actual-vs-predicted chart in every model "
        "write-up — the number for rigour, the picture for trust."
    )
    nb.md("**Worked example:**")
    nb.code(
        'from sklearn.linear_model import LinearRegression\n'
        '\n'
        'X = np.array([[1], [2], [3], [4], [5]])\n'
        'y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])   # noisy, roughly 2x\n'
        'model = LinearRegression().fit(X, y)\n'
        'pred = model.predict(X)\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.scatter(X.ravel(), y, label="Actual")\n'
        'ax.plot(X.ravel(), pred, color="red", label="Predicted")\n'
        'ax.set_title(f"Actual vs Predicted (R2 = {model.score(X, y):.3f})")\n'
        'ax.set_xlabel("X"); ax.set_ylabel("y"); ax.legend()\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Fit the model, plot actual vs predicted, then store whether it's a **good fit** "
        "(R² greater than 0.9) in `good_fit`."
    )
    nb.practice(
        "m6_regviz",
        placeholder=(
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5]])\n'
            'y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])\n'
            '\n'
            '# YOUR CODE HERE — fit, plot actual vs predicted, then:\n'
            'good_fit = None  # True if model.score(X, y) > 0.9'
        ),
        solution=(
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5]])\n'
            'y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])\n'
            'model = LinearRegression().fit(X, y)\n'
            'pred = model.predict(X)\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.scatter(X.ravel(), y, label="Actual")\n'
            'ax.plot(X.ravel(), pred, color="red", label="Predicted")\n'
            'ax.set_title("Actual vs Predicted")\n'
            'ax.set_xlabel("X"); ax.set_ylabel("y"); ax.legend()\n'
            'plt.show()\n'
            '\n'
            'good_fit = bool(model.score(X, y) > 0.9)'
        ),
        hint="After fitting: good_fit = bool(model.score(X, y) > 0.9).",
        label="regression fit quality",
    )
    nb.check("m6_regviz", user="good_fit", expected="True",
             hint="The near-straight data gives an R² well above 0.9.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q4.** An R² (score) close to **1.0** means…?\n\n"
        "- **A)** the model fits the data very well\n- **B)** the model is broken\n"
        "- **C)** the data has missing values\n"
    )
    nb.practice("m6_q_regviz", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="1.0 is a perfect fit.", label="quiz: R2")
    nb.mcq("m6_q_regviz", user="answer", correct="A",
           explanation="R² near 1.0 means the model explains almost all the variation.",
           hint="Higher R² = better fit.")


# --------------------------------------------------------------------------- #
def _lesson_classification(nb: NB):
    nb.lesson("m6-classify", "Lesson 6.5 — Classification (predicting categories)")
    nb.md(
        "**What it is.** When the target is a **category** (yes/no, spam/ham, class 0/1), you use a "
        "**classifier**. `LogisticRegression` is the classic starting point. Same ritual: "
        "`fit` → `predict` → `score` (here the score is **accuracy** = fraction correct).\n\n"
        "**Why it exists.** Countless business questions are yes/no: will this customer churn? is this "
        "transaction fraud? should we approve this loan?\n\n"
        "**Real-world analogy.** A spam filter learning from labelled emails, then sorting new mail "
        "into inbox vs junk.\n\n"
        "**On the job.** Churn, fraud, lead-scoring, quality pass/fail — classification is everywhere "
        "in operational analytics."
    )
    nb.md("**Worked example** — small values are class 0, large values class 1:")
    nb.code(
        'from sklearn.linear_model import LogisticRegression\n'
        '\n'
        'X = np.array([[1], [2], [3], [6], [7], [8]])\n'
        'y = np.array([0, 0, 0, 1, 1, 1])\n'
        '\n'
        'clf = LogisticRegression().fit(X, y)\n'
        'print("predict 2 ->", clf.predict([[2]])[0])   # 0 (small)\n'
        'print("predict 7 ->", clf.predict([[7]])[0])   # 1 (large)\n'
        'print("accuracy  :", clf.score(X, y))          # 1.0'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Fit a `LogisticRegression`. Predict the class of a small value (`15`) into `pred_small` and "
        "a large value (`75`) into `pred_large` (wrap each in `int(...)`), and store the training "
        "`accuracy`."
    )
    nb.practice(
        "m6_classify",
        placeholder=(
            'from sklearn.linear_model import LogisticRegression\n'
            '\n'
            'X = np.array([[10], [20], [30], [60], [70], [80]])\n'
            'y = np.array([0, 0, 0, 1, 1, 1])\n'
            '\n'
            '# YOUR CODE HERE — fit the classifier, then:\n'
            'pred_small = None  # int(clf.predict([[15]])[0])\n'
            'pred_large = None  # int(clf.predict([[75]])[0])\n'
            'accuracy = None    # clf.score(X, y)'
        ),
        solution=(
            'from sklearn.linear_model import LogisticRegression\n'
            '\n'
            'X = np.array([[10], [20], [30], [60], [70], [80]])\n'
            'y = np.array([0, 0, 0, 1, 1, 1])\n'
            '\n'
            'clf = LogisticRegression().fit(X, y)\n'
            'pred_small = int(clf.predict([[15]])[0])\n'
            'pred_large = int(clf.predict([[75]])[0])\n'
            'accuracy = clf.score(X, y)'
        ),
        hint="Fit clf, then int(clf.predict([[15]])[0]), int(clf.predict([[75]])[0]), clf.score(X, y).",
        label="classification",
    )
    nb.check("m6_classify", user="(pred_small, pred_large, accuracy)", expected="(0, 1, 1.0)",
             hint="15 → class 0, 75 → class 1, and the clean split gives 100% accuracy.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q5.** A classification model predicts…?\n\n"
        "- **A)** a category / label\n- **B)** a continuous number\n- **C)** a chart\n"
    )
    nb.practice("m6_q_classify", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="Spam or not-spam, 0 or 1.", label="quiz: classification")
    nb.mcq("m6_q_classify", user="answer", correct="A",
           explanation="Classifiers output a discrete category.", hint="A label, not a number.")
    nb.realjob(
        "**Accuracy alone can lie.** If 99% of transactions are legitimate, a lazy model that always "
        "predicts 'legit' is 99% accurate — and completely useless for catching fraud. That's why real "
        "work also uses the **confusion matrix, precision, and recall** for classification, and "
        "**MAE / RMSE** (average error size) for regression. You don't need them today; just know that "
        "'accuracy' is only the first question a good analyst asks."
    )


# --------------------------------------------------------------------------- #
def _lesson_class_viz(nb: NB):
    nb.lesson("m6-classviz", "Lesson 6.6 — Visualising Classification (decision regions)")
    nb.md(
        "**What it is.** With two features you can *see* how a classifier carves up the space: colour "
        "each region by the class the model would predict there, then overlay the real points. The "
        "boundary between colours is the **decision boundary**.\n\n"
        "**Why it matters.** It builds intuition for what the model actually learned, and reveals "
        "whether the classes are cleanly separable or hopelessly tangled.\n\n"
        "**Real-world analogy.** Drawing territory lines on a map so any new town is assigned to the "
        "nearest region.\n\n"
        "**On the job.** Great for explaining a model to stakeholders and for spotting when two "
        "classes overlap too much to separate well."
    )
    nb.md("**Worked example — shade the decision regions:**")
    nb.code(
        'from sklearn.linear_model import LogisticRegression\n'
        '\n'
        'X = np.array([[1, 1], [2, 1], [1, 2], [6, 5], [7, 6], [6, 7]])\n'
        'y = np.array([0, 0, 0, 1, 1, 1])\n'
        'clf = LogisticRegression().fit(X, y)\n'
        '\n'
        'xx, yy = np.meshgrid(np.linspace(0, 8, 100), np.linspace(0, 8, 100))\n'
        'zz = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)\n'
        '\n'
        'fig, ax = plt.subplots()\n'
        'ax.contourf(xx, yy, zz, alpha=0.2, cmap="coolwarm")   # shaded regions\n'
        'ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="black")\n'
        'ax.set_title("Decision Regions")\n'
        'ax.set_xlabel("Feature 1"); ax.set_ylabel("Feature 2")\n'
        'plt.show()'
    )
    nb.md(
        "### 🎯 Your turn\n"
        "Fit a classifier on the two-feature data and make a scatter coloured by class "
        "(`c=y`). Store the training accuracy in `class_accuracy`."
    )
    nb.practice(
        "m6_classviz",
        placeholder=(
            'from sklearn.linear_model import LogisticRegression\n'
            '\n'
            'X = np.array([[1, 2], [2, 1], [2, 3], [7, 8], [8, 7], [7, 6]])\n'
            'y = np.array([0, 0, 0, 1, 1, 1])\n'
            '\n'
            '# YOUR CODE HERE — fit, scatter X[:,0] vs X[:,1] coloured by y, then:\n'
            'class_accuracy = None  # clf.score(X, y)'
        ),
        solution=(
            'from sklearn.linear_model import LogisticRegression\n'
            '\n'
            'X = np.array([[1, 2], [2, 1], [2, 3], [7, 8], [8, 7], [7, 6]])\n'
            'y = np.array([0, 0, 0, 1, 1, 1])\n'
            'clf = LogisticRegression().fit(X, y)\n'
            '\n'
            'fig, ax = plt.subplots()\n'
            'ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="black")\n'
            'ax.set_title("Classes")\n'
            'ax.set_xlabel("Feature 1"); ax.set_ylabel("Feature 2")\n'
            'plt.show()\n'
            '\n'
            'class_accuracy = clf.score(X, y)'
        ),
        hint="Fit clf, scatter with c=y, then class_accuracy = clf.score(X, y).",
        label="classification viz",
    )
    nb.check("m6_classviz", user="class_accuracy", expected="1.0",
             hint="The two clusters are well separated → 100% accuracy.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q6.** A decision-region (boundary) plot shows…?\n\n"
        "- **A)** how the model separates the classes\n- **B)** a time trend\n- **C)** missing data\n"
    )
    nb.practice("m6_q_classviz", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'", hint="It colours which class wins in each region.",
                label="quiz: decision regions")
    nb.mcq("m6_q_classviz", user="answer", correct="A",
           explanation="Decision regions show where the model predicts each class.",
           hint="Where each class 'wins'.")


# --------------------------------------------------------------------------- #
def _lesson_experiment(nb: NB):
    nb.lesson("m6-experiment", "Lesson 6.7 — Experiment: Watch Overfitting Happen")
    nb.md(
        "**Machine learning is empirical** — you *try* things and *observe*. Here's a knob to play "
        "with: a decision tree's **`max_depth`**. A deeper tree can fit the training data more and "
        "more perfectly… which is exactly how **overfitting** creeps in.\n\n"
        "**What to watch.** As depth increases, **training** accuracy climbs toward 100% — but that "
        "doesn't mean it generalises. A model that aces the training set yet flops on the test set is "
        "the textbook symptom of overfitting.\n\n"
        "**On the job.** This 'turn a knob, watch train vs test' loop is the essence of model tuning. "
        "Learning to *distrust* a suspiciously perfect training score is a hallmark of a good analyst."
    )
    nb.md("**Worked example — deeper trees memorise more:**")
    nb.code(
        'from sklearn.tree import DecisionTreeClassifier\n'
        'from sklearn.datasets import make_classification\n'
        '\n'
        'Xc, yc = make_classification(n_samples=100, n_features=4, random_state=42)\n'
        'for depth in [1, 3, 10]:\n'
        '    m = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(Xc, yc)\n'
        '    print(f"max_depth={depth:>2}: training accuracy = {m.score(Xc, yc):.2f}")'
    )
    nb.md(
        "### 🎯 Your turn — run the experiment\n"
        "Train a **shallow** tree (`max_depth=1`) and a **deep** tree (`max_depth=None`) on the same "
        "data. Store each training accuracy, and whether the deep tree scores **at least as high** "
        "in `deep_is_higher`."
    )
    nb.practice(
        "m6_experiment",
        placeholder=(
            'from sklearn.tree import DecisionTreeClassifier\n'
            'from sklearn.datasets import make_classification\n'
            '\n'
            'Xc, yc = make_classification(n_samples=100, n_features=4, random_state=42)\n'
            '\n'
            '# YOUR CODE HERE — fit a shallow (max_depth=1) and a deep (max_depth=None) tree\n'
            'acc_shallow = None    # shallow.score(Xc, yc)\n'
            'acc_deep = None       # deep.score(Xc, yc)\n'
            'deep_is_higher = None # True if acc_deep >= acc_shallow'
        ),
        solution=(
            'from sklearn.tree import DecisionTreeClassifier\n'
            'from sklearn.datasets import make_classification\n'
            '\n'
            'Xc, yc = make_classification(n_samples=100, n_features=4, random_state=42)\n'
            '\n'
            'shallow = DecisionTreeClassifier(max_depth=1, random_state=42).fit(Xc, yc)\n'
            'deep = DecisionTreeClassifier(max_depth=None, random_state=42).fit(Xc, yc)\n'
            'acc_shallow = shallow.score(Xc, yc)\n'
            'acc_deep = deep.score(Xc, yc)\n'
            'deep_is_higher = bool(acc_deep >= acc_shallow)'
        ),
        hint="Fit both trees, score each on (Xc, yc), then compare with >=.",
        label="overfitting experiment",
    )
    nb.check("m6_experiment", user="deep_is_higher", expected="True",
             hint="An unrestricted tree drives TRAINING accuracy up (to ~1.0) — the overfitting trap.")
    nb.md(
        "### 📝 Quick quiz\n"
        "**Q7.** A model with near-perfect **training** accuracy but poor **test** accuracy is…?\n\n"
        "- **A)** overfitting\n- **B)** underfitting\n- **C)** perfect\n"
    )
    nb.practice("m6_q_experiment", placeholder="answer = None  # 'A', 'B', or 'C'",
                solution="answer = 'A'",
                hint="It memorised the training data instead of learning the general pattern.",
                label="quiz: overfitting")
    nb.mcq("m6_q_experiment", user="answer", correct="A",
           explanation="Great on training, poor on test = overfitting.",
           hint="Memorised, didn't generalise.")
    nb.keyterms([
        ("features (X) / target (y)", "the inputs you learn from / the thing you predict."),
        ("supervised learning", "learning from examples where the correct answer is known."),
        ("regression / classification", "predict a number / predict a category."),
        ("train/test split", "learn on one slice, judge honestly on an unseen slice."),
        ("fit / predict / score", "the three-step model ritual: learn, forecast, grade."),
        ("R² / accuracy", "how well a regression fits / the fraction a classifier gets right."),
        ("overfitting / underfitting", "memorising the data / too simple to catch the pattern."),
    ])


# --------------------------------------------------------------------------- #
def _module_test(nb: NB):
    nb.lesson("m6-test", "🧪 Module 6 Test — End-to-End Model")
    nb.md(
        "Run the full ritual: **split → fit → predict → score** on data following `y = 2x + 1`. "
        "Four points on offer.\n\n"
        "> `show_hint('m6_test')` / `show_solution('m6_test')` available."
    )
    nb.practice(
        "m6_test",
        placeholder=(
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])\n'
            'y = np.array([3, 5, 7, 9, 11, 13, 15, 17])   # y = 2x + 1\n'
            '\n'
            '# YOUR CODE HERE — split (test_size=0.25, random_state=42), fit on train, then:\n'
            'test_n = None        # number of TEST rows\n'
            'test_slope = None    # round(model.coef_[0], 1)\n'
            'test_pred_9 = None   # round(model.predict([[9]])[0], 1)\n'
            'test_r2 = None       # round(model.score(X_test, y_test), 2)'
        ),
        solution=(
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            'X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])\n'
            'y = np.array([3, 5, 7, 9, 11, 13, 15, 17])\n'
            '\n'
            'X_train, X_test, y_train, y_test = train_test_split(\n'
            '    X, y, test_size=0.25, random_state=42)\n'
            'model = LinearRegression().fit(X_train, y_train)\n'
            'test_n = len(X_test)\n'
            'test_slope = round(model.coef_[0], 1)\n'
            'test_pred_9 = round(model.predict([[9]])[0], 1)\n'
            'test_r2 = round(model.score(X_test, y_test), 2)'
        ),
        hint="Split, fit on X_train/y_train, then len(X_test), round(coef_[0],1), "
             "round(predict([[9]])[0],1), round(score(X_test,y_test),2).",
        label="Module 6 test",
    )
    nb.check("m6_test_n", user="test_n", expected="2",
             hint="25% of 8 rows = 2 test rows.")
    nb.check("m6_test_slope", user="test_slope", expected="2.0",
             hint="The data is exactly y = 2x + 1, so the slope is 2.0.")
    nb.check("m6_test_pred", user="test_pred_9", expected="19.0",
             hint="At x = 9: 2·9 + 1 = 19.")
    nb.check("m6_test_r2", user="test_r2", expected="1.0",
             hint="Perfectly linear data → R² of 1.0 on the test set.")
    nb.md(
        "🎉 **Module 6 complete — you've trained real models!** You understand supervised learning, "
        "the train/test split, regression and classification, how to read scores, how to visualise "
        "predictions and decision regions, and the ever-present danger of overfitting. Time to put "
        "*everything* together in the **Capstone Project**."
    )

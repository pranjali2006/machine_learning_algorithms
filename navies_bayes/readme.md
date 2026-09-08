# Naive Bayes Classifier — When to Use Which Variant

## 🎯 What is Naive Bayes?

Naive Bayes is a **classification algorithm**.

It is mainly used when the output `Y` represents **classes**, such as:

* Yes / No
* True / False
* Spam / Not Spam
* 0 / 1
* Class A / Class B / Class C

> **Important:** The Naive Bayes variant is mainly selected based on the **type of input features (X)**, not simply based on how the target `Y` is encoded.

---

## 🧠 Which Naive Bayes should I use?

| Input Features (X)   | Typical Data                     | Naive Bayes Variant |
| -------------------- | -------------------------------- | ------------------- |
| Categorical          | Sunny, Rain, Hot, Cold           | **CategoricalNB**   |
| Binary               | 0/1, True/False, Present/Absent  | **BernoulliNB**     |
| Continuous Numerical | Age, Salary, Height, Temperature | **GaussianNB**      |
| Count / Frequency    | Word counts, Term frequencies    | **MultinomialNB**   |

---

## 1️⃣ CategoricalNB

Use when your **input features are categorical**.

Example:

```text
Outlook     → Sunny / Rain / Overcast
Temperature → Hot / Mild / Cool
Wind        → Weak / Strong

Play        → Yes / No
```

Use:

```python
from sklearn.naive_bayes import CategoricalNB

model = CategoricalNB()
```

Even if the target is encoded as `0/1`, you can still use **CategoricalNB** because the important thing is that `X` is categorical.

---

## 2️⃣ BernoulliNB

Use when your **input features are binary**.

Example:

```text
Fever     → 0/1
Cough     → 0/1
Fatigue   → 0/1
Headache  → 0/1

Disease   → 0/1
```

Use:

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()
```

Think:

> **Binary features → BernoulliNB**

---

## 3️⃣ GaussianNB

Use when your **input features are continuous numerical values**.

Example:

```text
Age            → 21.5
Blood Pressure → 120.4
Glucose        → 135.7
BMI            → 24.8

Diabetes       → 0/1
```

Use:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

Think:

> **Continuous numerical features → GaussianNB**

The target can still be `0/1`, Yes/No, or multiple classes.

---

## 4️⃣ MultinomialNB

Use when your input features represent **counts or frequencies**.

A common example is text classification:

```text
"good movie good"

good  → 2
movie → 1
```

These are counts.

Use:

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
```

Think:

> **Count/Frequency features → MultinomialNB**

---

# 🚨 Important: What about Numerical X + Numerical Y?

Naive Bayes is a **classification algorithm**, not a regression algorithm.

So:

```text
X = numerical
Y = continuous numerical
```

Example:

```text
Hours studied → 8.5
Attendance    → 92%
Assignments   → 9

Marks         → 87.5
```

❌ Do NOT use Naive Bayes.

This is a **regression problem**.

You would consider algorithms such as:

```text
Linear Regression
Decision Tree Regressor
Random Forest Regressor
```

---

# ⭐ Final Memory Trick

Don't start by looking at `Y`.

First ask:

> **"What kind of data is my X?"**

```text
                What is X?
                   |
        ┌──────────┼───────────┐
        ↓          ↓           ↓
  Categorical    Binary    Continuous
        ↓          ↓           ↓
CategoricalNB  BernoulliNB  GaussianNB
                   
                   +
                   
        Count / Frequency
                ↓
         MultinomialNB
```

### One-line rule:

> **Categorical X → CategoricalNB**
> **Binary X → BernoulliNB**
> **Continuous Numerical X → GaussianNB**
> **Count/Frequency X → MultinomialNB**
> **Continuous Numerical Y → Naive Bayes is NOT appropriate**

### ⚠️ Remember

`Y = 0/1` does **NOT automatically mean BernoulliNB**.

The question is:

> **Are my INPUT FEATURES (X) binary?**

If yes → **BernoulliNB**.

If X is categorical → **CategoricalNB**.

If X is continuous numerical → **GaussianNB**.

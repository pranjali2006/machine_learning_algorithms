# Precision, Recall & F1-Score

These metrics are used to evaluate a **classification model**.

Before understanding them, remember the four confusion-matrix terms:

| Term   | Meaning                               |
| ------ | ------------------------------------- |
| **TP** | Predicted Positive, Actually Positive |
| **TN** | Predicted Negative, Actually Negative |
| **FP** | Predicted Positive, Actually Negative |
| **FN** | Predicted Negative, Actually Positive |

---

## 🎯 1. Precision

### Question it answers:

> **"When my model predicted Positive, how often was it actually Positive?"**

Formula:

```text
Precision = TP / (TP + FP)
```

### Example

Model predicted **10 people as Positive**.

* 8 were actually Positive → TP = 8
* 2 were actually Negative → FP = 2

Therefore:

```text
Precision = 8 / (8 + 2)
         = 0.80
         = 80%
```

### Think:

> **Precision = How trustworthy are my Positive predictions?**

High precision → **few False Positives**

---

# 🔎 2. Recall

### Question it answers:

> **"Out of all the people who were actually Positive, how many did my model find?"**

Formula:

```text
Recall = TP / (TP + FN)
```

### Example

There are **10 actually Positive** people.

* Model correctly found 8 → TP = 8
* Model missed 2 → FN = 2

Therefore:

```text
Recall = 8 / (8 + 2)
       = 0.80
       = 80%
```

### Think:

> **Recall = How many of the actual Positives did my model catch?**

High recall → **few False Negatives**

---

# ⚖️ 3. F1-Score

F1-score combines **Precision and Recall** into one score.

Formula:

```text
F1 = 2 × (Precision × Recall)
        -----------------------
        (Precision + Recall)
```

You don't need to calculate it manually every time.

### Think:

> **F1-score = Balance between Precision and Recall**

A model needs a good F1-score when **both false positives and false negatives matter**.

---

# 🧠 The Easiest Way to Remember

### Precision

> **"I predicted Positive. Was I right?"**

Focuses on:

```text
FP
```

High Precision → Low FP

---

### Recall

> **"There were actual Positives. Did I find them?"**

Focuses on:

```text
FN
```

High Recall → Low FN

---

### F1

> **"How well am I balancing Precision and Recall?"**

---

# 🚨 Real-World Example: Disease Detection

Suppose:

```text
Positive = Patient has disease
Negative = Patient doesn't have disease
```

### High Precision

When the model says:

> "This patient has the disease."

It should usually be correct.

Important when **False Positives are costly**.

---

### High Recall

The model should find **as many actual patients with the disease as possible**.

Missing a sick patient (False Negative) could be dangerous.

So in many medical screening situations:

> **High Recall is especially important.**

---

# 📊 Quick Comparison

| Metric        | Main Question                         | Wants to Reduce |
| ------------- | ------------------------------------- | --------------- |
| **Precision** | Were my Positive predictions correct? | **FP**          |
| **Recall**    | Did I find most actual Positives?     | **FN**          |
| **F1-score**  | How balanced are Precision & Recall?  | **FP + FN**     |

---

## ⭐ One-Line Memory Trick

```text
PRECISION → "When I said YES, was I right?"

RECALL    → "Out of all actual YES, how many did I find?"

F1        → "How well are Precision and Recall balanced?"
```

And remember:

```text
High Precision → fewer False Positives
High Recall    → fewer False Negatives
```

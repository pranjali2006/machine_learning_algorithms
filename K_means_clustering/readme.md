# K-Means Clustering — Iris Dataset

## 📌 Overview

This notebook demonstrates the complete workflow of **K-Means Clustering**, an unsupervised machine learning algorithm, using the real-world **Iris dataset** available directly from `scikit-learn`.

Unlike supervised learning, the dataset was used with **features (X) only** and the target labels were intentionally not used during clustering.

The main objective was to understand how K-Means discovers groups in unlabeled data and how to determine and evaluate an appropriate number of clusters.

---

## 🎯 Objectives

Through this implementation, I practiced:

- Loading a real dataset directly from `sklearn`
- Working with an unsupervised dataset using `X` only
- Performing basic data exploration
- Checking missing values and duplicate records
- Understanding feature types
- Feature scaling using `StandardScaler`
- Training a K-Means clustering model
- Understanding cluster labels
- Selecting the number of clusters using the Elbow Method
- Evaluating clusters using Silhouette Score
- Comparing different values of K
- Selecting a final K based on clustering evaluation
- Visualizing the resulting clusters

---

## 📊 Dataset

### Iris Dataset

The Iris dataset was loaded using:

```python
from sklearn.datasets import load_iris

iris = load_iris()
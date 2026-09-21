# Machine Learning Algorithms Journey

A structured learning repository documenting my journey through **Classical Machine Learning** — from fundamental algorithms and mathematical intuition to implementation, model evaluation, hyperparameter tuning, and practical projects.

This repository contains my **notes, Jupyter notebooks, experiments, evaluations, and machine-learning projects** developed while learning and applying classical ML concepts.

> **Current Status:** Core Classical Machine Learning algorithms completed. PCA is the remaining major topic in my current Classical ML roadmap.

---

## About This Repository

I created this repository to document my Machine Learning learning journey in a practical and structured way.

My goal has not been to only learn the syntax of machine-learning libraries. Instead, I have focused on understanding:

* What an algorithm does
* How the algorithm works conceptually
* When to use it
* When not to use it
* What assumptions it makes
* What preprocessing it requires
* How to evaluate its performance
* How to tune its hyperparameters
* How to compare different models
* How the algorithm behaves on real datasets

The repository therefore combines **theory + implementation + evaluation + experimentation + projects**.

---

# Learning Roadmap

My Classical Machine Learning journey has covered:

```text
Machine Learning
│
├── Supervised Learning
│   │
│   ├── Regression
│   │   ├── Linear Regression
│   │   ├── KNN Regression
│   │   └── SVM Regression
│   │
│   └── Classification
│       ├── Logistic Regression
│       ├── Decision Tree
│       ├── Random Forest
│       ├── KNN Classification
│       ├── SVM Classification
│       └── Naive Bayes
│
├── Ensemble Learning
│   ├── Voting
│   ├── Bagging
│   ├── Boosting
│   ├── AdaBoost
│   ├── Gradient Boosting
│   ├── XGBoost
│   ├── Stacking
│   └── Blending
│
└── Unsupervised Learning
    ├── K-Means Clustering
    ├── Hierarchical Clustering
    ├── DBSCAN
    └── PCA → In Progress
```

---

# Algorithms Covered

## 1. Linear Regression

### Concepts

* Simple and multiple linear regression
* Relationship between features and target
* Prediction using a linear function
* Error and loss
* Model fitting

### Evaluation

* MAE
* MSE
* RMSE
* R² Score

---

## 2. Logistic Regression

### Concepts

* Binary classification
* Sigmoid function
* Probability-based prediction
* Decision boundary
* Classification threshold

### Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

---

## 3. Decision Tree

### Concepts

* Decision boundaries
* Recursive splitting
* Gini impurity
* Entropy
* Information gain
* Tree depth
* Overfitting

### Evaluation

* Classification metrics
* Regression metrics
* Train/test performance comparison
* Hyperparameter experimentation

---

## 4. Random Forest

### Concepts

* Ensemble learning
* Bootstrap sampling
* Multiple decision trees
* Random feature selection
* Aggregation of predictions
* Reduction of overfitting compared with individual trees

### Evaluation

* Classification metrics
* Regression metrics
* Cross-validation
* Hyperparameter tuning

---

# Ensemble Learning

I studied multiple ensemble learning strategies and how combining models can improve predictive performance and stability.

## Techniques Covered

### Voting

Combining predictions from multiple models.

### Bagging

Training multiple models on different bootstrap samples and combining their predictions.

### Boosting

Sequentially improving weak learners by focusing on previous errors.

### AdaBoost

Adaptive boosting using weighted examples.

### Gradient Boosting

Sequentially reducing prediction errors through gradient-based optimization.

### XGBoost

A more optimized and regularized implementation of gradient boosting.

### Stacking

Combining different models using a meta-model.

### Blending

Combining predictions from multiple models using a separate validation-based approach.

---

# 5. K-Nearest Neighbors

KNN helped me understand instance-based learning and the importance of distance.

### Concepts

* Distance-based learning
* Classification
* Regression
* Choosing K
* Underfitting and overfitting
* Effect of feature scaling
* Cross-validation

### Practical Evaluation

For classification:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1-score

For regression:

* MAE
* MSE
* RMSE
* R²

I also experimented with different K values and used cross-validation to identify more appropriate values instead of selecting K arbitrarily.

---

# 6. Support Vector Machine

SVM was studied for both classification and regression.

### Concepts

* Decision boundary
* Margin
* Support vectors
* Maximum-margin classification
* Kernel trick
* Linear kernel
* RBF kernel
* Polynomial kernel
* Sigmoid kernel

### Important Hyperparameters

* `C`
* `gamma`
* `epsilon`
* Kernel

### Evaluation

Classification:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Regression:

* MAE
* MSE
* RMSE
* R²

### Model Improvement

I experimented with hyperparameters and used **GridSearchCV** to search for better configurations rather than relying only on default parameters.

---

# 7. Naive Bayes

I studied Naive Bayes from its probability foundations rather than treating it as a black-box classifier.

### Concepts

* Conditional probability
* Bayes' theorem
* Prior probability
* Likelihood
* Evidence
* Posterior probability
* Independence assumption
* Conditional independence

### Variants Practiced

* Categorical Naive Bayes
* Bernoulli Naive Bayes

I also practiced interpreting prediction probabilities using `predict_proba()`.

---

# Unsupervised Learning

## 8. K-Means Clustering

### Concepts

* Unsupervised learning
* Centroids
* Cluster assignment
* Distance-based clustering
* Iterative centroid updates
* Choosing the number of clusters

### Evaluation

* WCSS / Inertia
* Elbow Method
* Silhouette Score
* Cluster interpretation

I also explored why a clustering configuration should not be selected using only a single metric.

---

# 9. Hierarchical Clustering

### Concepts

* Hierarchical clustering
* Agglomerative approach
* Distance between clusters
* Dendrogram
* Cluster formation

The focus was on understanding how clusters can be built hierarchically and how the resulting structure can be interpreted.

---

# 10. DBSCAN

### Concepts

* Density-based clustering
* Core points
* Border points
* Noise points
* `eps`
* `min_samples`

A major part of learning DBSCAN was understanding that parameter selection is not simply about producing fewer noise points.

I explored how different parameter values change:

* Number of clusters
* Number of noise points
* Cluster structure
* Silhouette score
* Overall interpretation of the clustering result

This helped me understand the difference between **getting a result** and **validating whether the result is meaningful**.

---

# 11. PCA

**Status: In Progress**

Principal Component Analysis is the remaining major topic in my current Classical Machine Learning roadmap.

Topics to cover:

* Dimensionality reduction
* Variance
* Covariance
* Eigenvectors
* Eigenvalues
* Principal components
* Explained variance
* Feature transformation
* Visualization
* PCA before machine learning models

---

# Model Evaluation

One of the most important parts of this journey has been learning that **model performance cannot be judged by one universal metric**.

## Regression

| Metric | Purpose                                      |
| ------ | -------------------------------------------- |
| MAE    | Average absolute prediction error            |
| MSE    | Penalizes larger errors more strongly        |
| RMSE   | Error measure in the target's original scale |
| R²     | Measures explained variance                  |

## Classification

| Metric           | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| Accuracy         | Overall proportion of correct predictions           |
| Precision        | How many predicted positives were actually positive |
| Recall           | How many actual positives were detected             |
| F1-score         | Balance between precision and recall                |
| Confusion Matrix | Detailed view of prediction outcomes                |

## Clustering

| Method           | Purpose                                      |
| ---------------- | -------------------------------------------- |
| WCSS / Inertia   | Measures within-cluster compactness          |
| Elbow Method     | Helps investigate an appropriate K           |
| Silhouette Score | Measures cluster separation and cohesion     |
| Cluster Analysis | Checks whether clusters make practical sense |

---

# Model Validation & Improvement

Throughout the journey, I practiced:

* Train/Test Split
* Cross-Validation
* GridSearchCV
* Hyperparameter Tuning
* Feature Scaling
* Encoding
* Preprocessing
* Pipelines
* Model Comparison
* Error Analysis
* Parameter Sensitivity

The focus has gradually shifted from:

> **"Can I train this model?"**

to:

> **"Why should I use this model, how should I configure it, and how do I know the result is reliable?"**

---

# Practical Projects

The concepts studied here have also been applied to practical machine-learning and data projects.

## 1. NASA Turbofan Remaining Useful Life Prediction

A regression project based on the NASA C-MAPSS FD001 dataset.

Focus areas included:

* Data preprocessing
* Feature engineering
* Regression
* Model evaluation
* Remaining Useful Life prediction

---

## 2. Heart Disease Prediction

A classification project comparing machine-learning approaches for predicting heart disease.

Models explored included:

* Logistic Regression
* Decision Tree
* Random Forest

The project was also deployed as an interactive Streamlit application.

---

## 3. Email Spam Detection

A text-classification project using:

* Text preprocessing
* TF-IDF
* Logistic Regression
* Classification evaluation

The project was deployed using Streamlit.

---

## 4. Credit Card Fraud Analysis

An exploratory machine-learning/data-analysis project focused on understanding patterns in highly imbalanced transaction data.

---

## 5. Road Accident Analysis

A Power BI project involving:

* Data cleaning
* Data transformation
* Exploratory analysis
* Dashboard development
* Data visualization

---

## 6. Student Depression Analysis

A data-analysis project focused on exploring relationships and patterns within student-related data.

---

# Tools & Technologies

### Programming

* Python
* SQL

### Machine Learning

* Scikit-learn

### Data Analysis

* NumPy
* Pandas

### Visualization

* Matplotlib
* Power BI

### Development Environment

* Jupyter Notebook
* Git
* GitHub

### Deployment

* Streamlit

---

# Learning Philosophy

I am following a **concept-first and evaluation-focused approach**.

For every algorithm, I try to understand:

```text
Problem
   ↓
Type of ML Problem
   ↓
Data Understanding
   ↓
Preprocessing
   ↓
Algorithm Selection
   ↓
Training
   ↓
Evaluation
   ↓
Cross-Validation
   ↓
Hyperparameter Tuning
   ↓
Error Analysis
   ↓
Model Interpretation
   ↓
Practical Application
```

The objective is not to memorize algorithms, but to develop the ability to reason about **which approach is appropriate for a given problem and why**.

---

# Current Progress

### Classical Machine Learning

* [x] Regression
* [x] Classification
* [x] Tree-based Models
* [x] Ensemble Learning
* [x] KNN
* [x] SVM
* [x] Naive Bayes
* [x] K-Means
* [x] Hierarchical Clustering
* [x] DBSCAN
* [ ] PCA

### Next Phase

After completing PCA, the focus will shift from continuously collecting algorithms toward:

* End-to-end case studies
* Model selection
* Deeper evaluation
* Feature engineering
* Advanced model tuning
* Interview-oriented problem solving
* Real-world machine-learning workflows

---

# Repository Structure

The repository is organized around individual algorithms and evaluation/practice work.

```text
machine_learning_algorithms/
│
├── linear_regression/
├── logistic_regression/
├── decision_tree/
├── random_forest/
├── ensemble_techniques/
├── knn/
├── svm/
├── navies_bayes/
├── kmeans/
├── hierarchical_clustering/
├── dbscan/
├── model_performance_evaluation/
│
└── README.md
```

> Folder names may evolve as the repository continues to grow.

---

# Why I Built This Repository

This repository represents my transition from simply learning machine-learning algorithms to developing a more structured understanding of the **complete machine-learning workflow**.

The goal is to build the ability to answer questions such as:

* Why this algorithm?
* Why not another algorithm?
* What preprocessing is required?
* Which metric should be used?
* Is the model actually improving?
* How should hyperparameters be selected?
* Is the model overfitting?
* Does the result make sense for the real-world problem?

---

# Progress

This repository will continue to evolve as I move from **Classical Machine Learning → Advanced ML → Deep Learning → Real-world ML Systems**.

The current milestone is:

> **Core Classical Machine Learning algorithms completed — PCA remaining.**

---

## Connect

GitHub:
https://github.com/pranjali2006

Machine Learning Repository:
https://github.com/pranjali2006/machine_learning_algorithms

LinkedIn:
https://www.linkedin.com/in/pranjali-yewale/

---

## Acknowledgement

This repository represents my personal learning, experimentation, implementation, and project work in Machine Learning.

I am continuing to build my understanding through practical experimentation, case studies, projects, and continuous revision.

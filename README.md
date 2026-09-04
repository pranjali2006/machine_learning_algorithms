# 🚀 Machine Learning Algorithms Journey

> A hands-on Machine Learning learning journey covering theory, mathematics, coding implementations, model evaluation, cross-validation, hyperparameter tuning, ensemble learning, end-to-end ML projects, and deployment using Python and Scikit-learn.

---

## 👩‍💻 About This Repository

This repository documents my step-by-step journey of learning and implementing Machine Learning algorithms.

Rather than only studying theory, I focus on understanding:

* The intuition behind each algorithm
* The mathematics behind how it works
* Implementation using Python
* Practical implementation using Scikit-learn
* Model evaluation
* Feature preprocessing
* Cross-validation
* Hyperparameter tuning
* Ensemble learning
* Practical datasets and experiments

The goal is to build a strong foundation in Machine Learning and gradually progress toward advanced Machine Learning engineering, deployment, and AI systems.

---

# 📚 Learning Roadmap

## ✅ Phase 1: Supervised Machine Learning

### ✔ Linear Regression

**Status:** Completed

**Topics Covered**

* Simple Linear Regression
* Multiple Linear Regression
* Cost Function
* Gradient Descent
* Ordinary Least Squares (OLS)
* Model Training
* Model Evaluation
* Regression Metrics

---

### ✔ Logistic Regression

**Status:** Completed

**Topics Covered**

* Classification vs Regression
* Perceptron Trick
* Sigmoid Function
* Decision Boundary
* Gradient Descent
* Logistic Regression using Scikit-learn
* Classification Metrics

---

### ✔ Decision Tree

**Status:** Completed

**Topics Covered**

* Decision Tree Classification
* Decision Tree Regression
* Entropy
* Information Gain
* Gini Index
* Overfitting & Underfitting
* Model Evaluation
* Cross-Validation
* Hyperparameter Tuning
* GridSearchCV

---

### ✔ Random Forest

**Status:** Completed

**Topics Covered**

* Random Forest Classification
* Random Forest Regression
* Ensemble Learning
* Bagging
* Bootstrap Sampling
* Feature Randomness
* Model Evaluation
* Hyperparameter Tuning

---

# 🌳 Ensemble Learning

## ✔ Voting Ensemble

**Status:** Completed

Techniques Covered:

* Voting Classifier
* Voting Regressor

---

## ✔ Bagging

**Status:** Completed

Topics Covered:

* Bagging
* Bootstrap Sampling
* Aggregation
* Ensemble-based prediction

---

## ✔ Boosting Algorithms

**Status:** Completed

Algorithms Covered:

* Gradient Boosting
* AdaBoost
* XGBoost

Topics Covered:

* Boosting intuition
* Sequential model learning
* Weak learners
* Error correction
* Gradient-based boosting
* Ensemble prediction

---

# 📍 K-Nearest Neighbors (KNN)

**Status:** Completed

Topics Covered:

* KNN Classification
* KNN Regression
* Distance-based learning
* Feature Scaling
* StandardScaler
* Train-Test Split
* Model Evaluation
* Classification Metrics
* Regression Metrics
* Cross-Validation
* Selecting the best value of K

**Practical Datasets**

* Iris Dataset
* Breast Cancer Dataset
* Diabetes Dataset

---

# 🔄 Support Vector Machine (SVM)

**Status:** Completed

Support Vector Machine was practiced for both **classification and regression**, including linear and non-linear problems, feature scaling, kernels, hyperparameter tuning, and GridSearchCV.

## Topics Covered

* SVM Intuition
* Hyperplanes
* Margins
* Support Vectors
* Decision Boundary
* Linear SVM
* Kernel Trick
* Non-linear SVM
* SVM Classification
* SVM Regression
* Feature Scaling
* RBF Kernel
* Hyperparameter Tuning
* GridSearchCV
* `C`
* `epsilon`
* `gamma`
* Kernel selection

---

## 🧪 SVM Classification

**Dataset**

* Breast Cancer Dataset

**Model**

* `SVC`

**Techniques Covered**

* Train-Test Split
* Feature Scaling using StandardScaler
* Linear SVM Classification
* RBF Kernel
* Model Prediction
* Classification Evaluation
* Accuracy Score

**Result**

* Final Classification Accuracy: **96%**

---

## 📈 SVM Regression

**Dataset**

* Diabetes Dataset

**Model**

* `SVR`

**Techniques Covered**

* Train-Test Split
* Feature Scaling
* Linear SVR
* RBF SVR
* Model Prediction
* MAE
* MSE
* RMSE
* R² Score

**Initial Result**

* Linear SVR R² Score: **≈ 44.5%**

RBF SVR with default parameters performed significantly worse, demonstrating the importance of selecting suitable hyperparameters.

---

## 🔍 SVR with GridSearchCV

GridSearchCV was applied to the SVR regression problem to search for better hyperparameter combinations.

**Hyperparameters Tuned**

* `C`
* `epsilon`
* `gamma`
* `kernel`

**Best Parameters**

```text
C = 100
epsilon = 0.01
gamma = 0.01
kernel = rbf

# Principal Component Analysis (PCA)

This folder documents my learning and practical implementation of **Principal Component Analysis (PCA)** as part of my Classical Machine Learning journey.

## What I Learned

Before learning PCA, I first understood:

- Why feature selection is required
- Feature Selection vs Feature Extraction
- Why dimensionality reduction is useful
- How PCA transforms the original features into principal components
- The importance of variance in PCA
- Explained Variance
- How to select an appropriate number of principal components

## Practical Experiment

I applied PCA to a **Digit Classification dataset** and used **K-Nearest Neighbors (KNN)** to compare model performance before and after dimensionality reduction.

### Experiment

| Approach | Accuracy |
|---|---:|
| KNN without PCA | 93% |
| PCA with all components | 96% |
| PCA with 100 components | 96% |

This experiment helped me understand that dimensionality reduction can reduce the number of features while retaining useful information for the machine learning model.

## Explained Variance

I also explored **Explained Variance** to understand how much information is retained by different numbers of principal components.

This helped me understand how an appropriate value of `n_components` can be selected instead of choosing the number of components arbitrarily.

## Key Learning

The main concepts I understood through this experiment were:

- PCA is a **feature extraction** technique.
- PCA creates new principal components from the original features.
- Principal components capture maximum variance in decreasing order.
- Scaling is important before applying PCA when features are on different scales.
- Explained variance helps determine how many components should be retained.
- PCA can reduce dimensionality while preserving useful information.

## Kaggle Notebook

The complete practical implementation and experiment are available on Kaggle:

👉 **[View the PCA Kaggle Notebook](https://www.kaggle.com/code/pranjaliyewale/pca-demo/edit)**

## Status

✅ PCA completed as part of my Classical Machine Learning learning journey.

Next focus: **Real-world ML case studies, model evaluation, and problem-solving.**
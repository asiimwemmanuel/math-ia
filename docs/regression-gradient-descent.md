### Gradient Descent for Polynomial Regression

**Objective:** Iteratively find the coefficients \(\beta_j\) that minimize the Mean Squared Error (MSE) to reduce the error between predicted and actual values.

**Polynomial of degree \(d\):**

\[
\hat{y} = \sum_{j=0}^d \beta_j x^j
\]

**MSE for dataset \(\{(x_i, y_i)\}_{i=1}^n\):**

\[
\text{MSE}(\boldsymbol{\beta}) = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \frac{1}{n} \sum_{i=1}^n \left(y_i - \sum_{j=0}^d \beta_j x_i^j \right)^2
\]

### Gradient Calculation

To minimize MSE, compute the gradient with respect to each \(\beta_j\):

\[
\frac{\partial \text{MSE}}{\partial \beta_j} = -\frac{2}{n} \sum_{i=1}^n \left( y_i - \hat{y}_i \right) x_i^j
\]

### Gradient Descent Update Rule

Update \(\beta_j\) iteratively using the learning rate \(\alpha\):

\[
\beta_j := \beta_j + \frac{2 \alpha}{n} \sum_{i=1}^n \left( y_i - \hat{y}_i \right) x_i^j
\]

### Summary

1. **Compute Gradient:** 
   \[
   \frac{\partial \text{MSE}}{\partial \beta_j} = -\frac{2}{n} \sum_{i=1}^n \left( y_i - \hat{y}_i \right) x_i^j
   \]
2. **Update Coefficients:** 
   \[
   \beta_j := \beta_j + \frac{2 \alpha}{n} \sum_{i=1}^n \left( y_i - \hat{y}_i \right) x_i^j
   \]

Repeat until the change in MSE is below a threshold or a maximum number of iterations is reached.
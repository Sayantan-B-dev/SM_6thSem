# Linear Regression

## 1. Definition

Linear regression is a supervised machine learning algorithm used for predicting a continuous numeric output. It models the relationship between one or more input features (independent variables) and the target (dependent variable) by fitting a straight line – or a hyperplane in higher dimensions – to the training data. The objective is to find the line that minimises the sum of squared differences between the predicted and actual values.

## 2. Concept Explanation

The core idea of linear regression is simple: we assume that the output \( y \) can be expressed as a linear combination of the input features \( x \). For a single feature, this is the familiar equation of a straight line: \( y = mx + b \). For multiple features, it becomes a plane or hyperplane.

How does it work? The algorithm starts with random values for the coefficients (weights and bias) and then repeatedly adjusts them to reduce the error on the training data. The most common method is **ordinary least squares**, which selects coefficients that minimise the residual sum of squares – the squared vertical distance between each data point and the fitted line.

Why use it? Linear regression is the foundation of many advanced techniques. It is highly interpretable, trains almost instantly, and provides a baseline before trying more complex models. It answers questions like “How much does the price of a house increase per additional square meter?” and is widely used in economics, finance, engineering, and data science for forecasting and causal inference.

## 3. Key Characteristics / Features

- **Linearity assumption:** The relationship between the input features and the output is assumed to be approximately linear. If this assumption is violated, the model performs poorly.
- **Interpretability:** Each weight directly tells you the expected change in the target when the corresponding feature increases by one unit, holding others constant. This makes the model easy to explain.
- **Analytic solution:** Ordinary least squares can be solved directly using the normal equation, without iterative optimisation. For very large datasets, gradient descent is used instead.
- **Fast training and prediction:** Both the closed‑form solution and mini‑batch gradient descent are computationally efficient, even on modest hardware.
- **Sensitive to outliers:** A single data point far from the main trend can drastically shift the regression line because the squared error penalty is large.
- **Variance explained:** Metrics like \( R^2 \) quantify how much of the variability in the target is captured by the model, providing a clear goodness‑of‑fit measure.

## 4. Types / Classification

Linear regression can be classified based on the number of predictor variables.

- **Simple linear regression:** One input feature and one output variable. The model is \( y = \theta_0 + \theta_1 x \). It is used when exploring the effect of a single factor, such as advertising spend on sales.
- **Multiple linear regression:** Two or more input features. The model is \( y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n \). This is the standard tool for most real‑world regression problems, like predicting house prices from area, bedrooms, and location.

Note: Polynomial regression with degree \( d \) can be viewed as multiple linear regression on transformed features (\( x, x^2, \dots, x^d \)), but it is still a linear model in terms of the parameters.

## 5. Working / Mechanism

The typical workflow of a linear regression model is as follows.

1.  **Collect and prepare the data:** Gather numerical features and the target variable. Clean missing values and scale features if using regularisation.
2.  **Define the hypothesis function:** Choose \( h_\theta(x) = \theta^T x = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n \). A constant feature \( x_0 = 1 \) is added to absorb the bias term \( \theta_0 \).
3.  **Select a cost (loss) function:** The mean squared error (MSE) is almost universally used:
    $$ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2 $$
    where \( m \) is the number of training examples.
4.  **Optimise the parameters:** Find the values of \( \theta \) that minimise \( J(\theta) \). One of two methods is used:
    * **Normal equation:** \( \theta = (X^T X)^{-1} X^T y \). This gives an exact solution but becomes slow when the number of features is very large.
    * **Gradient descent:** Iteratively update each \( \theta_j \) by moving in the direction of the negative gradient:
      $$ \theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j} $$
      The learning rate \( \alpha \) controls the step size. This scales to very large datasets.
5.  **Evaluate the model:** Use metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and \( R^2 \) score on a held‑out test set.
6.  **Make predictions:** For new data \( x_{new} \), compute \( \hat{y} = \theta^T x_{new} \).

## 6. Diagram

```mermaid
graph TD
A[Dataset with Features X and Target y] --> B[Split into Train & Test sets]
B --> C[Define linear hypothesis: hθ(x)=θᵀx]
C --> D[Initialize parameters θ randomly]
D --> E[Compute cost J(θ) = (1/2m) Σ(hθ(x) - y)²]
E --> F[Update θ using gradient descent or solve normal equation]
F --> G[Repeat until convergence]
G --> H[Trained model with final θ]
H --> I[Predict on test data]
I --> J[Evaluate with RMSE and R²]
```

## 7. Mathematical Formulation

The linear regression model:

$$
\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
$$

In matrix form, for \( m \) examples:

$$
\hat{Y} = X \theta
$$

Where:
- \( X \) is the \( m \times (n+1) \) matrix of input features (including a column of ones for the bias term).
- \( \theta \) is the \( (n+1) \times 1 \) parameter vector (weights and bias).
- \( \hat{Y} \) is the vector of predicted values.

**Cost function (MSE):**

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2
$$

**Gradient of the cost function (for one parameter \( \theta_j \)):**

$$
\frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) \, x_j^{(i)}
$$

**Normal equation:**

$$
\theta = (X^T X)^{-1} X^T Y
$$

The term \( (X^T X)^{-1} \) exists only when the columns of \( X \) are linearly independent (no perfect multicollinearity).

## 8. Example

A civil engineer wants to predict the compressive strength of concrete based on its cement content (kg/m³). She collects data from 200 tested specimens. Using simple linear regression, she fits the model:

$$ \text{strength} = -18 + 0.076 \times \text{cement} $$

Interpretation: For every additional kilogram of cement per cubic metre, the predicted strength increases by 0.076 MPa. She evaluates the model on a test set and obtains an \( R^2 \) of 0.82, meaning 82% of the variance in compressive strength is explained by the cement content alone. She can now quickly estimate strength for a new mix design without waiting for a laboratory test.

## 9. Analogy

Fitting a linear regression model is like balancing a straight rod on a group of differently sized stones. The rod (regression line) is adjusted until it is as close as possible to all the stones (data points). The distance between each stone and the rod is the error. The final position of the rod gives you the best single straight summary of the trend in the stones’ heights.

## 10. Comparison

| Feature          | Linear Regression                         | Logistic Regression                       |
| ---------------- | ----------------------------------------- | ----------------------------------------- |
| Meaning          | Predicts continuous numeric values        | Predicts probability of a binary class    |
| Output           | Any real number (e.g., 150.2)             | A probability between 0 and 1             |
| Underlying model | Linear function \( y = \theta^T x \)      | Sigmoid applied to a linear function      |
| Loss function    | Mean Squared Error (MSE)                  | Log loss (cross‑entropy)                  |
| Use case         | House price prediction, sales forecasting | Spam detection, disease diagnosis         |

## 11. Advantages

- **Simple and interpretable:** The linear formula makes it easy to explain predictions to stakeholders.
- **Low computational cost:** Training, even on datasets with hundreds of thousands of examples, is fast.
- **No hyperparameter tuning:** Basic linear regression has no hyperparameters beyond feature engineering; it works out‑of‑the‑box as a baseline.
- **Works well with small datasets:** When data is scarce, a linear model often outperforms complex models that overfit.
- **Statistical inference:** P‑values and confidence intervals for coefficients can be derived, allowing hypothesis testing about relationships.
- **Easily extended:** Regularisation (Ridge, Lasso) can be added to prevent overfitting without changing the core concept.

## 12. Disadvantages / Limitations

- **Assumes linearity:** If the true relationship is highly non‑linear, performance drops sharply unless polynomial or interaction terms are manually added.
- **Sensitive to outliers:** A few extreme points can distort the line significantly, leading to poor generalisation.
- **Multicollinearity problems:** Highly correlated features make the coefficients unstable and hard to interpret; the normal equation may become ill‑conditioned.
- **Requires independent features:** The model assumes observations are independent; it is not suitable for time series with autocorrelation without modifications.
- **Homoscedasticity assumption:** The variance of errors is assumed constant. When this fails, predictions may be less reliable at certain ranges.
- **No built‑in feature selection:** Irrelevant or redundant features reduce model performance unless regularisation or manual selection is used.

## 13. Important Points / Exam Notes

- Linear regression is a **supervised learning algorithm** for **regression**.
- The hypothesis function: \( h_\theta(x) = \theta^T x \).
- Mean Squared Error (MSE) is the standard cost function; the factor \( \frac{1}{2} \) simplifies the derivative.
- **Normal equation** provides a one‑shot solution but is computationally expensive for many features (time complexity \( O(n^3) \)).
- **Gradient descent** scales to large datasets; the learning rate \( \alpha \) must be chosen carefully to ensure convergence.
- \( R^2 \) (coefficient of determination) measures the proportion of variance explained; ranges from 0 to 1 (can be negative for very bad models).
- **Residual plots** (residuals vs. fitted values) should show no pattern if the linear model assumptions hold.
- Key assumptions: linearity, independence, homoscedasticity, normality of errors (important for small‑sample inference).
- **Regularisation:** L1 (Lasso) and L2 (Ridge) add penalty terms to the cost function to prevent overfitting and handle multicollinearity.
- In multiple linear regression, **adjusted \( R^2 \)** accounts for the number of predictors to penalise adding useless variables.

## 14. Applications / Use Cases

- **Real estate pricing:** Predict house sale prices from square footage, number of rooms, and location scores.
- **Finance:** Forecast a company’s revenue based on advertising spend across TV, radio, and online channels.
- **Energy sector:** Estimate daily electricity consumption of a building from temperature, humidity, and weekday‑weekend flags.
- **Healthcare:** Predict a patient’s blood pressure trend based on age, weight, and diet scores.
- **Automotive:** Estimate fuel consumption (km/litre) from engine size, vehicle weight, and driving cycle data.
- **Agriculture:** Model crop yield from rainfall, soil pH, and fertiliser quantity.

## 15. MCQs

**Q1. Linear regression is used when the target variable is**

A. Categorical  
B. Continuous  
C. Binary  
D. Always zero  

**Answer:** B  
**Explanation:** Linear regression predicts a continuous numeric output, unlike classification algorithms.

---

**Q2. Which cost function is most commonly minimised in ordinary least squares linear regression?**

A. Mean Absolute Error  
B. Mean Squared Error  
C. Cross‑entropy loss  
D. Hinge loss  

**Answer:** B  
**Explanation:** Ordinary least squares minimises the sum of squared residuals, i.e., the mean squared error.

---

**Q3. In the normal equation \( \theta = (X^T X)^{-1} X^T y \), what is the size of \( X^T X \)?**

A. \( m \times m \)  
B. \( n \times n \)  
C. \( m \times n \)  
D. \( n \times m \)

**Answer:** B  
**Explanation:** \( X \) is \( m \times (n+1) \), so \( X^T X \) becomes \( (n+1) \times (n+1) \), where \( n \) is the number of features.

---

**Q4. What does the learning rate \( \alpha \) control in gradient descent?**

A. The number of features used  
B. The size of each update step toward the minimum  
C. The intercept term of the model  
D. The number of training examples  

**Answer:** B  
**Explanation:** The learning rate scales the gradient update; a too‑large \( \alpha \) can cause divergence, and a too‑small \( \alpha \) slows convergence.

---

**Q5. If \( R^2 = 0.92 \) for a linear regression model, it means**

A. 92% of the data points lie on the regression line  
B. 92% of the variance in the target is explained by the inputs  
C. The error is 92% of the mean target value  
D. The model has 92% accuracy  

**Answer:** B  
**Explanation:** The coefficient of determination \( R^2 \) measures the proportion of variance captured by the model.

---

**Q6. Which assumption must be true for the normal equation to be directly solvable?**

A. Features must have zero mean  
B. \( X^T X \) must be invertible (no multicollinearity)  
C. The dataset must contain at least one categorical feature  
D. The target must be normally distributed  

**Answer:** B  
**Explanation:** If columns of \( X \) are linearly dependent, \( X^T X \) is singular and cannot be inverted.

---

**Q7. Simple linear regression differs from multiple linear regression by**

A. Using a sigmoid activation function  
B. Having only one input feature  
C. Using a different cost function  
D. Not requiring an intercept term  

**Answer:** B  
**Explanation:** Simple linear regression models a single independent variable, whereas multiple linear regression includes two or more.

---

**Q8. How does an outlier affect a linear regression model fit with ordinary least squares?**

A. It has no effect because squared errors ignore large residuals  
B. It can pull the regression line toward itself, distorting the fit  
C. It forces the model to use regularisation  
D. It automatically increases the learning rate  

**Answer:** B  
**Explanation:** Because the error is squared, a point with a very large residual contributes heavily to the cost, causing the line to shift toward it.

---

**Q9. In the context of linear regression, what is the purpose of adding polynomial features?**

A. To convert the problem into a classification task  
B. To capture non‑linear relationships while keeping the model linear in parameters  
C. To reduce the number of input variables  
D. To automatically remove outliers  

**Answer:** B  
**Explanation:** Transforming \( x \) to \( x^2, x^3 \), etc., allows a linear model to fit curves; it remains linear in the coefficients.

---

**Q10. When the error variance increases with the predicted value, which linear regression assumption is violated?**

A. Linearity  
B. Independence of errors  
C. Homoscedasticity (constant variance)  
D. Normality of errors  

**Answer:** C  
**Explanation:** Homoscedasticity requires the error variance to be constant across all levels of the independent variables. A funnel‑shaped residual plot indicates heteroscedasticity.
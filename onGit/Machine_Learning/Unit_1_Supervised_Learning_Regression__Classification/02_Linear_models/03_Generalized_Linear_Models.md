# Generalized Linear Models

## 1. Definition

A Generalized Linear Model (GLM) is a flexible generalization of ordinary linear regression that allows the target variable to have a non‑normal error distribution and relates the linear predictor to the mean of the response via a link function. In simple terms, GLMs extend linear regression so that we can predict counts, binary outcomes, or other non‑continuous quantities while keeping the model interpretation simple.

---

## 2. Concept Explanation

**Basic Idea:** Linear regression assumes the dependent variable is continuous and normally distributed, and its mean equals a linear combination of inputs. But real‑world data often violates these assumptions. For example, we might want to predict whether a customer will churn (yes/no), or how many products a customer buys (count). GLMs solve this by keeping the linear combination of features but adding two extra ingredients: a link function that transforms the mean so it matches the linear predictor, and a distribution from the exponential family (like Binomial, Poisson) that describes the randomness in the response.

**Why it is used:** GLMs provide a unified framework for many common predictive models. Instead of learning entirely different algorithms, the same principles of parameter estimation, inference, and diagnostics carry over. They are interpretable because the influence of each feature is additive on the transformed scale.

**Where it is applied:** In machine learning, GLMs are used for classification (logistic regression), regression with non‑negative integer counts (Poisson regression), modeling insurance claim severity (Gamma regression), and many other tasks where standard linear regression would fail.

---

## 3. Key Characteristics / Features

* **Three components:** Every GLM is built from a random component (probability distribution of the response), a systematic component (linear predictor, a linear combination of features), and a link function that connects them.
* **Exponential family:** The response variable belongs to the exponential family of distributions (Normal, Binomial, Poisson, Gamma, Inverse Gaussian, etc.), which gives convenient mathematical properties.
* **Flexible target types:** GLMs can model continuous, binary, count, proportion, and positive‑skewed data.
* **Interpretability:** The effect of a feature is captured by a coefficient, similar to linear regression, but interpreted on the transformed (link) scale. Odds ratios in logistic regression and rate ratios in Poisson regression are direct.
* **Maximum likelihood estimation:** Parameters (coefficients) are typically estimated by maximizing the likelihood of the observed data, solved via iterative reweighted least squares (IRLS).
* **Natural regularization extension:** Regularization (ridge, lasso) can be added easily to GLMs, leading to regularized logistic regression, Poisson lasso, etc.

---

## 4. Types / Classification

GLMs are classified based on the response distribution and the corresponding canonical link function. Common types include:

* **Linear regression (Gaussian family):** Response is continuous, follows Normal distribution. Link is the identity function \( \mu = \eta \). This is the ordinary linear model.
* **Logistic regression (Binomial family):** Response is binary or number of successes out of trials. Distribution is Binomial. Link is the logit function \( \log(\mu/(1-\mu)) \). Predicted probabilities are bounded between 0 and 1.
* **Poisson regression (Poisson family):** Response is a count (non‑negative integer). Link is the log function \( \log(\mu) \). Ensures predicted counts are positive.
* **Gamma regression (Gamma family):** Response is positive continuous with constant coefficient of variation (e.g., insurance claim amounts). Link is often inverse or log.
* **Inverse Gaussian regression:** Similar to Gamma but with different variance structure, used in reliability engineering.

---

## 5. Working / Mechanism

The process of using a GLM follows these steps:

1. **Define the response distribution:** Choose an appropriate exponential family distribution based on the target variable type (Binary → Binomial, Count → Poisson, Positive continuous → Gamma).
2. **Formulate the linear predictor:** Compute a linear combination of input features: \(\eta = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p\).
3. **Apply the link function:** Transform the mean of the response \(\mu = E[Y]\) using a chosen link function \(g\) for which \(g(\mu) = \eta\). This ensures the predicted mean lies in the correct range.
4. **Estimate coefficients via maximum likelihood:** The coefficients \(\beta\) are found by maximizing the likelihood of the observed responses, using algorithms like Iteratively Reweighted Least Squares (IRLS) or gradient‑based optimization.
5. **Make predictions:** For new data, compute the linear predictor \(\eta\) using the estimated coefficients, then apply the inverse link function to obtain the predicted mean \(\hat{\mu} = g^{-1}(\eta)\). For binary outcomes, this mean is the predicted probability.
6. **Interpret results:** Coefficients reflect the change in the transformed mean. For logistic regression, exponentiating the coefficient gives an odds ratio.

---

## 6. Diagram

```mermaid
graph TD
    A[Input Features X] --> B[Linear Predictor: η = Xβ]
    B --> C[Link Function: g(μ) = η]
    C --> D[Response Distribution]
    D --> E[Output: Predicted Mean / Probability]
```

*Explanation:* The linear predictor is computed from inputs. It is transformed via the link function to the scale of the response distribution, which then produces predictions.

---

## 7. Mathematical Formulation

A GLM is fully defined by specifying:

* Random component: \(Y \sim \text{Exponential Family}(\mu, \phi)\), where \(\mu = E[Y]\) and \(\phi\) is a dispersion parameter.
* Systematic component: \(\eta = X\beta\), a linear combination of features.
* Link function: \(g(\mu) = \eta\).

For the most common binary logistic regression:

* Distribution: \(Y \sim \text{Bernoulli}(p)\), \(p = \mu\).
* Link: logit, \(\eta = \log\left(\frac{p}{1-p}\right)\).
* Inverse link: \(p = \frac{1}{1+e^{-\eta}}\).

For Poisson regression:

* Distribution: \(Y \sim \text{Poisson}(\mu)\).
* Link: log, \(\eta = \log(\mu)\).
* Inverse link: \(\mu = e^{\eta}\).

The coefficients are estimated by maximizing the log‑likelihood:

$$
\ell(\beta) = \sum_{i=1}^{n} \log f(y_i; \mu_i, \phi)
$$

where \(\mu_i = g^{-1}(X_i\beta)\). This is solved via IRLS, which iteratively fits a weighted linear regression.

---

## 8. Example

**Predicting hospital length of stay (count data):** Suppose we want to predict the number of days a patient stays based on age, diagnosis severity, and treatment type. Length of stay is a count, typically skewed. We use a Poisson regression GLM with a log link. The linear predictor is:

\(\eta = \beta_0 + \beta_1 \times \text{Age} + \beta_2 \times \text{SeverityScore}\).

The predicted mean stay is \(\hat{\mu} = e^{\eta}\). If \(\beta_1 = 0.02\), then a one‑year increase in age multiplies the expected stay by \(e^{0.02} \approx 1.02\), a 2% increase, assuming other factors constant.

For binary classification: Predicting email spam. We use logistic regression (Binomial family, logit link). The predicted probability of spam is \(\hat{p} = 1/(1+e^{-X\beta})\).

---

## 9. Analogy

Think of a GLM as a **multilingual interpreter**. You speak a universal language (the linear combination of features). The interpreter (link function) translates your universal message into the specific language the response understands (the distribution). For a binary response, the interpreter ensures the message is a probability between 0 and 1. For a count response, the interpreter ensures the answer is a positive number.

---

## 10. Comparison (if needed)

| Feature          | Ordinary Linear Regression               | Generalized Linear Model                       |
| ---------------- | ---------------------------------------- | ---------------------------------------------- |
| Target distribution | Normal (continuous, unbounded)        | Any exponential family (Binomial, Poisson, Gamma, etc.) |
| Mean–linear relation | \(\mu = X\beta\) (identity)           | \(g(\mu) = X\beta\) (link function)            |
| Variance structure | Constant variance                     | Variance can be a function of the mean (e.g., Poisson: var = μ) |
| Estimation       | Ordinary least squares                 | Maximum likelihood (IRLS)                      |
| Prediction range | Unlimited real values                  | Correct range (e.g., [0,1], positive)       |

---

## 11. Advantages

* **Unified framework:** One methodology covers many types of predictive modeling tasks; the same theoretical properties apply.
* **Interpretability:** Coefficients have clear interpretations on the transformed scale (odds ratios, rate ratios).
* **Well‑studied inference:** Statistical inference (confidence intervals, p‑values) is mature, unlike many black‑box models.
* **Natural for non‑normal data:** Avoids the pitfalls of applying linear regression to skewed, binary, or count data.
* **Can handle heteroscedasticity:** Because variance depends on the mean, GLMs directly model the variance structure.
* **Easy to regularize:** Lasso and ridge penalties can be added to prevent overfitting and perform feature selection.

---

## 12. Disadvantages / Limitations

* **Requires correct distribution choice:** If the chosen distribution poorly matches the data, model fit and predictions suffer.
* **Assumes independence:** Standard GLMs assume observations are independent; correlated data require extensions like mixed models.
* **Linearity in the transformed predictor:** The relationship on the link scale is linear; complex interactions or nonlinearities must be manually engineered.
* **Sensitive to outliers:** Outliers can heavily influence maximum likelihood estimates.
* **Iterative fitting:** Estimation (IRLS) may not converge for ill‑conditioned data.
* **Not as expressive as deep learning:** GLMs cannot learn hierarchical features or complex non‑linear patterns without manual feature transformation.

---

## 13. Important Points / Exam Notes

* **GLM = Linear Predictor + Link Function + Exponential Family.** 
* **Common GLMs:** Linear regression (Normal, identity), Logistic regression (Binomial, logit), Poisson regression (Poisson, log), Gamma regression (Gamma, inverse/log).
* **Link function** connects the mean to the linear predictor: \(g(\mu) = X\beta\).
* **Inverse link** gives predicted mean: \(\hat{\mu} = g^{-1}(X\hat{\beta})\).
* **Maximum likelihood** estimates are found using IRLS.
* **Interpretation** uses log‑odds ratio (logistic), rate ratio (Poisson).
* **GLMs are the foundation** of many advanced models; they bridge classical statistics and modern ML.

---

## 14. Applications / Use Cases

* **Credit scoring:** Logistic regression (Binary) predicts probability of default based on applicant information.
* **Insurance pricing:** Poisson or Gamma regression models claim frequency and severity; the results inform premium setting.
* **E‑commerce conversion prediction:** Predicting purchase probability (Binomial) from user clickstream data.
* **Public health:** Modeling disease counts per region (Poisson) to identify outbreaks.
* **Manufacturing:** Predicting number of defects per batch (Poisson) based on process parameters.
* **Marketing:** Analyzing A/B test results with logistic regression to estimate conversion uplift.

---

## 15. MCQs

**Q1. Which component is NOT part of a Generalized Linear Model?**

A. Link function  
B. Response distribution from the exponential family  
C. Linear predictor  
D. Hidden layer with activation function  

**Answer:** D  
**Explanation:** GLMs have three components: random (exponential family), systematic (linear predictor), and link function. Hidden layers are part of neural networks.

---

**Q2. In logistic regression, the link function most commonly used is:**

A. Identity  
B. Log  
C. Logit  
D. Inverse  

**Answer:** C  
**Explanation:** Logistic regression uses the logit link: \(\log(p/(1-p))\). Identity is for linear regression, log for Poisson, inverse for Gamma.

---

**Q3. For Poisson regression, the canonical link function is:**

A. Log  
B. Logit  
C. Power  
D. Reciprocal  

**Answer:** A  
**Explanation:** The canonical link for the Poisson family is the natural logarithm. It ensures predicted counts are positive.

---

**Q4. The parameters of a GLM are estimated by:**

A. Minimizing sum of squared errors  
B. Maximum likelihood estimation (MLE)  
C. Minimizing Gini impurity  
D. Backpropagation  

**Answer:** B  
**Explanation:** GLM coefficients are found by maximizing the likelihood, often via IRLS. Least squares is a special case for Normal distribution.

---

**Q5. Which statement about GLMs is TRUE?**

A. They can only handle normally distributed responses.  
B. They require feature scaling to converge.  
C. They can model responses with non‑constant variance.  
D. They always use identity link function.  

**Answer:** C  
**Explanation:** GLMs allow variance to be a function of the mean (e.g., Poisson). They do not require scaling for estimation and can use many link functions.

---

**Q6. The predicted probability in logistic regression is obtained by:**

A. \( \hat{p} = X\beta \)  
B. \( \hat{p} = e^{X\beta} \)  
C. \( \hat{p} = \frac{1}{1 + e^{-X\beta}} \)  
D. \( \hat{p} = \log(X\beta) \)  

**Answer:** C  
**Explanation:** The inverse of the logit function is the logistic sigmoid function: \(1/(1+e^{-\eta})\).

---

**Q7. A GLM is most suitable for predicting the number of customer service calls per day. Which family and link would be appropriate?**

A. Gaussian, identity  
B. Poisson, log  
C. Binomial, logit  
D. Gamma, inverse  

**Answer:** B  
**Explanation:** Number of calls is count data, non‑negative integers, often modeled with Poisson. The log link ensures positive predictions.

---

**Q8. What is the role of the link function in a GLM?**

A. It converts the response variable into a linear scale.  
B. It connects the mean of the response to the linear predictor.  
C. It determines the variance of the response.  
D. It normalizes the features.  

**Answer:** B  
**Explanation:** The link function \(g\) satisfies \(g(\mu) = \eta\), linking the expected value of the response to the linear combination of predictors.

---

**Q9. Which of the following is an advantage of GLMs over tree‑based methods?**

A. Automatic feature interaction detection.  
B. Higher interpretability of individual feature effects.  
C. Better performance on image data.  
D. No need for hyperparameter tuning.  

**Answer:** B  
**Explanation:** GLMs provide clear coefficients and odds/rate ratios, making the effect of each feature easy to understand. Trees capture interactions but are less straightforward.

---

**Q10. In a Poisson GLM with log link, a coefficient of 0.5 for feature X means:**

A. A one‑unit increase in X multiplies the expected count by \(e^{0.5} \approx 1.65\).  
B. A one‑unit increase in X increases the count by 0.5.  
C. the probability of success increases by 0.5.  
D. The model is linear in the original scale.  

**Answer:** A  
**Explanation:** With a log link, the effect is multiplicative. Expected count changes by a factor of \(e^{\beta}\). So, \(e^{0.5} \approx 1.65\), about a 65% increase.
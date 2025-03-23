---
title: Statistics
icon: file
order: 5
author: Doris
category:
  - Fin
tags:
  - Fin
footer: What is the meaning of data?
copyright: 无版权
date: 2024-08-01
---
1. Regression: OLS, GLM, logistic, and etc.
2. Time-series : ARIMA, GARCH, ECM
3. Nonparametric Regression: Splines, Kernel, Locally Weighted Regression
4. Data exploration: Density, estimation, normality, tests, monte carlo copulas
5. Data Cleaning and reduction: Cluster analysis, and stats theory

# 1 Regression

## 1.1 Linear models

1. linear model: coeffiecients $\beta$ are linear.

### 1.1.2 Simple linear regression(SLR)

$$
y = \beta_0+\beta_1x+\epsilon_i
$$

where

- $\beta_0\text{ population intercept },\beta_1 \text{ population slope }$ are fixed but unknown. Estimated by $b_0\text{ and } b_1$ (whether using maximum likelihood or OLS, same result). $\beta_1$ means the amount of change in $E(y)$ when one unit change in x.
- $(x_i, y_i)$ is a pair of data, plug in the formula: $y_i = \beta_0+\beta_1x_i+\epsilon_i$ . The only variable in this
  formula is $\epsilon_i$.
- $\epsilon$ is the model error, which follows the normal theory $\epsilon_i \sim N(0,\sigma^2)$.
  - It is iid(independent identically distributed). $cov(\epsilon_i,\epsilon_j)=0, \text{for i} \neq j$.
  - Homogeneous variance assumption $var(\epsilon_i)=\sigma^2$. (note: the unbiased estimator of $\sigma$ is $s$)

    $$
    s^2=\dfrac{1}{n-2}\sum\limits_{i=1}^{n}(y_i-\hat{y_i})^2
    $$

    **Some inferences**:

1. $E(a)=a$. $E(\epsilon_i)=0$
   $$
   E(y_i)=E(\beta_0+\beta_1+\epsilon_i)=E(\beta_0+\beta_1x_i)+E(\epsilon_i)=\beta_0+\beta_1x_i
   $$
2. $var(a)=0$
   $$
   var(y_i)=var(\beta_0+\beta_1+\epsilon_i)=var(\beta_0+\beta_1x_i)+var(\epsilon_i)=\sigma^2
   $$

### 1.1.3 Multiple linear regression (MLR)

$$
\hat{y}=X\hat{\beta}+\hat{\epsilon}
$$

### 1.1.4 Ordinary least squares (OLS)

1. A method to estimate unknown paras$\beta$. in a linear regression model.
2. It can be used in SLR & MLR (>1 regressor).

##### In SLR, 2 paras $\beta_0, \beta_1$, and their estimators are $b_0, b_1$. Use OLS:

$$
min J(b_0, b_1) = min SSE=min\sum\limits_{i=1}^{n}[y_i - \hat{y_i}]^2=min\sum\limits_{i=1}^{n}[y_i - b_0 -b_1x_i]^2
$$

Use partial derivatives, tl.hen get 2 estimators:

$$
b_0 = \bar{y} - b_1\bar{x}
$$

$$
b_1=\dfrac{n\bar{x}\bar{y}-\sum\limits_{i=1}^{n}x_iy_i}{n\bar{x}^2-\sum\limits_{i=1}^{n}x_i^2}
=\dfrac{\sum\limits_{i=1}^{n}(x_i-\bar{x})y_i}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}
=\dfrac{\sum\limits_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}
=\dfrac{S_\text{xy}}{S_\text{xx}}
$$

Because

$$
E(b_0)=\beta_0
$$

$$
E(b_1)=\beta_1
$$

$b_0, b_1$ are unbiased estimators.

$$
var(b_1)= \dfrac{\sigma^2}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}
$$

$$
var(b_0)=\sigma^2(\dfrac{1}{n}+\dfrac{\bar{x}^2}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2})
$$

$$
cov(b_0,b_1) = -\dfrac{\bar{x}\sigma^2}{S_\text{xx}}
$$

### 1.1.5 Analysis of variance (ANOVA)

1. partition of digree of freedom for SLR.
   equation:  $y = \beta_0 + \beta_1x$
   - k = 2 for($\beta_0,\beta_1$)
   - n sample size

![[df.png]]

2. Regression hypothesis

   $$
   H_0: \beta_1=0
   $$

   $$
   H_1: \beta_1\neq0
   $$

   - $H_0 \text{ No regression relationship exists.}$
   - $H_1 \text{ Regression analyasis exists.}$
     Then do ==F-test==: test for the entire regression. Is the reg statistically significant?

     $$
     F_\text{k-1, n-k}=\dfrac{MSR}{MSE}=\dfrac{\frac{SSR}{k-1}}{\frac{SSE}{n-k}}
     $$

     where
   - k-1: df for reg
   - n-k: df for error
     **Conclusion**: Reject $H_0$ if $F_\text{CALC}>F_\text{CV}$ . Regression analysis exists.
     Note: F value can be used for ranking the importance of features. The bigger the F for a feature, the bigger the
     SSR, in favor of $H_1$.
3. Hypothesis for $\beta_1$

   $$
   H_0: \beta_1=0
   $$

   $$
   H_1: \beta_1\neq0
   $$

   - $H_0 \text{ x has no impact on y.} E(y)=\beta_0$
     ==t-test== is a test for only $\beta_1$. Is there an evidence that x contributes information in the prediction of
     y?

     $$
     t_\text{n-k}=\dfrac{b_1}{\frac{\sqrt{MSE}}{\sqrt{\sum(x-\bar{x})^2}}}
     $$

     **Conclusion**: Reject $H_0$ if $t_\text{CALC}>t_\text{CV}$. x has impact on y.
4. $R^2$ coefficient of determinate

   $$
   R^2=\dfrac{SSR}{SST}=\dfrac{\sum\limits_{i=1}^{n}(\hat{y_i}-\bar{y})^2}{\sum\limits_{i=1}^{n}(y_i-\bar{y})
   ^2}=1-\dfrac{SSE}{SST}
   $$

   - $0<R^2<1$
   - $R^2$ means the proportion of variation in the response data that is explained by the **model**.
   - $R^2$ on its own cannot tell you anything about causation. (causaion means that a change in one variable causes a
     change in another variable. correlation: there is a statistical association between variables)

## 1.2 Generalized linear models (GLM)

The differences between linear models and GLM.
**Standard linear model**:

- systematic component:
  $$
  y = \beta_0+\beta_1x+\epsilon_i
  $$
- Link function is one. $\mu_i=x_i^T\beta$.
- Random component: normal distribution $y_i \sim N(\mu_i,\sigma^2)$ residuals are normally distributed.
- Estimators: least squares or maximum likelihood will give the same result
  Not all situation can be considered as a normal distribution, large error.

**GLM**:

- systematic component:

  $$
  y = \beta_0+\beta_1x+\epsilon_i
  $$
- Link function is a function that delinearize the mathematical relationship between the predictors and the outcome. $g(\mu_i)=x_i^T\beta$ . The link function transforms the prediction part, everything except for the $\epsilon.$ You need
  to decide this when doing analysis.
- Random component: Residuals ars not normal, it might be comes from a poisson, a binomial, a gamma.
- have to use maximum likelihood

  ![[Pasted image 20240803223049.png]]
  [1] Types of GLM.

two tpyes of varia: binomial.
skewed, positive discrete distribution: poisson. # times you go to a doctor.
skewed, positive continuous dist: gamma

# 2 Time series

## 2.1 Time series data

1. assumption: observations at a certain point depend on previous observations in time.
   decomposition:
   **Time** **series** = **signal**(forecasts extraplolate signal portion of model; trend/cycle and seasonal)
   +**noise** (confidence intervals account for uncertainty; error/remainder/irregular)
   - trend: classical: MA, morden way:
   - LOESS locally estimated scatterplot smoothing:non-parametric regression method that combines multiple regression
     models in a k-nearest-neighbor-based meta-model. This technique is used to fit a smooth curve through points in a
     scatterplot, especially when dealing with noisy data.
     Steps:
     - **Choose a point of interest**.
     - **Identify the neighborhood** around this point (based on the span).
     - **Fit a weighted least squares regression** to the points in the neighborhood.
     - **Predict the value** at the point of interest using the local regression model.
     - **Repeat** the process for all points in the dataset.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Example data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.5, 100)

# Apply LOESS
smoothed = lowess(y, x, frac=0.2)  # frac is the span

# Plotting
plt.scatter(x, y, label='Data')
plt.plot(smoothed[:, 0], smoothed[:, 1], color='red', label='LOESS Smoothed')
plt.legend()
plt.show()
```

### 2.2 Models for time series

![[Pasted image 20240805144951.png]]
[4]

1. Exponential smoothing models
   Apply a weighting scheme that decreases exponentially the further back in time we go. The larger the theta, the more
   recent observation is emphasized.

   $$
   \hat{Y}_\text{t+1}=\theta Y_t+\theta(1-\theta)Y_\text{t-1}+\theta(1-\theta)^2Y_\text{t-2}+\theta(1-\theta)^3Y_
   \text{t-3}+...
   $$

   $$
   0\le\theta\le1
   $$

   Simplify it, its prediction is like a horizontal line. So add trend and season terms in it. Holt winters exponential
   smoothing forecast:

   $$
   \hat{Y}_\text{t+k}=L_t+kT_t+S_\text{t-p+k}
   $$

   $$
   L_t=\theta Y_t + (1-\theta)L_\text{t-1}
   $$

   $$
   T_t=\gamma(L_t-L_\text{t-1})+(1-\gamma)T_\text{t-1}
   $$

   $$
   S_t=\delta(Y_t-L_t)+(1-\delta)S_\text{t-p}
   $$
2. consistency of distribution: can't have independece, but still want some consistency. Distribution depends only on
   difference in time, not location in time. same width(any size) of time, same distribution-strong stationarity.
   mean, var, autocorrelation depends only on difference in time-weak stationarity.
   Strong stationarity does not imply the weak one. Weak needs finite variance, strong does not.
3. **weak stationarity helps build stationary classes of models: MA...ARIMA**
   not sationary: no consistent mean and var.
   4.1 shifts in mean(not stationary):
   ![[Pasted image 20240804145903.png]]
   [4]
   common solution: differencing:

   - trend: look at the difference between the current point and previous one $Y_t-Y_\text{t-1}$
   - season: look at the difference between the current point and the same point in the previous season $Y_t-Y_\text{t-S}$
     4.2 shifts in variance:
   - ignore when most models only model the mean
   - model the lack of consistency in var: ARCH/GARCH
4. autoregressive models

   - forecast a series based on the past values in the series-lagsAR(1)

     $$
     Y_t = \omega + \phi Y_\text{t-1}+e_t
     $$

     target $Y_t$ , Lagged Target $Y_\text{t-1}$, $e_t$ error.

   The recursion in time goes back until the beginngn of the series-long memory models. if $|\phi|<1$ shocks happens long
   ago has little effect at the present.

   You can also has n lags AR(n).
5. Moving average model. Forecast a series based solely on the past errors-error lags. short memory models

   $$
   Y_t = \omega + \theta e_\text{t-1} + e_t
   $$

![[Pasted image 20240804224532.png]]

MA(n)

$$
Y_\text{t-1} = \omega + \theta e_\text{t-2} + e_\text{t-1}
$$

$$
Y_\text{t} = \omega + \theta e_\text{t-1} + e_\text{t}
$$

$$
Y_\text{t+1} = \omega + \theta e_\text{t} + e_\text{t+1}
$$

No more $e_\text{t-1}$

6. ARIMA

   1. ARIMA
      first, make your data stationary (typically done throug differencing).
      Distribution depends only on difference in time.
      AR, integrated, MA.

      $$
      Y_t=\omega+\phi_1Y_\text{t-1}+...+\phi_pY_\text{t-p}+\theta_1e_\text{t-1}+...+\theta_qe_\text{t-q}+e_t
      $$

      Deciding how many p's and q's. 2 techniques:

      - Plotting patterns in correlation
      - Automatic selection techniques: MINIC, SCAN, ESACF

      ARIMA(d,p,q)=ARIMA(#ARterms, # first differences, # Aterms)

      $$
      ARIMA(1,1,1)
      $$

      $$
      Y_t-Y_\text{t-1}=W_t
      $$

      $$
      W_t=\omega+\phi_1W_\text{t-1}+\theta_1e_\text{t-1}+e_t
      $$
   2. seasonal ARIMA: when data are not stationary.
      ARIMA(p,d,q)(P,D,Q)s

      - P: # seasonal AR terms
      - D: # seasonal differences
      - Q: # seasonal MA terms
      - s: length of season

      $$
      ARIMA(1,0,1)(2,1,0)_\text{12}
      $$

      $$
      Y_t-Y_\text{t-12}=W_t
      $$

      $$
      W_t=\omega+\phi_1W_\text{t-1}+\phi_2W_\text{t-12}+\phi_3W_\text{t-24}+\theta_1e_\text{t-1}+e_t
      $$
7. Neural network time series models
   input: # Number of autoregressive lags(AR lags): explore with correlation plots or aotomatic selection tecniques.
   seasonal data: typically include all lags up through one season unless correlation plots say you only need specific
   ones.
   STILL WANT TO MAKE DATA STATIONARY FIRST.
8. Prophet model
   **Time series** = **signal**(forecasts extraplolate signal portion of model; trend/cycle, seasonal, holiday)
   +**noise** (confidence intervals account for uncertainty; error/remainder/irregular)

   1. trend lines with knots, logorithm trend...
   2. seasonal: fourier transformation
   3. holiday-point(pulse) intervention
9. Vector autoregressive (VAR) model:

   1. model multiple time series at one time.
   2. multivariate regression is not multiple regression
   3. trying to predict multiple target variable at the same time
   4. when estimating 1 target variable, common: ARMA>AR
   5. when .... multiple ... , common: VAR > VARMA
      ![[Pasted image 20240805151510.png]]
      [5]
10. Bayesian autoregressive models

    $$
    Y_t=\alpha_0+\alpha_1Y_\text{t-1}+...+\alpha_pY_\text{t-q}+e_t
    $$
11. ARCH, GARCH

    1. unconditional variance

       $$
       Var(x)=\sigma^2=\dfrac{1}{n-1}\sum\limits_{i=1}^{n}(x_i-\bar{x}^2)=E(x-E(x))^2
       $$
    2. conditional variance: the measure of uncertainty about a variable given a set of information
       Heteroscedasticity-variance depends on external factors.(variance are changing)

       $$
       Var(x|I)=\sigma_\text{cond}^2=E(x-E(x|I))^2
       $$

       In cross-sectional data, heteroscedasticity: avoid
       In time series data especially in finance: we desire to model it. 建模return 更有规律。
    3. Autoregressive conditional heteroscedasticity. Trying to account for time dependency and "clustering" of
       volatility.
       Volatility tommorow: $\sigma_\text{t+1}^2$
       Actual today: $r_t^2$

       $$
       \sigma_\text{t+1}^2=\alpha_0+\alpha_1r_t^2
       $$

       why? Use squared returns to estimate a daily volatility:

       $$
       \sigma_\text{t}^2=\frac{1}{t}\sum\limits_{i=1}^{t}(r_t-\bar{r})^2
       =\frac{1}{t}\sum\limits_{i=1}^{t}(r_t-0)^2
       =\frac{1}{1}\sum\limits_{i=1}^{t}(r_t)^2
       =r_t^2
       $$

       - volatility tomorrow: $\sigma_\text{t+1}^2$
       - actual today: $\alpha_1r_t^2$
         ARCH(n) uses multiple lags in the past to model the volatility.
    4. generalized ARCH (GARCH).

       $$
       \sigma_\text{t+1}^2=\alpha_0+\alpha_1r_t^2+\beta_1\hat{\sigma_t}^2
       $$

       - volatility tomorrow: $\sigma_\text{t+1}^2$
         Real world data typically needs one of each:
       - actual today: $\alpha_1r_t^2$
       - forecasted today:$\beta_1\hat{\sigma_t}^2$
12. ECM
    An**error correction model**(**ECM**) belongs to a category of multiple [time series](https://en.wikipedia.org/wiki/Time_series "Time series")models most commonly used for data
    where the underlying variables have a long-run common stochastic trend, also known
    as [cointegration](https://en.wikipedia.org/wiki/Cointegration "Cointegration").[3]

### 2.3 Model evaluation

1. Prediction
   MAPE. mean absolute percentage error

   $$
   MAPE=\frac{1}{n}\sum\limits_{t=1}^{n}|\dfrac{Y_t-\hat{Y_t}}{Y_t}|
   $$

   sMAPE. symmetric MAPE

   $$
   sMAPE=\frac{1}{n}\sum\limits_{t=1}^{n}\dfrac{|Y_t-\hat{Y_t}|}{(|Y_t|+|\hat{Y_t}|)}
   $$
2. validation: rolling hold-out samples: 连续的按顺序逐步下扩张自己的训练集，测试集长度不变紧跟训练集。一次完成后，记录误差，模型基于此次训练集更新。然后继续向下扩张特定数量的训练集。

# 3 Nonparametric Regression

Splines, Kernel, Locally Weighted Regression
Most of tools in classical statistics are parametrics, they rely on assumptions about the underlying distribution of the data being studied.Techniques like least squares regression (which assumes normally distributed residuals) are parametric.Non-parametric machine learning algorithms do not rely on assumptions about the shape of the underlying data to work.

# 4 Data exploration

https://www.geeksforgeeks.org/density-plots-with-pandas-in-python/

1. density
2. estimation
3. normality
4. test
5. monte carla copulas

# 5 Data Cleaning

### References:

[1]https://www.youtube.com/watch?v=SqN-qlQOM5A
[2]https://www.youtube.com/watch?v=hAD5vVz07ZA&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&index=3
[3]https://en.wikipedia.org/wiki/Error_correction_model
[4]https://www.youtube.com/watch?v=R3Y0KQ-RkCE&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&index=9
[5]https://www.youtube.com/watch?v=0-FKPJ5KxSo&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&index=11

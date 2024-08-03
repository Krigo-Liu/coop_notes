---
title: Statistics
icon: file
order: 2
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
$$y = \beta_0+\beta_1x+\epsilon_i$$
where 
- $\beta_0\text{ population intercept },\beta_1 \text{ population slope }$ are fixed but unknown. Estimated by $b_0 \text{ and } b_1$ (whether using maximum likelihood or OLS, same result). $\beta_1$ means the amount of change in $E(y)$ when one unit change in x. 
- $(x_i, y_i)$ is a pair of data, plug in the formula: $y_i = \beta_0+\beta_1x_i+\epsilon_i$ . The only variable in this formula is $\epsilon_i$.
- $\epsilon$  is the model error, which follows the normal theory $\epsilon_i \sim N(0,\sigma^2)$. 
	- It is iid(independent identically distributed). $cov(\epsilon_i,\epsilon_j)=0, \text{for i} \neq j$. 
	- Homogeneous variance assumption $var(\epsilon_i)=\sigma^2$. (note: the unbiased estimator of $\sigma$ is $s$)
$$s^2=\dfrac{1}{n-2}\sum\limits_{i=1}^{n}(y_i-\hat{y_i})^2$$
**Some inferences**:
1. $E(a)=a$. $E(\epsilon_i)=0$
$$E(y_i)=E(\beta_0+\beta_1+\epsilon_i)=E(\beta_0+\beta_1x_i)+E(\epsilon_i)=\beta_0+\beta_1x_i$$
2. $var(a)=0$ $$var(y_i)=var(\beta_0+\beta_1+\epsilon_i)=var(\beta_0+\beta_1x_i)+var(\epsilon_i)=\sigma^2$$

### 1.1.3 Multiple linear regression (MLR)
$$\hat{y}=X\hat{\beta}+\hat{\epsilon}$$
### 1.1.4 Ordinary least squares (OLS)
1. A method to estimate unknown paras$\beta$. in a linear regression model. 
2. It canbe used in  SLR & MLR (>1 regressor).
##### In SLR, 2 paras $\beta_0, \beta_1$, and their estimators are $b_0, b_1$. Use OLS: 
$$min J(b_0, b_1) = min SSE=min\sum\limits_{i=1}^{n}[y_i - \hat{y_i}]^2=min\sum\limits_{i=1}^{n}[y_i - b_0 -b_1x_i]^2$$
Use partial derivatives, then get 2 estimators:
$$b_0 = \bar{y} - b_1\bar{x}$$
$$b_1=\dfrac{n\bar{x}\bar{y}-\sum\limits_{i=1}^{n}x_iy_i}{n\bar{x}^2-\sum\limits_{i=1}^{n}x_i^2}
=\dfrac{\sum\limits_{i=1}^{n}(x_i-\bar{x})y_i}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}
=\dfrac{\sum\limits_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}
=\dfrac{S_\text{xy}}{S_\text{xx}}$$
Because
$$E(b_0)=\beta_0$$
$$E(b_1)=\beta_1$$

$b_0, b_1$ are unbiased estimators.
$$var(b_1)= \dfrac{\sigma^2}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2}$$
$$var(b_0)=\sigma^2(\dfrac{1}{n}+\dfrac{\bar{x}^2}{\sum\limits_{i=1}^{n}(x_i-\bar{x})^2})$$
$$cov(b_0,b_1) = -\dfrac{\bar{x}\sigma^2}{S_\text{xx}}$$
### 1.1.5 Analysis of variance (ANOVA) 
1. partition of digree of freedom for SLR.
	equation:  $y = \beta_0 + \beta_1x$
	- k = 2      for($\beta_0,\beta_1$)
	- n sample size
	
![[df.png]]
2. Regression hypothesis
$$H_0: \beta_1=0$$
$$H_1: \beta_1\neq0$$
	- $H_0 \text{ No regression relationship exists.}$
	- $H_1 \text{ Regression analyasis exists.}$
	Then do ==F-test==: test for the entire regression. Is the reg statistically significant?
	$$F_\text{k-1, n-k}=\dfrac{MSR}{MSE}=\dfrac{\frac{SSR}{k-1}}{\frac{SSE}{n-k}}$$
	where
	- k-1: df for reg
	- n-k: df for error
	**Conclusion**: Reject $H_0$ if $F_\text{CALC}>F_\text{CV}$ . Regression analysis exists.
	Note: F value can be used for ranking the importance of features. The bigger the F for a feature, the bigger the SSR, in favor of $H_1$.
	
3. Hypothesis for $\beta_1$
$$H_0: \beta_1=0$$
$$H_1: \beta_1\neq0$$
	- $H_0 \text{ x has no impact on y.} E(y)=\beta_0$
	==t-test== is a test for only $\beta_1$. Is there an evidence that x contributes information in the prediction of y?
$$t_\text{n-k}=\dfrac{b_1}{\frac{\sqrt{MSE}}{\sqrt{\sum(x-\bar{x})^2}}}$$
	**Conclusion**: Reject $H_0$ if $t_\text{CALC}>t_\text{CV}$. x has impact on y.
4. $R^2$ coefficient of determinate
$$R^2=\dfrac{SSR}{SST}=\dfrac{\sum\limits_{i=1}^{n}(\hat{y_i}-\bar{y})^2}{\sum\limits_{i=1}^{n}(y_i-\bar{y})^2}=1-\dfrac{SSE}{SST}$$
	- $0<R^2<1$
	- $R^2$ means the proportion of variation in the response data that is explained by the **model**.
	- $R^2$ on its own cannot tell you anything about causation. (causaion means that a change in one variable causes a change in another variable. correlation: there is a statistical association between variables)
## 1.2 Generalized linear models (GLM)
The difference between linear models and GLM.
**standard linear model**: 
- systematic component: $$y = \beta_0+\beta_1x+\epsilon_i$$
- Link function is one.   $\mu_i=x_i^T\beta$.  
- Random component: normal distribution $y_i \sim N(\mu_i,\sigma^2)$ residuals are normally distributed.
- Estimators: least squares or maximum likelihood will give the same result
Not all situation can be considered as a normal distribution, large error.
**GLM**:
- systematic component: $$y = \beta_0+\beta_1x+\epsilon_i$$
- Link function is a function that delinearize the mathematical relationship between the predictors and the outcome. $g(\mu_i)=x_i^T\beta$ . The link function transforms the prediction part, everything except for the $\epsilon.$  You need to decide this when doing analysis. 
- Random component: Residuals ars not normal, it might be comes from a poisson, a binomial, a gamma.
- have to use maximum likelihood

	![[Pasted image 20240803223049.png]]
							[1] Types of GLM.


two tpyes of varia: binomial.
skewed, positive discrete distribution: poisson. #time you go to a doctor.
skewed, positive continuous dist: gamma
# 2 Time series
### References:
[1]https://www.youtube.com/watch?v=SqN-qlQOM5A



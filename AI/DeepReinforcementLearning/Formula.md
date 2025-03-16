# Summary of Notation

1. Capital letters: random variables
2. Lowercase letters: values of random variables & for scalar functions.
3. **Quantities** that are required to be real-valued vectors are written in **bold** and in **lowercase** (even if random variables). Matrices are bold capitals.

## Symbols

- $\overset{.}{=}$: equality relationship that is true by definition
- $\approx$: approximately equal
- $\propto$: proportional to
- $Pr\{X = x\}$: probability that a random variable $X$ takes on the value $x$
- $X \sim p$: random variable $X$ selected from distribution $p(x)$
- $ E[X] $: expectation of a random variable $X$, i.e.,
  $  E[X] \overset{.}{=} \sum_x p(x)x  $
- $ \arg\max_{a} f(a) $: a value of $a$ at which $f(a)$ takes its maximal value
- $ \ln x $: natural logarithm of $x$
- $ e^x $: the base of the natural logarithm, $ e \approx 2.71828 $, carried to power $x$; $ e^{\ln x} = x $
- $ \mathbb{R} $: set of real numbers
- $ f: X \to Y $: function $ f $ from elements of set $ X $ to elements of set $ Y $
- $ (a, b] $: the real interval between $ a $ and $ b $ including $ b $ but not including $ a $

## Parameters

- $ \epsilon $: probability of taking a random action in an $ \epsilon $-greedy policy
- $ \alpha, \beta $: step-size parameters
- $ \gamma $: discount-rate parameter
- $ \lambda $: decay-rate parameter for eligibility traces
- $ \mathbb{1}_\text{predicate} $:  indicator function. = 1 if the predicate is true, else 0.

## 1 Introduction

## 2 Multi-Armed Bandit Problem

- $ k $: number of actions (arms)
- $ t $: discrete time step or play number
- $ q_*(a) $: true value (expected reward) of action $ a $
- $ Q_t(a) $: estimate at time $ t $ of $ q_*(a) $
- $ N_t(a) $: number of times action $ a $ has been selected up to time $ t $
- $ H_t(a) $: learned preference for selecting action $ a $ at time $ t $
- $ \pi_t(a) $: probability of selecting action $ a $ at time $ t $
- $ \bar{R}_t $: estimate at time $ t $ of the expected reward given $ \pi_t $

## 3 Markov Decision Process

The reinforcement learning agent and its environment interact over a sequence of discrete time steps. Everything inside the agent is completely known and controllable by the agent; everything outside is incompletely controllable but may or may not be completely known.The agent’s objective is to maximize the amount of reward it receives over time. ****Markov Decision Process**** is a mathematical framework used to describe an environment in decision-making scenarios where outcomes are partly random and partly under the control of a decision-maker.

- $t$: discrete time step.
- $\color{turquoise}\text{s, s' : current state, next state}$,  $\color{turquoise}\text{basis for making the choices}$
- $ a $: an action made my the agent
- $\color{turquoise}\text{ r} $: a reward, $\color{turquoise}\text{basis for evaluating the choices}$
- $ S $: set of all nonterminal states
- $ S^+ $: set of all states, including the **terminal state**
- $ A(s) $: set of all actions available in state $ s $
- $ R $: set of all possible rewards, a finite subset of $ \mathbb{R} $
- $ \rho \subseteq \mathbb{R} $: subset of $ \mathbb{R} $
- $ |S| $: number of elements in set $ S $
- $ T, T(t)$ final time step of an episode; the episode including time step t.
- $ A(t)$ : Action at t
- $ S(t)$ : state at t
- $ R(t)$ : reward at t
- $\color{turquoise} \pi  $ : policy (stochastic decision-making rule),is a $\color{turquoise}\text{mapping from states to actions}$
- $\pi(s)$ : action taken in state s under deterministic policy $\pi$
- $\pi(a|s)$ : <mark> probability </mark> of taking action a in state s under stochastic policy $\pi$

$\color{orange}\text{Finite Markov dynamics:}$ probability of transition to state $ s' $ with reward $ r $, from state $ s $ and action $ a $

$$
p(s', r | s, a)= Pr\{S_t=s', R_t=r | S_\text{t-1}=s, A_\text{t-1}=a\}
$$

$$
\sum_{s'\in S} \sum_{r\in R} p(s', r | s, a)=1, \text{for all s} \in S, a \in A(s)
$$

- $ p(s' | s, a) $: **state**-transition prob. probability of transition to state $ s' $, from state $ s $ taking action $ a $
- $ r(s, a) $: expected immediate reward from state $ s $ after action $ a $. 从上个状态采取行动后的即时回报

  $$
  r(s,a) = E[R_t| S_\text{t-1}=s, A_\text{t-1}=a]=\sum_{r\in R}r\sum_{s'\in S}p(s',r|s,a)
  $$
- $ r(s, a, s') $: expected immediate reward on transition from $ s $ to $ s' $ under action $ a. $ 在行动a下，两个状态转化的即时回报

  $$
  r(s,a,s') = E[R_t| S_\text{t-1}=s, A_\text{t-1}=a, S_t=s']=\sum_{r\in R}r \frac{p(s',r|s,a)}{p(s'|s,a)}
  $$

$\color{orange}\text{Expected return }G_t$

- function of future rewards, long term, that the agent seeks to maximize (in expected value).
- undiscounted formula: $G_t= R_\text{t+1}+R_\text{t+2}+R_\text{t+3}+...+R_\text{T}$ appropriate for episodic tasks (interaction does not naturally break into episodes but continues without limit.)
- discounted formula: $G_t= R_\text{t+1}+\gamma R_\text{t+2}+\gamma^2R_\text{t+3}+...+R_\text{T}=\sum_{k=0}^{\infty} \gamma^kR_\text{t+k+1}=R_\text{t+1}+\gamma G_\text{t+1}$, appropriate for continuing tasks (Xbreaks into episode, continue without limitation).
  - Note that although the return is a sum of an infinite number of terms, it is still finite if the reward is nonzero and constant—if < 1. For example, if the reward is a constant +1
    $$
    G_t=\sum_{k=0}^{\infty} \gamma^kR_\text{t+k+1}=\sum_{k=0}^{\infty}\gamma^k = \frac{1}{1-\gamma}
    $$

$\color {orange}\pi \text{'s Value Functions}$ 给s, (s,a), exp return from that sate, (s,a)|$\pi$赋值

- $ v_\pi(s) $: value of state $ s $ under policy $ \pi $ (expected return)
- $ v_*(s) $: value of state $ s $ under the **optimal policy** (its value functions are optimal).
  - optimal value f for s & (s,a) are unique for a MDP, but there can be many optimal $\pi$
  - Any policy that is greedy with respect to  the optimal value functions must be an optimal policy.
- $ q_\pi(s, a) $: value of taking action $ a $ in state $ s $ under policy $ \pi $
- $ q_*(s, a) $: value of taking action $ a $ in state $ s $ under the optimal policy

$\color{orange}\text{Bellman equation for state values } v_\pi$ The value function $v_\pi$ s Bellman equation.

![image.png](pic/image.png)

$$
v_\pi(s)=E_\pi[G_t|s]
=E_\pi[R_\text{t+1}+\gamma G_\text{t+1}|S=s]
=\sum_a\pi(a|s)\sum_\text{s',r}p(s',r|s,a)[r+\gamma v_\pi(s')] \text{   for all s} \in S
$$

$\color{orange}\text{Bellman optimality equation}$ :the value of a state under an optimal policy must equal the expected return for  the best action from that state

$$
v_*(s)=max_a q\pi_*(s,a) 
=E_\pi[G_t|s]
=E_\pi[R_\text{t+1}+\gamma G_\text{t+1}|S=s]
=\sum_a\pi(a|s)\sum_\text{s',r}p(s',r|s,a)[r+\gamma v_\pi(s')]
$$

$\color{orange}\text{Apporximations for value f, policy, models}$

Even if the agent has a complete and accurate environment model, the agent is typically unable to perform enough computation (memory) per time step to fully use it.

---

# dft

Approximate Value Functions

- $ v_\theta(s) $: approximate value of state $ s $ given parameter vector $ \theta $
- $ q_\theta(s, a) $: approximate value of state-action pair $ (s, a) $ given parameter vector $ \theta $
- $ \nabla v_\theta(s) $: column vector of partial derivatives of $ v_\theta(s) $ with respect to $ \theta $
- $ \nabla q_\theta(s, a) $: column vector of partial derivatives of $ q_\theta(s, a) $ with respect to $ \theta $

#### Bellman Operators

- $ B_\pi $: Bellman operator for value functions
- $ P $: state-transition probability matrix under $ \pi $
- $ D $: diagonal matrix with on-policy state distribution on its diagonal
- $ X $: feature matrix, with $ x(s) $ as its rows
- $ \Pi $: projection operator for value functions

## Missing Symbols and Notation

Below are the missing symbols and notation that were not properly formatted in the original document:

## Symbols

- $\mathbb{R}$: set of real numbers
- $f : X \to Y$: function $f$ from elements of set $X$ to elements of set $Y$
- $(a, b]$: the real interval between $a$ and $b$ including $b$ but not including $a$
- $\in$: is an element of; e.g., $s \in S, r \in R$
- $\subseteq$: subset of; e.g., $R \subseteq \mathbb{R}$
- $|S|$: number of elements in set $S$

## Temporal Difference Learning

- $\delta_t$: temporal-difference (TD) error at time $t$
- $\delta_t^s, \delta_t^a$: state- and action-specific forms of the TD error
- $n$: in n-step methods, $n$ is the number of steps of bootstrapping

## Eligibility Traces

- $w, w_t$: weight vector in function approximation
- $\mathbf{w}, \mathbf{w}_t$: weight vector notation
- $x(s)$: vector of features visible in state $s$
- $x(s, a)$: vector of features visible in state $s$ taking action $a$
- $\mathbf{x}(s)$, $\mathbf{x}(s, a)$: feature vectors in bold
- $\mathbf{w}^T \mathbf{x}$: inner product of weight vector and feature vector

## Policy Gradient Methods

- $\theta, \theta_t$: parameter vector of target policy
- $\pi(a | s, \theta)$: probability of taking action $a$ in state $s$ given parameter $\theta$
- $\nabla \pi(a | s, \theta)$: gradient of policy function
- $J(\theta)$: performance measure for policy $\pi_\theta$
- $\nabla J(\theta)$: gradient of performance measure
- $b(a|s)$: behavior policy used to select actions while learning about target policy $\pi$

## Importance Sampling

- $\rho_t:h$: importance sampling ratio for time $t$ through time $h$
- $\rho_t$: importance sampling ratio for time $t$ alone, $\rho_t = \rho_{t:t}$
- $r(\pi)$: average reward (reward rate) for policy $\pi$
- $\bar{R}_t$: estimate of $r(\pi)$ at time $t$

## Norms and Errors

- $\|v\|^2_{\mu}$: $\mu$-weighted squared norm of value function $v$
- $\|\delta_t\|^2$: squared temporal-difference error
- $BE(w)$: mean square Bellman error
- $PBE(w)$: mean square projected Bellman error
- $TDE(w)$: mean square temporal-difference error

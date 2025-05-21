### Formatting and Abbreviation Key

1. Capital letters: random variables
2. Lowercase letters: values of random variables & for scalar functions.
3. **Quantities** that are required to be real-valued vectors are written in **bold** and in **lowercase** (even if random variables). Matrices are bold capitals.
4. Abbreviations: - for disadvantages, + for advantages, sol for solution, nw for network, nn for neural network, env for environment.
# 1 Introduction

Types of learning in AI:
- Supervised Learning(SL): a teacher gives an AI answers to learn from.
- Unsupervised Learning(UL): AI tries to find patterns in the world.
- Reinforcement Learning (RL): particular useful where we want to train AIs to have certain skills we do not fully understand ourselves. e.g. how to walk (the angles and velocity of your feet ...) 

|           | SL                                                                                                                                                                      | UL                                                                                                                                                                                                                                   | RL                                                                                                                                                                                                                                                                                                                            |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objective | Learning from static dataset<br><br>Build a system to generalize its responses which acts correctly in situations not present in the training set                       | finding patterns hidden in collections of unlabeled data.                                                                                                                                                                            | Learns through interaction with an environment,maximize the total reward in the long run  <br> <br>About sequence decision making                                                                                                                                                                                             |
| Problem   | Needs the knowledgable external supervisor, and it is impractical to obtain exp. (correct and representative behavior) of all situations, focus on isolated subproblems | Lack of Ground Truth:can't directly know if the clusters or representations are “correct” or meaningful without manual inspection or domain knowledge;<br><br>Sensitive to Initialization and Hyper-parameters;<br><br>Mode collapse | Trade-off between exploration (trying new actions) and exploitation(choosing actions known to yield good rewards):The dilemma is that neither exploration nor exploitation can be pursued exclusively without failing at the task. Pure exploitation might miss better options, while pure exploration might waste resources. |


CrashCourse AI lecture 9 has explained fundamental ideas of RL:

   Generally, we tell the AI at the very end of the task if they succeeded, and then ask them to tell us how they did it. Sometimes the feed back could come earlier. So, if we want AI to learn how to walk, we give them a **reward** when it both standing up and moving forward, and then figure out what steps they took to get to that point. The longer the AI stands up and moves forward, the longer it's walking, and the more reward it gets.

   The key of RL is trial-and-error, over and over again. For human, the reward might be a cookie or the joy. For AI, the reward is just a small positive signal that tells it "good job, and do that again!"

   In SL, we would have a training label after each action that tells the AI whether it did the right thing or not. We cannot do that here with RL, because we do not know the right thing actually is until we complete the task. Here is the hardest thing in RL: **credit assignment**.

   Let's say we put the agent into a room, its goal is to get the battery for recharging. The agent has 4 actions (up, down, left, right), and states (current location, previous location, and visual scope(whole room)). Then, let the agent **explore** the room. Every time the agent succeed at its tasks (walks from the start point to the goal), we look back at its action, and figure out which game state were helpful and which were not. During this reflection, we are assigning **values** to those different game states and deciding on a **policy** for which actions work best. The values give more information that help decide a better policy.

   But it is boring if the agent just takes the same long and winding path every time. -> **Trade-off between exploitation and exploration**. Now that the bot knows one way to get to the battery, he could just **exploit** his knowledge by always taking the same 10 actions. It is not terrible, he knows he will not get lost and will definitely get a reward. But there are probably more efficient paths out there. It is usually worth trying lots of different actions to see what happens which is a strategy called **exploration**. Every time he explores, he will get a bit more data about the best way to get a reward. So, let the bot explore for 100 actions, and after he completes a path, we will update the values of the cells he have been to. But the bot might explore worse paths. So we always need the **balance of exploitation and exploration**.

   When the bot was learning how to navigate on that small grid, cells closer to the battery have higher values than those far away. But for many problems we will want to use a **value function** to think about what we have done so far, and decide on the next move using math.

   There are so many **types of problems**. But a lot these problems need a ton of data and a ton of time to solve. There have been really impressive results recently thanks to deep reinforcement learning on large-scale computing. These systems can explore massive environments and a huge number of states. At core of a lot of these problems are discrete symbols, like the squares on a game board. So how to reason and plan in these spaces is a key part of AI. (CrashCourse, 2019)

Algorithm Selection Matrix Based on Environment Characteristics and Model Transparency by the lecture note:

| Env characteristics                    | White-Box (The relationship between variables and objectives can be expressed with explicit formulas.)                                                                                      | Black-Box (only input-output interactions are observable)                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Static                                 | **Operations Research & Optimization**:<br>(Mixed-integer) Linear Programming,<br>Nonlinear Optimization                                                                                    | **NN Surrogate**: Model Optimization,<br>Bayesian Optimization                                                                |
| Dynamic<br>(env has state transitions) | Transition prob and the reward $P(s'\| s,a), R(s,a)$ are fully known.<br><br>**Dynamic Programming**:<br>Value Iteration, Policy Iteration,<br>Direct MDP Solving,<br>Tree/Graph Search<br> | Do not know the model.<br><br><br>**RL** (the most typical senario):<br>Policy Optimization,<br>Bandits, Sequential Black-Box |

s for state, a for action.

Usually:
White-box ↔ Model-based methods
Black-box ↔ Model-free

Not 100%, because: sometimes you may learn a model (transition dynamics) when the model is unknown, that is a model-based, but black-box.


# 2 Multi-Armed Bandit Problem (MAB)

It can be viewed as a state-less RL problem.

The scene:
2. I am a gambler who wants to **maximize** my total rewards on pulling levers in a 300 trails.
3. there are k levers
4. each lever corresponds to an unknown stationary probability distribution. each choice(actions) -> expected/mean reward (value of that action)
5. explore - exploit the levers

Action-value Q
$$
Q_t(a) =  \frac{\sum_{i=1}^{t-1} R_i \cdot \mathbb{1}_{A_i=a}}{\sum_{i=1}^{t-1} \mathbb{1}_{A_i=a}}=\frac{R_1+R_2+...+R_{N_t(a)}}{N_t(a)}
$$

We introduce 3 methods to solve:
### 2.1 Greedy type
1. **Greedy**: At every step, **choose the arm with the highest estimated average reward** (based on past plays).  It **does not explore**. If the initial estimates are wrong, greedy may **lock into a sub-optimal arm** permanently. It can’t discover better arms if it never tries them again.
$$
A_t = arg \max_a Q_t(a)
$$

2. **$\epsilon$ - greedy**: With probability **ε**, explore, pick a random arm. With prob **1-ε** exploit: pick the current best arm.
	The probability of selecting a* depends on whether it is currently estimated as the best action.
	If a* is the current best action:
$$
P(a^*)=(1-\epsilon)+\epsilon/k
$$
	If not: 
$$
P(a^*)=\epsilon/k
$$
	Early in the learning, when the agent does not know the true values, the probability of choosing a* is low. Over time as Q(a*) gets updated and improves, a* is more likely to become the best action, and the probability increases toward $(1-\epsilon)+\epsilon/k$.

	It is possible to reduce $\epsilon$ over time to try to get the best of both high and low values.

skip: ### 2.2 Upper Confidence Bound (UCB)
skip: ### 2.3 Thompson Sampling (TS)

| Algorithm             | Exploitation | Exploration          | Type          | Pros                         | Cons                                  |
| --------------------- | ------------ | -------------------- | ------------- | ---------------------------- | ------------------------------------- |
| **Greedy**            | ✅ High       | ❌ None               | Deterministic | Simple, fast                 | Easily gets stuck                     |
| **ε-Greedy**          | ✅ Moderate   | ✅ Random, uniform    | Stochastic    | Easy to implement            | Inefficient exploration               |
| **UCB**               | ✅ Strong     | ✅ Confidence-based   | Deterministic | Theoretically grounded       | Needs tuning, assumes bounded rewards |
| **Thompson Sampling** | ✅ Strong     | ✅ Posterior sampling | Probabilistic | Effective, Bayesian approach | Can be computationally heavier        |

skip:
incremental update rule, 
Non-stationary problem for sample-avg, 
Exponential-recency weighted average.
# 3 Markov Decision Process (MDP)

The reinforcement learning agent and its environment interact over a sequence of discrete time steps. Everything inside the agent is completely known and controllable by the agent; everything outside is incompletely controllable but may or may not be **completely** known. The agent’s objective is to maximize the amount of reward it receives over time.
### 3.1 Define the process/trajectory
$\color{red}\text{Stochastic process}$: 1/more events, stochastic(dynamic) system/phenomenon evolve with t.

$$
P[S_\text{t+1}|S_1,...,S_t]
$$

$\color{red}\text{Markov process }$

- <S state,P>
- a stochastic process
- with Markov property:The current state is the future sufficient statistics (充分统计量). $(future \bot past)|present$

$$
P[S_\text{t+1}|S_t]=P[S_\text{t+1}|S_1,...,S_t]
$$

$\color{red}\text{Markov reward process(MRP)}$

- < S, P, r reward, $\gamma$ discount>
- env: 不受agent控制，产生s,r
- episodes: agent–environment interaction breaks naturally into subsequences, each episode ends in a special state called the terminal state.
- $\color{red}\text{discounted episode's return from }s_t$

$$
G_t= R_\text{t}+\gamma R_\text{t+1}+\gamma^2R_\text{t+2}+...=\sum_{k=0}^{\infty} \gamma^kR_\text{t+k}=R_\text{t}+\gamma G_\text{t+1}
$$

	$\gamma \in[0,1]$, which helps to converge.

Comparing the G here and the one in book written by Sutton and Barto ($G_t'= R_\text{t+1}+\gamma R_\text{t+2}+\gamma^2R_\text{t+3}+...+R_\text{T}=\sum_{k=0}^{\infty} \gamma^kR_\text{t+k+1}$), G here makes sure the total order of episodic return for all different return sequences.


$\color {red}\text{Markov decision process (MDP)}$

- <S,A,P,r,$\gamma$>
- state transfer function $p(s'| s, a)= Pr\{S_t=s' | S_\text{t-1}=s, A_\text{t-1}=a\}$
- reward function r(s,a)

  ![image.png](pic/MDP.png)
- dynamics: MDP stochastic transition, to next state $s～P(·|s_0,a_0)$. dot (⋅) represents any possible next state

  ![image.png](pic/MDPdy.png)

When the rewards are only related to state in the situation of maze(location) or go (size of the final territory):

  Reward function r(s): $S -> R$
  their MDP dynamics:
   s0 - a0, r(s0) -> s1 -a1, r(s1)-> ...

   cumulative reward: 
$$
   r(s_0)+\gamma(s_1)+\gamma^2r(s_2)+...
$$


$\color {red}\text{Policy }\pi(a|s)=P(a|s)$

- prob of taking action a in state s
- Markov property: policy only needs to be related to current s

$$
\sum_a \pi(a|s)=1
$$

- **deterministic** policy: for a given s, the agent always chooses the same a, without any randomness or probabilities involved.

$$
\pi(a \mid s)=\pi(s)=\mu(s)=\begin{cases}1 & \text{if } a = \mu(s) \\0 & \text{otherwise} \end{cases}
$$

- **stochastic** policy: a is sampled from the distribution $\pi$

$$
\pi(a \mid s)\in[0,1]
$$

$\color {red}\text{Convert MDP to MRP by marginalization}$
- MRP is MDP's simplified version, removing the action part, which focuses on state transition, reward function and discount factor (γ). 
- Under each state, after selecting a certain action: 

$$
P'(s'| s)=\sum_a \pi(a|s)P(s'| s, a)
$$

- reward at s

$$
r'(s)=\sum_a \pi(a|s)r(s,a)
$$

So, MRP <S,P',r',$\gamma$>

### 3.2 Stats about the trajectory

$\color {red}\text{State-action occupancy measure}$
- Given the same MDP, the state-action(s-a) **distribution** sampled by different policy is different
- describes how often a policy visits certain state-action pairs in a Markov Decision Process (MDP).

- state distribution $$d^\pi(s)=\sum_{t=0}^{\infty}P(s|\pi)$$
- state-action distribution $$d^\pi(s,a)=\sum_{t=0}^{\infty}P(s,a|\pi)$$
  Relationship

$$
\begin{aligned}
& d^\pi(s,a) = \pi(a|s)d^\pi(s)=\pi(a|s)\sum_{a'} d^\pi(s,a')\\
\end{aligned}
$$

- **Discounted** state-action distribution

$$\begin{aligned}

\hat{\rho}^\pi(s, a) &= \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty}\gamma^t \mathbb{I}(S_t = s, A_t = a) \right] \quad \forall s \in S, a \in \mathcal{A} \\ 
&= \sum_{t=0}^{\infty} \gamma^t \mathbb{P}(S_t = s, A_t = a|\pi)
\end{aligned}
$$

- **Discounted** state distribution

$$
\begin{aligned}
\hat{v}^\pi(s) &= \sum_{t=0}^{\infty} \gamma^t \mathbb{P}(S_t = s | \pi)
\\ &= \sum_{t=0}^{\infty} \gamma^t \mathbb{P}( s | \pi) \sum_{a} \pi(a|s)
\\ &= \sum_{t=0}^{\infty} \sum_{a} \gamma^t \mathbb{P}( s | \pi) \pi(a|s)
\\ &= \sum_{a} \sum_{t=0}^{\infty} \mathbb{P}( s,a | \pi)
\\ &= \sum_{a} \hat{\rho}^\pi(s, a)
\end{aligned}
$$

- Normalization (When ($\gamma$ < 1\)): two distribution above -> real dist

$$
\begin{aligned}
\sum_{s} \hat{v}^\pi(s) &= \sum_{s} \sum_{t=0}^{\infty} \gamma^t \mathbb{P}(s | \pi)
\\ &= \sum_{t=0}^{\infty} \sum_{s}\gamma^t\mathbb{P}(s| \pi)
\\ &= \sum_{t=0}^{\infty}\gamma^t
\\ &= \frac{1}{1-\gamma}
\end{aligned}
$$

- Normalized Discounted (Action-) State Distribution:

$$
\begin{aligned}
v^\pi(s) &= (1 - \gamma) \hat{v}^\pi(s) \\
\rho^\pi(s,a) &= (1 - \gamma) \hat{\rho}^\pi(s,a)
\end{aligned}
$$

- relationship

$$
\begin{aligned}
\rho^\pi(s,a)=v^\pi(s)\pi(a|s) \\
 v^\pi(s)=\sum_a \rho^\pi(s,a)
\end{aligned}
$$

---
- Theorem 1: The occupancy measure obtained by two policies interacting with the same dynamic environment satisfies: $$\rho^{\pi_1}=\rho^{\pi_2} \text{ iff } \pi_1=\pi_2$$
- Theorem 2: Given occupancy measure 𝜌, The only policy that can generate this occupancy metric is $$\pi_\rho(s|a) = \frac{\rho(s,a)}{\sum_{a'} \rho^\pi(s,a')}$$
---
  
### 3.3 Policy

  - **policy cumulative reward**: 

$$
\begin{aligned}
J(\pi) &=\mathbb{E}_\pi[\sum_{t=0}^{\infty}\gamma^t r(S_t,A_t)]
\\ &= \sum_{t=0}^{\infty}\gamma^t \mathbb{E}_\pi[r(S_t,A_t)]
\\ &= \sum_{t=0}^{\infty}\gamma^t \sum_s \sum_a \mathbb{P}(s,a|\pi) {\color{red}\text{r(s,a)}}
\\ &= \sum_s \sum_a {\color{green}[\sum_{t=0}^{\infty} \gamma^t\mathbb{P}(s,a|\pi)]} {\color{red}\text{r(s,a)}}
\\ &= \sum_s \sum_a {\color{green}\hat{\rho}^\pi(s, a)}{\color{red}\text{r(s,a)}}
\\ &= \mathbb{E}_{(s,a)\sim \hat\rho^\pi}[r(s,a)]
\end{aligned}
$$

- **Policy learning goal**: select those actions that can maximize the expected cumulative reward
  omit the max for two after terms.
$$
\max_\pi J(\pi)= \mathbb{E}_\pi[\sum_{t=0}^{\infty}\gamma^t r(S_t,A_t)] ≃ \sum_s \sum_a\rho^\pi(s,a)r(s,a)
$$
  The relationship between the policy π and its occupancy measure ρ is a black box, so the optimization objectives above cannot directly guide the update direction.
  
  In each state S, after the policy changes the choice of action, does the policy as a whole become better? 
  Not necessarily. The RL optimization especially with cumulative reward is not locally decomposable due to the sequential and dynamics nature of MDP's, so improving the local choice **doesn't guarantee** global improvement of the policy. Therefore, to improve the policy as a **whole**, we often need to: estimate gradients over **expected return**,  and make **global updates** based on full trajectories, not just one-step changes.

#### 3.3.1 Policy Evaluation & Policy Improvement

$\color{red}\text{Bellman expectation equations }$

- State-value function $V^\pi(s)$: Expected reward by following policy $\pi$ from state s
- Action-value function $Q^\pi(s, a)$: Expected reward while following policy $\pi$ from state s and take action a
  - q: quality

$$
\begin{aligned}
V^\pi(s) &= E_\pi[G_t|s]
\\ &= E_\pi[R_t + \gamma G_{t+1}|s]
\\ &= E_\pi[R_t|s]+ E_\pi[\gamma G_{t+1}|s]
\\ &= E_\pi[R_t|s]+ \gamma E_\pi[G_{t+1}|s]
\\ &= E_\pi[R_t|s]+ \gamma V^\pi(s_{t+1})
\\ &= E_\pi[R_t|s]+ E_\pi[\gamma V^\pi(s_{t+1})|s]
\\ &= \sum_a \pi(a|s)r(s,a) + \sum_a \pi(a|s)\gamma\sum_{s_{t+1}} P(s_{t+1}|s,a) V^\pi(s_{t+1})
\\ &= \sum_a \pi(a|s)(r(s,a) + \gamma\sum_{s_{t+1}} P(s_{t+1}|s,a) V^\pi(s_{t+1}))
\\ &= \sum_a \pi(a|s)Q(s,a)
\end{aligned}
$$

$$
\begin{aligned}
Q^\pi(s,a) &= E_\pi[G_t|s,a]
\\ &= E_\pi[R_t + \gamma G_{t+1}|s,a]
\\ &= E_\pi[R_t + \gamma Q(S_{t+1},A_{t+1})|s,a]
\\ &= E_\pi[R_t|s,a]+ E_\pi[\gamma Q(S_{t+1},A_{t+1})|s,a]
\\ &= r(s,a) + \gamma \sum_{s_{t+1}} P(s_{t+1}|s,a) \sum_{a_{t+1}} \pi(a_{t+1}|s_{t+1})Q(s_{t+1},a_{t+1})
\\ &= r(s,a) + \gamma E_{s'∼P(⋅∣s,a), a'\sim\pi_\theta(·|s')}Q(s',a')
\\ &= r(s,a)+ \gamma \sum_{s_{t+1}} P(s_{t+1}|s,a) V^\pi(s_{t+1})
\\ &= \color{red}{r(s,a)+ \gamma E_{s'∼P(⋅∣s,a)} [V^{\pi} (s')]}
\end{aligned}
$$

- Explanations: 
  The value function $V_\pi$ 's Bellman equation.

![image.png](pic/image.png)

```text
Starting from state s, the root node at the top, the agent could take any of some set of actions (e.g.3) based on its policy pi. 
From each of these, the environment could respond with one of several next states, s0 (e.g.2), 
along with a reward, r, depending on its dynamics given by the function p.
```

  The action-value function $Q_\pi$ 's Bellman equation.

![q pi.png](pic/qpi.png)

```text
If we were to take action 𝑎 in state 𝑠, what is the expected return if we then follow 𝜋 afterward?
```

---
$\color{red}\text{Policy improvement theorem}$

Policy $\pi'$ is the improvement of $\pi$ if:  for any s, $Q^\pi(s, \pi'(s)) \ge V^\pi(s)$

Then $\pi \text{ and } \pi'$ satisfy: for any s, $V^{\pi'}(s) \ge V^\pi(s)$.                       (Proof p28)

---

So it is able to improve our policy iteratively.

#### 3.3.2 Algorithms that that iteratively improve a policy to solve an MDP

2 algos: 
- **Policy Iteration** (PI) = alternating evaluation and improvement
- **Value Iteration** (VI) = single-step updates combining evaluation + improvement


| Property                        | Description                                                | Value Iteration & Policy Iteration                                                                      |
| ------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **White-box or Black-box**      | Do we know the model (transitions & rewards)?              | ✅ **White-box** — both require full knowledge of the MDP                                                |
| **Model-based or Model-free**   | Do they need access to a model?                            | ✅ **Model-based** — they rely on knowing ( P(s'                                                         |
| **Static or Dynamic**           | Is the problem fixed or changing over time?                | ✅ **Static** — the environment (P, r) is fixed; they solve for the optimal policy in that setting       |
| **Planning or Learning**        | Are we acting in a known or unknown environment?           | ✅ **Planning** — because everything is known and we compute the solution ahead of acting                |
| **Policy-based or Value-based** | Do we optimize policy directly or through value functions? | Mixed: Policy Iteration = policy-based, Value Iteration = value-based, but both involve both components |

 1. **Policy Iteration Process**

$$
\pi^0 \xrightarrow{PE} V^{\pi^0} \xrightarrow{PI} \pi^1 \xrightarrow{PE} V^{\pi^1} \xrightarrow{PI} \pi^2 \xrightarrow{PE} \cdots \xrightarrow{PI} \pi^*
$$

  According to Policy Improvement Theorem: Value function of the updated policy satisfies monotonicity.
  $$
  V^{\pi^{k+1}}(s) \geq Q\left(s, \pi^{k+1}(s)\right) \geq V^{\pi^k}(s)
  $$

  As long as the number of all possible policies is limited, the policy iteration can converge to the optimal policy

  Since $$|S| < \infty$$$$|A| < \infty$$, # possible policies is $$|A|^{|S|}$$ is limited.

  Policy iteration can find the optimal policy in finite iterations

   **Deterministic** policy:
   Given a MDP with limited action space and state space: $|S| < \infty, |A| < \infty$

- PI based on V

  1. Randomly initialize policy 𝜋
  2. Repeat until convergence {
     a) Calculate $𝑉 ≔ 𝑉^𝜋$ (Updating is time consuming)
     b) For each state 𝑠 ∈ 𝒮, update:
$$
\pi(s) = arg \max_a r(s,a) + \gamma \sum_{s'}P(s'|s,a)V(s')
$$
  }

- PI based on Q
  1. Randomly initialize policy 𝜋
  2. Repeat until convergence {
     a) Calculate $Q ≔ Q^𝜋$ (Updating is time consuming)
     b) For each state 𝑠 ∈ 𝒮, update:
$$
\pi(s) = arg \max_a Q(s,a)
$$
  }

  Skip PI for stochastic policy.


 2. **Value iteration** $\color{Lime} \text{+e.g.}$
   Only one round of value update is carried out in the policy evaluation, and then the policy is upgraded directly according to the updated value.

**Value Iteration (V value)**
1. For each state, initialize V(s)=0
2. Repeat until convergence {
   a) For each state 𝑠 ∈ 𝒮, update:

$$
V(s) = arg \max_a r(s,a) + \gamma \sum_{s'}P(s'|s,a)V(s')
$$

   }
3. Return a deterministic policy
$$
\pi(s) = arg \max_a r(s,a) + \gamma \sum_{s'}P(s'|s,a)V(s')
$$


2.Value Iteration
$$
V_0 \rightarrow V_1 \rightarrow V_2 \rightarrow \cdots \rightarrow V^*
$$
**Value Iteration (Q value)**
5. For each state, initialize Q(s)=0
6. Repeat until convergence {
   a) For each state 𝑠 ∈ 𝒮, update:

$$
Q(s,a) = r(s,a) + \gamma \sum_{s'}P(s'|s,a)\max_{a'}Q(s',a')
$$

   }
3. Return a deterministic policy
$$
\pi(s) = arg \max_a Q(s,a)
$$



 **Synchronous Value Iteration**  
*(stores two copies of value function - updates new using old)*  

1. For all states $$s \in S$$:  
$$
V_{new}(s) \leftarrow \max_{a \in A} \left[ r(s, a) + \gamma \sum_{s' \in S} P(s'|s, a) V_{old}(s') \right]
$$

2. Update:  
$$
V_{old}(s) \leftarrow V_{new}(s)
$$

**Asynchronous Value Iteration**  
*(stores one copy of value function - updates using mixed old/new values)*  

1. For all states $$s \in S$$:  
$$
V(s) \leftarrow \max_{a \in A} \left[ r(s, a) + \gamma \sum_{s' \in S} P(s'|s, a) V(s') \right]
$$
**PI VS. VI**
Value iteration: greedy update method, equivalent to a round of value update in policy evaluation, and then the policy is upgraded directly according to the updated value

In policy iteration, the cost of updating value function by using Bellman equation is very large!

For MDP with **small** space, **policy iteration** usually converges **quickly.**
For MDP with large space, value iteration is more practical, more efficient.

If no state transition loop, best to use value iteration

#### 3.3.3 Optimal policy $\pi^*$

In MDP with limited state and action  space, there is a policy:

$V^{\pi^*}(s)\ge V^{\pi}(s) \text{ for any s} \in S$

Optimal state value f

$$
V^{*}(s) = \max_\pi V^\pi(s) 
\\ = \max_\pi \sum_a \pi(a|s)Q^\pi(s,a) 
\\ = \max_aQ^*(s,a) 
\\ = \max_a r(s,a) + \gamma \sum_{s'}P(s'|s,a)V^*(s')
$$

Optimal action value f

$$
Q^{*}(s,a) = \max_\pi Q^\pi(s,a)
\\ = r(s,a) + \gamma \sum_{s'}P(s'|s,a)V^*(s')
\\ = r(s,a) + \gamma \sum_{s'}P(s'|s,a)\max_a Q^*(s,a)
$$

When value function is optimal, its policy is optimal:
$$V^{*}(s)=V^{\pi^*}(s)\ge V^{\pi}(s) $$
$$
\pi^*(s) = arg \max_a r(s,a) + \gamma \sum_{s'}P(s'|s,a)V^*(s')
$$

### 3.4 Model-based method

MDP<S,A,P,r,$\gamma$>.
In real applications, 𝑃 and 𝑟 are unknown.

Need to learn the state transition probability P and reward r

$$
P(s'|s,a)=\frac{\text{\# take a under s and transfer to s'}}{\text{\# take a under s}}
$$

$$
r(s,a)= \text{avgerage } {r(s,a)^{(i)}}
$$

Algorithm

1. Randomly initialize policy 𝜋
2. Repeat untFil convergence {
   a) Execute 𝜋 in MDP, collect experienced data
   b) Use the collected experience in MDP to update the estimation of 𝑃 and 𝑟
   c) Value iteration by using the estimation of 𝑃 and 𝑟 to get new estimation of value function V
   d) Update policy 𝜋 as greedy policy according to V
   }

-: action space is too large. -> model-free (not learn an MDP, but to learn value function and policy directly from experience).


Symbols:
- $t$: discrete time step.
- $\color{turquoise}\text{s, s' : current state, next state}$,  $\color{turquoise}\text{basis for making the choices}$
- $a$: an action made my the agent
- $\color{turquoise}\text{ r}$: a reward, $\color{turquoise}\text{basis for evaluating the choices}$
- $S$: set of all nonterminal states
- $S^+$: set of all states, including the **terminal state**
- $A(s)$: set of all actions available in state $s$
- $R$: set of all possible rewards, a finite subset of $\mathbb{R}$
- $\rho \subseteq \mathbb{R}$: subset of $\mathbb{R}$
- $|S|$: number of elements in set $S$
- $T, T(t)$ final time step of an episode; the episode including time step t.
- $A(t)$ : Action at t
- $S(t)$ : state at t
- $R(t)$ : reward at t
- $\color{turquoise} \pi$: policy (stochastic decision-making rule),is a $\color{turquoise}\text{mapping from states to actions}$
- $\pi(s)$ : action taken in state s under deterministic policy $\pi$
- $\pi(a|s)$ : <mark> probability </mark> of taking action a in state s under stochastic policy $\pi$
# 4 Model-free method

If a problem cannot be modeled as MDP, it is not a reinforcement learning problem.
Can be modeled does not mean that we know all the parameters.

Here comes the model-free method:

Learn value function and policy directly from experiences.

Key steps:

(1) Estimating value function (Policy evaluation)

(2) Optimizing policy (Policy improvement)/ control

2 kinds of policy learning

on-policy learning:Sampling policy and learning policy is the same!

off-policy: Sampling policy and learning policy is different!

- target policy $\pi(a|s)$: evluate value function $V^\pi(s)$ or $Q^\pi(s,a)$
- Behavior policy $\mu(a|s)$: collect data $\{s_t,a_t,r_t, s_{t+1},...,s_{T-1},a_{T-1},r_{T-1},s_T,a_T,r_T \}～\mu$
- why:
  - Balance exploration and exploitation
  - Learning policy by observing human beings or other agents
  - Experience from reusing old policies
  - Learn the optimal policy when following the policy used in exploration
  - Learn multiple policies when following one policy in exploration
  - An example of MSR research in Cambridge

#### 4.1 Monte Carlo value estimation

MC: repeated random sampling to obtain numerical results.
can only be applied to MDP with finite length (all episode has a terminate state).
learns from the complete episode: no bootstrapping

work in a fragmented (terminated) environment.

must wait for the end of the episode until the cumulative reward is  known

Steps:

1. Sampling a lot of episodes using policy $\pi$
2. For the state 𝑠 of each time step 𝑡 in each episode:Incremental counter 𝑁(𝑠) ←𝑁(𝑠) +1

   Incremental total cumulative reward 𝑀(𝑠) ←𝑀(𝑠) + 𝐺𝑡

   Value is estimated as the average of the cumulative rewards 𝑉(s)=  𝑀(𝑠)/𝑁(𝑠)
3. According to the law of large numbers: $V(s) -> V^\pi(s) \text{ as } N(s) -> \infty$

   Update 𝑉(𝑠) immediately after sampling an episode
4. For each state $𝑠_𝑡$ and its cumulative reward $g_t$

   $$
   N(s_t) \leftarrow N(s_t) +1
   \\ V(s_t) \leftarrow V(s_t) + \frac{1}{N(s_t)}(g_t-V(s_t))
   $$

   For nonn-stationary problems (that is, the environment will change over time), we can track a current average (that is, we don't consider episodes that are too long ago). Take $\alpha$ as a constant.

   $$
   V(s_t) \leftarrow V(s_t) + \alpha(g_t-V(s_t))
   $$
Analogy: You finish a whole chess game before adjusting your opinion about your opening moves.

Analysis:

The cummulative reward $g_t$ is the unbiased estimation of $V(s_t)$

 Good convergence property (This is still true when using functional  approximation)
 Insensitive to initial values
 Easy to understand and use

#### 4.2 Temporal difference

By bootstrapping, TD learns from incomplete fragment.

updates the current prediction value to make it close to  the estimated cumulative reward (untrue value).

works in a continuous (non-terminating) environment.

can do real-time learning at each step.

Steps:

1. Update value function $V(s_t)$, make it close to the estimated cummulative reward (TD target) $r_t+\gamma V(s_{t+1})$. the braket content in the $\alpha$ is the TD error.

$$
V(s_t) \leftarrow V(s_t) + \alpha(\color{green}{r_t+\gamma V(s_{t+1})}- \color{orange}V(s_t))
$$

Analysis:

Real target $r_t+\gamma V^\pi (s_{t+1})$ is the unbiased estimation of $V(s_t)$

TD target $r_t+\gamma V(s_{t+1})$ is biased, $\gamma V(s_{t+1})$ is the current estimation

TD target has a lower variance:

 Cumulative reward: depend on multi-step random action, multi-step state  transition and multi-step reward   TD target: depend on single-step random action, single-step state transition and single-step reward

 Usually more efficient than MC

 TD finally converges to $𝑉^\pi (𝑠_{𝑡+1})$ (but it is not always the case when using function approximation)

 More sensitive to initial values than MC

#### 4.3 Multi-step TD Learning

* Instead of updating based on a single reward, we update using a sum of rewards over **𝑛** steps.
* This helps balance between **speed (shorter horizon)** and **accuracy (longer horizon)**.
* It is useful when time constraints make full-episode learning impractical.
* The update rule still remains model-free because it doesn’t rely on knowing the full environment dynamics.

𝑛 step cummulative reward:

$$
g_t^{(n)}= r_\text{t}+\gamma r_\text{t+1}+...+\gamma^{n-1} R_\text{t+n-1}++\gamma^{n} R_\text{t+n}
$$

𝑛 step TD learning:

$$
V(s_t) \leftarrow V(s_t) + \alpha(g_t^{(n)}-V(s_t))
$$

#### 4.4 Off-policy MC by importance sampling

Evaluate policy 𝜋 using the cumulative rewarded generated by policy 𝜇

Cumulative reward 𝑔𝑡 should be weighted according by the importance ratio between two policies:

Multiply each segment by the importance ratio:

$$
\{s_t,a_t,r_t, s_{t+1},...,s_{T-1},a_{T-1},r_{T-1},s_T,a_T,r_T\}～\mu
\\g_t^{\pi/\mu}=\frac{\pi(a_t|s_t)}{\mu(a_t|s_t)}\frac{\pi(a_{t+1}|s_{t+1})}{\mu(a_{t+1}|s_{t+1})}...\frac{\pi(a_T|s_T)}{\mu(a_T|s_T)}g_t= \prod_{\tau = t}^T \frac{\pi (a_{\tau}|s_{\tau})}{\mu(a_{\tau}|s_{\tau})} g_t
$$

Update value function to approximate revised cumulative reward.

Cannot be used when 𝜋≠0 but 𝜇=0; and significantly increase variance.

$$
V(s_t) \leftarrow V(s_t) + \alpha(g_t^{\pi/\mu}-V(s_t))
$$


#### 4.4 Off-policy MC by importance sampling

TD target is weighted by the importance sampling

$$
V(s_t) \leftarrow V(s_t) + \alpha \left( \frac{\pi(a_t | s_t)}{\mu(a_t | s_t)} (r_t + \gamma V(s_{t+1})) - V(s_t) \right)
$$

Lower variance than MC importance sampling.

The policy only needs to be approximated in a single step.
.

#### 4.5 $\epsilon$ greedy policy improvement

![image.png](pic/epsilongdimp.png)

#### 4.6 Summery

Model-free RL

- On-policy MC:

  $$
  V(s_t) \leftarrow V(s_t) + \alpha (g_t - V(s_t))
  $$
- On-policy TD:

  $$
  V(s_t) \leftarrow V(s_t) + \alpha (r_t + \gamma V(s_{t+1}) - V(s_t))
  $$
- On-policy TD (SARSA):state-action-reward-state-action
  In each time step:

  $$
  Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha (r_t + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t))
  $$

  Policy improvement: 𝝐-greedy

  ![image.png](pic/SARSA.png)
- Off-policy TD (Q-learning):

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha (r_t + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t))
$$

Q learning's objective function:

t, get s_t, a_t, r_t -> Q. $\max_{a'} Q(s_{t+1},a')$ Select a', no need to sample.

$$
r_{t+1} = \gamma Q(s_{t+1}, a'_{t+1})=r_{t+1}+\gamma Q(s_{t+1}, arg \max_{a'} Q(s_{t+1},a'))=r_{t+1}+\gamma \max_{a'}Q(s_{t+1},a')
$$

efficient than SARSA

Do not need importance sampling:

* It **never explicitly computes expectations** over the target policy π, and
* It **doesn’t need to reweight samples** using importance sampling because it directly **uses the greedy action** in its update:

![image.png](pic/QLearning.png)

$\color{Lime} \text{PROOF Q-learning converge 52}$

![image.png](pic/Q-learning convergence.png?t=1743929995986)

# 5 Multi-step bootsrtrapping

折中4, 采样几步就更新几次，剩下的值函数估计

# 6 Value-based DRL

这一讲终于跳脱出了前面传统的强化学习（解决相对简单的问题），用神经网络拟合Q, V函数，适用于更大的状态空间。

focus on learning **how good** a state (or action) is.
We don't directly learn *what action* to take — we learn *values* first.

$\large \color{violet}\text{DQN family}$

Q-Learning: learns a function $Q_\theta(s,a)$ with para $\theta$

- given a segment {(s,a,s',r)}
- $\color{turquoise}\text{target }$ $y=r+\gamma max_\text{a'}Q_\theta(s',a')$
- update:

  $$
  Q_\theta(s,a) \leftarrow Q_\theta(s,a)+\alpha(r+\gamma \max\limits_{a'}Q_\theta(s',a')-Q_\theta(s,a))
  $$

  α后面类似梯度下降
- optimization objective:

  $$
  \theta^* \leftarrow arg \min_\theta E_\text{(s,a,s',r) ∼ U(D)} \frac{1}{2}[(r+\gamma \max\limits_{a'}Q_\theta(s',a'))-Q_\theta(s,a)]^2
  $$

  - $(r+\gamma max_\text{a'}Q_\theta(s',a')$ TD target, no gradient here???
  - $\text{(s,a,s',r) ∼ U(D)}$: a transition **(state, action, next state, reward)** is **randomly sampled** from the replay buffer D using a **uniform distribution** **U**.
  - $Q_\theta(s',a')$ 如果不固定，会连续更新，不稳定

$\color{orange}\text{Deep Q-Networks (DQN)}$ represents Q function $Q_\theta(s,a)$ by using neural networks.

- Input:s.   Not（s,a), because too large
- Last layer: a.  #of elements $|A|$
- Output:(s,a)

-:

- unstable
  - continuously sampled (s,a,s',r) is not IID
  - $Q_\theta(s',a')$ updates freq
- output is discrete (only fit for discrete action space)

sol:

- Experience replay: non IID data -> IID data
  - Store sample $e_t = (s_t, a_t, s_\text{t+1}, r_t)$ in each step of training INTO replay buffer D.
  - Sampling, uniformly distributed
- Build 2 nw:
  - Evaluations nw: $Q_\theta(s,a)$
  - Target nw $Q_{\theta^-}(s,a)$ to compute TD target: synchronize with the evaluation nw every C step

    - $\color{turquoise}\text{target }$ $y=r+\gamma \max\limits_{a'} Q_{\theta^-}(s',a')$

**Algorithm:**

1. Randomly initialize evaluation network $\theta; \theta^- \leftarrow \theta$
2. Initialize experience replay buffer D
3. Repeat until convergence{

- Get initial state $s_0$
- For each step t=0,1,...,T

  - take action $a_t$ by $\epsilon$-greedy based on $Q_\theta$
  - Get reward $r_t$ and the next state $s_{t+1}$
  - Store ($s_t, a_t, s_{t+1}, r_t$) in D
  - If D is large enough, sampling N samples $\{(s_t, a_t, s_{t+1}, r_t)\}^N_{i=1}$
  - For each sample, calculate target $y_i =r_i+ \gamma \max\limits_{a'} Q_{\theta^-}(s_{i+1},a')$
  - Update $\theta$ by minimize loss $L = \frac{1}{2N}\sum_i(y_i-Q_\theta(s_i,a_i))^2$
  - If t mod C=0, then update $\theta^- \leftarrow \theta$
    }

$\color{orange}\text{Double DQN (DDQN)}$,improved version of DQN

Due to the Jensen's inequality, max operation makes the est Q always larger than real Q value. And it will be more serious when #candidate actions increase.

$$
E[\hat Q(s,a)]=Q(s,a) \\E[\max\limits_{a} \hat Q(s,a)] \ge \max\limits_{a} Q(s,a)
$$

$$
\max\limits_{a'}Q_{\theta^-}(s',a')=Q_{\theta^{-}}(s', arg \max\limits_{a'}Q_{\theta^-}(s',a')) \\=E[R|s', arg \max\limits_{a'}Q_{\theta^-}(s',a'),{\theta^-}] \\ \ge \max(E[R|s', a_1,{\theta^-}], E[R|s', a_2,{\theta^-}],...  a_i \in A
$$

$$
\text{Where } E[\max(X_1, X_2)] \ge \max(E[X_1], E[X_2])
$$

In DDQN, $Q_\theta$ is used to select next action.

![image.png](pic/DDQN.png)

$\color{pink}\text{Prioritized Experience Replay}$ : find more experience samples

Calculate the priority $p_t$ (value of learning)

$$
p_t = |r_t + \gamma Q_{\theta^-}(s_{t+1}, arg \max\limits_{a'}Q_\theta(s_\text{t+1},a'))-Q_\theta(s_t,a_t)|
$$

Store experience $e_t = (s_t, a_t,s_\text{t+1},r_t, p_t+\epsilon)$ , $\epsilon$ is the noise for randomness, in replay buffer to give each sample a chance to be sampled.

Prob of $e_t$ being selected is $P(t)=(p_t^\alpha)/(\sum_kp_k^\alpha)$. α for smoothing. (=0 in uniform sampling)

Weight in importance sampling $w_t=(N\times P(t))^{-\beta}/(\max\limits_{i} w_i)$

![image.png](pic/DDQN+pp.png)

$\color{orange}\text{Dueling DQN}$, improved version of DQN. parallel with DDQN

Inputs of s are processed by CNN to extract features.

Core:Advantage funciton A

$$
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)\\Q^\pi(s,a)=E[G_t|s,a]\\V^\pi(s)=E_{a  ∼ \pi(·|s)}[Q^\pi(s,a)]
$$

$V^\pi(s) \text{ is the avagerage value of }Q^\pi(s,a)\text{. }A^\pi(s,a) \text{ measures the effect after taking an action.}$

To obtain V, A separately (fc layer), Q in the DQN is decomposed. And they are combined into Q finally. *Subscript denotes parameters.*

$$
Q_{\theta,\alpha,\beta}(s,a) = V_{\theta,\alpha}(s)+A_{\theta,\beta}(s,a)
$$

However, this version is unstable in training because the non-uniqueness in modeling V and A.

For sol 1, max two sides of Q=V+A (max limits a only operates the f with para a), define the optimal A function($\max\limits_aA(s,a)-\max\limits_aA(s,a)$) equals to 0.

$$
Q(s,a)=V(s)+A(s,a) \\ \max\limits_aQ(s,a)=V(s)+\max\limits_aA(s,a)-\max\limits_aA(s,a)\\V(s)=\max\limits_aQ(s,a)
$$

So is the sol 2.

Therefore the two sols:

1.Set $V_{\theta,\alpha}(s)=\max\limits_{a'}Q_{\theta,\alpha,\beta}(s,a')$

$$
Q_{\theta,\alpha,\beta}(s,a) = V_{\theta,\alpha}(s)+A_{\theta,\beta}(s,a)-\max\limits_{a'}A_{\theta,\beta}(s,a')
$$

2. Set $V_{\theta,\alpha}(s)=\frac{1}{|A|}\sum_{a' \in A}Q_{\theta,\alpha,\beta}(s,a')$

$$
Q_{\theta,\alpha,\beta}(s,a) = V_{\theta,\alpha}(s)+A_{\theta,\beta}(s,a)-\frac{1}{|A|}\sum_{a' \in A}A_{\theta,\beta}(s,a')
$$

The sol ensure the uniqueness of V function,

but not satisfy with the Bellman f, the outputs of A,V,Q of the network are no longer the real A,V,Q.

We do not care of it, because the standard of doing greedy is the order of Q.

The relative order of Q remains the same. s.t.$Q(s,a_1) > Q(s,a_2) \rightarrow A(s,a_1) > A(s,a_2)$$

+ +:

  + Handle states that are less associated with actions. 没人的路上怎么开都行。
  + effective in learning state-value f: one state  value function corresponds to multiple Advantage. functions. Share the same state-value function; Easy Training, fast convergence.
#### 6.3 Challenges in Large MDPs

Maintaining a table of $V(s)$ or $Q(s,a)$ becomes infeasible in large or continuous spaces.

Solutions:
- Discretization: split continuous spaces into grids.
- Bucketing: group similar states.
- Parameterized value functions: approximate $V_\theta(s)$ or $Q_\theta(s,a)$ using models.
#### 6.4 Value Function Approximation

  ??? Approximate $V(s)$ using parameters $\theta$:

  $$Vθ(s)=θTx(s)V_\theta(s) = \theta^T x(s)Vθ(s)=θ^Tx(s)$$
  
  where:

  * $x(s)$ is a feature vector extracted from state $s$.

Objective:

$$J(\theta) = \mathbb{E}_\pi \left[\frac{1}{2}(V_\pi(s) - V_\theta(s))^2\right]$$

Gradient descent update:

$$\theta \leftarrow \theta + \alpha (V_\pi(s) - V_\theta(s)) \nabla_\theta V_\theta(s)$$

If true $V_\pi(s)$ is unknown, use Monte Carlo or TD targets instead.

  > **Advantage**: Approximation generalizes to unseen states. **Weakness**: Bad approximators can give wrong value everywhere!
  > **Analogy**: Instead of remembering every person's favorite food, you learn that *"teenagers like fast food"*. You generalize!
  

# 7 Stochastic Policy Gradient (SPG)

### 7.1 Goal
This chapter considers the neural network (parameters $\theta$) that model the stochastic policy $\pi_\theta(a|s)=\pi_\theta(a|s;\theta)$ directly, which outputs a probability distribution over actions. Notice, the final outcome here does not mean the choose the largest probability.

Value-based RL vs. policy-based RL:
	value-based: 
		visit (s,a) to find Q(s,a)
		slower (compare and find the large a col by col: $a^* = \max_\limits{a} Q(s,a)$ ), discrete A.
	policy-based:
		having s then can have a -> generalization ability (generalize the visible known state to the unknown state.)
		efficient in high-dimensional, continuous A.
		can learn stochastic policy by $\color{red}\text{stochastic policy gradient (SPG)}$.
		better convergence property but usually converges into the local minimum. Because, NN is non-convex (gradient formula), non linearity.
		inefficient in evaluation policy, and having large variance.
 
### 7.2 SPG

Stochastic policy $\pi_\theta(a|s)=\pi_\theta(a|s;\theta)=P(a|s;\theta)$
Trajectory $\tau$ is sampled by $\pi_\theta$: $\tau = \{s_0,a_0,r_0,...\}\sim \pi_\theta$ 
Total return of the $\tau$  
$$J(\pi_\theta)=E_{ \pi_\theta}[\sum_{t=0}^{\infty}\gamma^t r(S_t,A_t)]=E_{ \pi_\theta}[\sum_{t=0}^{\infty}\gamma^t r_t]$$
the policy is determined by $\theta$:
$$
\begin{aligned}
J(\theta) &= \mathbb{E}_{\tau \sim \pi_\theta(\tau)}[G(\tau)] \\
&= \mathbb{E}_{\tau \sim \pi_\theta(\tau)}\left[\sum_{t=0}^{\infty} \gamma^t r(s_t, a_t)\right] \\
&= \mathbb{E}_{\pi_\theta}\left[\sum_{t=0}^{\infty} \gamma^t r(S_t, A_t)\right] \\
&= \mathbb{E}_{(s, a) \sim \hat{\rho}^{\pi_\theta}}[r(s, a)] \\
&= \frac{1}{1 - \gamma} \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[r(s, a)] \\
&= \mathbb{E}_{s_0 \sim v_0}[V^{\pi_\theta}(s_0)]
\end{aligned}
$$
	where, $v_0$ is the distribution of the initial states
	
$\color{red}\text{Goal}$: Gradient ascent to maximize the $J(\theta)$

  1-step MDP:

Starting state 𝑠\~𝑑(𝑠),The MDP ends after one-step decision-making, and reward is 𝑟(𝑠,𝑎)


$$
\begin{aligned}
J(\theta) &= \mathbb{E}_{s \sim d, a \sim \pi_\theta(·|s)}[r(s,a)] \\
&= \sum_s v^{\pi_\theta}(s) \sum_a \pi_\theta(a|s)r(s,a)
\end{aligned}$$
where $v(s)$ is the stationary distribution under policy $\pi$.

Gradient: Notice, $\pi_\theta$ is a function. $\log \pi_\theta$ is a composite function.
$$\begin{aligned}
\frac{\partial \pi_\theta(a|s)}{\partial\theta} 
&= \pi_\theta(a|s) \cdot \frac{1}{\pi_\theta(a|s)} \frac{\partial \pi_\theta(a|s)}{\partial\theta} 
&& \text{(Multiply by 1 in a clever way)} \\
&= \pi_\theta(a|s) \cdot \frac{\partial \log \pi_\theta(a|s)}{\partial\theta} \cdot\frac{\partial\theta}{\partial \pi_\theta(a|s)} \cdot\frac{\partial \pi_\theta(a|s)}{\partial\theta} 
&& \text{Using } \frac{d}{dx}\log f(x) = \frac{f'(x)}{f(x)} \\
&= \pi_\theta(a|s) \cdot \nabla_\theta \log \pi_\theta(a|s)
&& \text{(Final policy gradient form)}
\end{aligned}$$

$$
\begin{aligned}
\nabla_\theta J(\theta) 
&= \sum_{s \in S} d(s) \sum_{a \in A} \frac{\partial \pi_\theta(a|s)}{\partial \theta} r(s,a) \\
&= \sum_{s \in S} d(s) \sum_{a \in A} \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s) r(s,a) \\
&= \mathbb{E}_{s \sim d(s), a \sim \pi_\theta(s)} \left[ \nabla_\theta \log \pi_\theta(a|s) \cdot r(s,a) \right]
\end{aligned}
$$
---
#### Policy gradient theorem

For any differential policy $\pi_\theta(a|s)$
$$
\begin{aligned}
\nabla_\theta J(\theta) &=\mathbb{E}_{(s, a) \sim \hat{\rho}^{\pi_\theta}}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot Q^{\pi_\theta}(s,a) \right] \\
&\propto \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot Q^{\pi_\theta}(s,a) \right]
\end{aligned}$$
Parameters are put in into the learning rate.

- policy gradient algorithm: on-policy, sampling by $\pi_\theta$
---

Go deeper into the calculation of the gradient.
The NN-implemented scoring function $$f_\theta(s,a)$$
For a stochastic policy in a continuous action problem (does not cover in this lecture):
$$
\pi_\theta(a|s) \propto exp\{(a-f_\theta(s))^2\}$$
For a stochastic policy in a discrete action problem, the probability of sampling an action is implemented by softmax:
$$
\begin{aligned}
&\pi_\theta(a|s) = \frac{e^{f_\theta(s,a)}}{\sum_{a'} e^{f_\theta(s,a')}}\\

& \log \pi_\theta(a|s) = \log e^{f_\theta(s,a)} - \log {\sum_{a'} e^{f_\theta(s,a')}}= f_\theta(s,a) - \log {\sum_{a'} e^{f_\theta(s,a')}}\\

& \nabla_\theta \log \pi_\theta(a|s) = \frac{\partial f_\theta(s,a)}{\partial} - \nabla_\theta \log {\sum_{a'} e^{f_\theta(s,a')}}
\end{aligned}
$$
$$
\begin{aligned}

\nabla_\theta \log {\sum_{a'} e^{f_\theta(s,a')}} &= \frac{1}{\sum_{a'} e^{f_\theta(s,a')}} \cdot\nabla_\theta {\sum_{a'} e^{f_\theta(s,a')}} \\

&= \frac{1}{\sum_{a''} e^{f_\theta(s,a'')}} \cdot {\sum_{a'} e^{f_\theta(s,a')}} \cdot \nabla_\theta f_\theta(s,a')\\

&= \sum_{a'}(\frac{e^{f_\theta(s,a')}}{\sum_{a''} e^{f_\theta(s,a'')}}\nabla_\theta f_\theta(s,a'))\\

&= \sum_{a'} \pi_\theta(a'|s)\nabla_\theta f_\theta(s,a')\\

&= \mathbb{E}_{a' \sim \pi_\theta(·|s)} \nabla_\theta f_\theta(s,a')
\end{aligned}
$$
So,
$$
\nabla_\theta \log \pi_\theta(a|s) =\nabla_\theta f_\theta(s,a) - \mathbb{E}_{a' \sim \pi_\theta(·|s)} \nabla_\theta f_\theta(s,a')
$$
The policy gradient theorem can be derived into:
$$
\begin{aligned}
\nabla_\theta J(\theta) &=\mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot Q^{\pi_\theta}(s,a) \right]\\
& = \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}\left[ (\nabla_\theta f_\theta(s,a) - \mathbb{E}_{a' \sim \pi_\theta(·|s)} \nabla_\theta f_\theta(s,a')) \cdot Q^{\pi_\theta}(s,a) \right]

\end{aligned}
$$
The next step is to estimate the Q.

### 7.3 REINFORCE Algorithm： MC policy gradient
Cumulative reward $g_t$ to estimate $Q^{\pi_\theta} (s_t,a_t)$, by running multiple rollout (sampling multiple episode) ->  full-episode returns ->high variance, slow learning.

The variance can be reduced in some sense by the baseline $b(s)$, typically $b(s)=V_w(s)$, and it will not cause the bias. Reason:
$$
\begin{aligned}
\nabla_\theta J(\theta) &\propto \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[ 
\nabla_\theta \log \pi_\theta(a|s) \cdot (Q^{\pi_\theta}(s,a)-b(s))]\\

&= \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)]
- \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)b(s)]\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s) \sum_a \pi_\theta(a|s)\nabla_\theta\log \pi_\theta(a|s)b(s)\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s)b(s) \sum_a \pi_\theta(a|s) \nabla_\theta\log \pi_\theta(a|s)\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s)b(s) \sum_a  \nabla_\theta \pi_\theta(a|s)\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s)b(s) \nabla_\theta \sum_a  \pi_\theta(a|s)\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s)b(s) \nabla_\theta 1\\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)] - \sum_s v^{\pi_\theta}(s)b(s) \cdot0 \\

&=  \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}[\nabla_\theta\log \pi_\theta(a|s)Q^{\pi_\theta}(s,a)]

\end{aligned}
$$
The best baseline is $V^\pi(s)$. 
	- **Implementation**: Requires learning an additional value function network (essentially forming the foundation of **Actor-Critic methods**). The critic (Vπ(s)Vπ(s)) is trained via supervised regression (e.g., MSE) to predict expected returns. 
	- **Empirical Impact**: In practice, using Vπ(s)Vπ(s) as a baseline can **reduce variance by 10× or more**, depending on task complexity and reward scaling.

#### REINFORCE (Standard Policy Gradient)
1. **Repeat until convergence**:
   - **a)** Generate an episode $\{s_0, a_0, r_0, \cdots, s_T, a_T, r_T\} \sim \pi_\theta$
   - **b)** For each step $t = 0, 1, \cdots, T$:
     - $g_t \leftarrow \sum_{\tau=t}^T \gamma^{\tau-t} r_\tau$
     - $\theta \leftarrow \theta + \alpha g_t \nabla_\theta \log \pi_\theta (a_t | s_t)$

#### REINFORCE (with b(s))
1. **Episode generation**:
   - **a)** Generate an episode $\{s_0, a_0, r_0, \cdots, s_T, a_T, r_t\} \sim \pi_\theta$
2. **For each step $t = 0, 1, \cdots, T$**:
   - $g_t \leftarrow \sum_{\tau=1}^T r^{2-\tau} t_\tau$
   - $\delta_t \leftarrow g_t - V_W(s_t)$
   - $w \leftarrow w + \alpha^w \delta_t \nabla_w V(s_t)$
   - $\theta \leftarrow \theta + \alpha^\theta \delta_t \nabla_\theta \log \pi_\theta (a_t | s_t)$
   
Still having problems: task needs to have a terminate state before REINFORCE, Low data utilization efficiency, High training variance (imp defect).

### 7.4 Actor-Critic
Build a trainable action-value function $Q_\phi$ to replace the Q estimation.
Actor network $\pi_\theta$ learns to take actions to satisfy the critic. Loss:
$$L(\phi)=\frac{1}{2} (r_t+\gamma Q_\phi(s_{t+1},a_{t+1})-Q_\phi(s_t,a_t))^2$$
Critic $Q_\phi(s,a)$ learns to accurately estimate the value function of the actions taken by policies.  Policy gradient
$$\nabla_\theta J(\theta) \propto \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot Q^{\pi_\theta}(s,a) \right]$$
#### Actor-Critic Algorithm
1. **Initialize parameters**:
   - Randomly initialize policy parameters $\theta$ (Actor), $\phi$ (Critic)
1. **Repeat until convergence**:
   - a) Start from initial state $s_0$, take action $a_0 \sim \pi_\theta(\cdot|s_0)$
   - b) For each step $t = 0, 1, \cdots, T$:
     - Receive reward $r_t$ and next state $s_{t+1}$
     - Take next action $a_{t+1} \sim \pi_\theta(\cdot|s_{t+1})$
     - **Compute TD error**:
       $$\delta_t \leftarrow r_t + \gamma Q_\phi(s_{t+1}, a_{t+1}) - Q_\phi(s_t, a_t)$$
     - **Update Actor (policy)**:
       $$\theta \leftarrow \theta + \alpha \nabla_\theta \log \pi_\theta(a_t|s_t) Q_\phi(s_t, a_t)$$
     - **Update Critic (value function)**:
       $$\phi \leftarrow \phi + \beta \delta_t \nabla_\phi Q_\phi(s_t, a_t)$$
1. **Note**: This is essentially a Deep Learning version of SARSA, using the transition tuple $(s_t, a_t, r_t, s_{t+1}, a_{t+1})$. On-policy.
   It can be -> off-policy with importance sampling.
![[AC.png]]
### Advantage Actor-Critic (A2C)
Standardize critics' scores by subtracting a baseline function,
reduce the probability of poor action and improve the probability of good action,
reduce the variance, speed up convergence.

Advantage function $A^\pi = Q^\pi(s,a)-V^\pi(s)$
$$\nabla_\theta J(\theta) \propto \mathbb{E}_{(s, a) \sim \rho^{\pi_\theta}}\left[ \nabla_\theta \log \pi_\theta(a|s) \cdot A^{\pi}(s,a) \right]$$
$$
\begin{aligned}
A^\pi &= Q^\pi(s,a)-V^\pi(s)
\\ &= {r(s,a)+ \gamma E_{s'∼P(⋅∣s,a)} [V^{\pi} (s')]}-V^\pi(s)

\end{aligned}
$$
#### Training: $V^{\pi_\theta}(s) \approx V_\phi(s)$
1. **TD Error Calculation**:
   - Compute temporal difference (TD) error using current critic $V_\phi$:
     $$
     \delta_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
     $$
     where $s_{t+1}$ is the sampled next state.
1. **Actor Update**:
   - Update policy parameters $\theta$ using the advantage estimate:
     $$
     \nabla_\theta J(\theta) \approx \nabla_\theta \log \pi_\theta(a_t|s_t) \cdot \delta_t
     $$
     (Here $\delta_t$ serves as an estimate of the advantage function $A(s_t,a_t)$)
2. **Critic Update**:
   - Minimize the mean squared TD error:
     $$
     \mathcal{L}(\phi) = \frac{1}{2} \left( r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t) \right)^2
     $$
![[A3C.png]]
![[A3C alg.png]]
### 7.5 TRPO (Trust Region Policy Optimization)
When the policy network is a deep model, updating the parameters along the policy gradient is likely to cause the policy to suddenly deteriorate significantly due to the long step size, affecting the training effect.

TRPO (Trust region policy optimization): Find a trust region when updating, when updating policies in this region, you can get a certain security guarantee of policy performance. Proposed in 2015. Theoretically, guarantee the monotonicity (单调性) of policy learning, and achieved better results than the policy gradient algorithm in practical application.

weakness of policy gradient: Difficult to determine a good step size. The distribution of collected data will change with the update of the policy. Poor step size has great influence.

$$
\begin{aligned}
\max_\theta \quad & \mathbb{E}_{s \sim \rho_{\pi_{\text{old}}}, a \sim \pi_{\text{old}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\text{old}}(a|s)} A^{\pi_{\text{old}}}(s, a) \right] \\\\
\text{s.t.} \quad & \mathbb{E}_{s \sim \rho_{\pi_{\text{old}}}} \left[ \text{KL}[\pi_{\text{old}}(\cdot|s) \| \pi_\theta(\cdot|s)] \right] \leq \delta
\end{aligned}
$$

Where:
- $A^{\pi_{\text{old}}}(s, a)$: Advantage function under the old policy
- $\rho_{\pi_{\text{old}}}$: State visitation distribution of the old policy
- $\delta$: Maximum allowed average KL-divergence between old and new policies
### Features
- Ensures monotonic policy improvement under mild assumptions
- Uses **second-order optimization techniques**
- Computationally more expensive due to Fisher matrix and KL constraint enforcement
### 7.6 Proximal Policy Optimization (PPO)

#### Motivation

PPO simplifies TRPO by replacing the hard trust region constraint with a **soft clipping mechanism**. It retains the benefits of stable policy updates while being much easier to implement and more computationally efficient.
#### Objective

PPO maximizes a clipped surrogate objective:

$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min \left( r_t(\theta) A_t, \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) A_t \right) \right]
$$

Where:
- $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\text{old}}(a_t|s_t)}$: Importance sampling ratio
- $A_t$: Advantage estimate at time \( t \)
- $\epsilon$: Clipping range parameter (e.g., 0.1 or 0.2)
#### Features
- Simple first-order optimization
- Avoids large policy updates via clipping
- Strong empirical performance across many RL environments
- Often used with GAE (Generalized Advantage Estimation)
#### 🔸 Comparison

| Feature                  | TRPO                                   | PPO                                      |
|--------------------------|----------------------------------------|------------------------------------------|
| Action Space             | Continuous/Discrete                    | Continuous/Discrete                      |
| Optimization             | Constrained (Trust Region)             | Unconstrained (Clipped)                  |
| Stability                | Very High                              | High                                     |
| Efficiency               | Lower (second-order method)            | Higher (first-order gradient descent)    |
| Implementation           | Complex                                | Simple                                   |

# 8 Deterministic Policy Gradient (DPG)

Deterministic policy $$a=\mu_\theta(s)$$
In discrete action prob: undifferentiable
$$
\mu_\theta = arg \max_a Q_\theta(s,a)
$$
In continuous action prob: differentiable (this lec)
$$
a = \mu_\theta(s)
$$
In previous RL algorithms:
REINFORCE & Actor-Critic (TRPO, PPO): All of them are on-policy; their sample efficiency is relatively low.
DQN: Off-policy, but only deal with the environment with limited action space because of maximizing Q-function.
So off-policy, unlimited (continuous) action space? DPG.

---

**Deterministic on-policy learning objective.**
$$
\begin{aligned}
J(\theta) &= \mathbb{E}_{\tau \sim \mu_\theta(\tau)}[G(\tau)]\\
&= \mathbb{E}_{s_0 \sim v_0}[V^{\mu_\theta}(s_0)] \\
&= \mathbb{E}_{s_0 \sim v_0}[Q^{\mu_\theta}(s_0, \mu_\theta(s_0))] \\
&= \mathbb{E}_{s \sim \hat v^{\mu_\theta}}[r(s, \mu_\theta(s))] \\
&= \frac{1}{1-\gamma}\mathbb{E}_{s \sim v^{\mu_\theta}}[r(s, \mu_\theta(s))] \\
\end{aligned}
$$
**Deterministic policy gradient theorem (on-policy)**
$$
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim \hat v^{\mu_\theta}}\left[\nabla_\theta \mu_\theta(s) \nabla_a Q^{\mu_\theta}(s,a)\big|_{a=\mu_\theta(s)}\right]
$$

**Deterministic off-policy learning objective**
$$
\begin{aligned}
J_\beta(\theta) 
&= \mathbb{E}_{s_0 \sim \hat v^{\pi_\beta}}[V^{\mu_\theta}(s_0)] \\
&= \int_S \hat{v}^{\pi_\beta}(s) V^{\mu_\theta}(s) \, ds \\
&= \int_S \hat{v}^{\pi_\beta}(s) Q^{\mu_\theta}(s,\mu_\theta(s)) \, ds
\end{aligned}
$$
**Deterministic policy gradient theorem (off-policy)**
$$
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim \hat v^{\mu_\beta}}\left[\nabla_\theta \mu_\theta(s) \nabla_a Q^{\mu_\theta}(s,a)\big|_{a=\mu_\theta(s)}\right]
$$
---

#### 8.1. Deterministic Actor-Critic Training Comparison
 On-Policy (SARSA-style)
1. **Sampling**:  
   Collect transitions using current policy $\mu_\theta$:  
   $\{s_t, a_t, r_t, s_{t+1}, a_{t+1}\} \sim \mu_\theta$

2. **TD Error**:  
   Compute SARSA-style TD target:  
   $\delta_t = r_t + \gamma Q_\phi(s_{t+1}, a_{t+1}) - Q_\phi(s_t, a_t)$

3. **Actor Update**:  
   Update policy parameters via deterministic policy gradient:  
   $\theta \leftarrow \theta + \alpha \nabla_\theta \mu_\theta(s_t) \cdot \nabla_a Q_\phi(s_t, a)\big|_{a=a_t}$  
   *(Uses actions sampled from $\mu_\theta$)*

4. **Critic Update**:  
   Minimize TD error (MSE loss):  
   $\phi \leftarrow \phi + \beta \delta_t \nabla_\phi Q_\phi(s_t, a_t)$  
   $\text{Loss} = \frac{1}{2} \delta_t^2$

 **Off-Policy (Q-learning-style)**
4. **Sampling**:  
   Collect transitions using behavior policy $\pi_\beta$:  
   $\{s_t, a_t, r_t, s_{t+1}\} \sim \pi_\beta$

5. **TD Error**:  
   Compute Q-learning-style TD target:  
   $\delta_t = r_t + \gamma Q_\phi(s_{t+1}, \mu_\theta(s_{t+1})) - Q_\phi(s_t, a_t)$  
   *(Uses target policy's action $\mu_\theta(s_{t+1})$ instead of sampled $a_{t+1}$)*

6. **Actor Update**:  
   Update policy parameters similarly but with off-policy actions:  
   $\theta \leftarrow \theta + \alpha \nabla_\theta \mu_\theta(s_t) \cdot \nabla_a Q_\phi(s_t, a)\big|_{a=\mu_\theta(s_t)}$

7. **Critic Update**:  
   Same as on-policy:  
   $\phi \leftarrow \phi + \beta \delta_t \nabla_\phi Q_\phi(s_t, a_t)$

---
#### 8.2 Compatible Function Approximation
当函数 $Q_\phi(s,a)$ 和策略 $\mu_\theta(s)$ 满足以下两个条件时，称为兼容compatible的：

 1. Q 梯度与 $\mu_\theta(s)$ 用线性关系估计
$$
\nabla_a Q_\phi(s, a) \big|_{a = \mu_\theta(s)} = \nabla_\theta \mu_\theta(s)^T \phi
$$

2. 均方误差最小化
$$
\phi \text{ minimize the mean-squared error: } \text{MSE}(\theta, \phi) = \mathbb{E}\left[ \epsilon(s; \theta, \phi)^T \epsilon(s; \theta, \phi) \right]
$$
where $$
\epsilon(s; \theta, \phi) = \nabla_a Q_\phi(s, a)\big|_{a = \mu_\theta(s)} - \nabla_a Q^{\mu_\theta}(s, a)\big|_{a = \mu_\theta(s)}
$$
---
e.g. $$
Q_\phi(s, a) = x(s, a)^T \phi
$$

where
$$
x(s, a)^T = a^T \nabla_\theta \mu_\theta(s)
$$
#### 8.3 Deep Deterministic Policy Gradient (DDPG)
solve the unstability of AC with neural function approximator, combines DPG and DQN.
key words: experience replay (off-policy), target networks, batch normalization Q-network before action input. add continuous noise.
![[DDPG.png]]
#### 8.4 Twin delayed DDPG (TD3)
Overestimation problem exists in DDPG.
Learn two (twin) critics simultaneously, select the smaller Q estimation to avoid overestimation.
Smooth the policy’s output, make it difficult to exploit the vulnerability of the Q function.
Actor is updated at a lower frequency and critic is updated at a higher frequency. Usually, Critic : Actor = 2 : 1
![[TD3.png]]
#### 8.5 Maximum Entropy RL
For the deterministic policy of continuous action, gradient can be directly returned to the action from the critic, and then the gradient can be further returned to policy network through the chain rule.

Soft Q-Learning and Soft AC are very popular, and they are equivalent.

Policy’s entropy is regarded as a part of the reward, which encourages the diversity, encourages exploration, and improves the robustness to environmental changes

1. **Entropy**: measure of randomness of distribution
$$\mathcal{H}(p) = \mathbb{E}_{x \sim p} [-\log p(x)]$$

Maximum Entropy Principle: Under known conditions or constraints, the selected probability distribution should maximize the entropy (that is, uncertainty or information), so as to minimize the influence from one's own assumptions or prejudices. 事情有余地。

2. **Maximum entropy RL**
$$\pi^* = \arg \max_{\pi} \mathbb{E}_{\tau \sim \pi(\tau)} \left[ \sum_{t=0}^{\infty} \gamma^t \left( r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot | s_t)) \right) \right]$$

其中：
- $\alpha > 0$ is Entropy regularization coefficient
- 离散动作空间熵：$\mathcal{H}(\pi(\cdot | s_t)) = -\sum_a \pi(a|s_t) \log \pi(a|s_t)$, The bigger 𝛼 is, the more exploratory it is
- 连续动作空间熵：$\int_{-\infty}^{\infty} \pi(x|s_t) \log \pi(x|s_t) dx$

**3.Energy-Based Model, EBM)**
Objective:
$$\max_{p} \mathbb{E}_{x \sim p} [\phi(x)] + \alpha\mathcal{H}(p)$$

The optimal dist. Boltzmann:
$$p^*(x) = \frac{\exp(-\phi(x)/\alpha)}{Z}$$
where：
- $Z$ is the partition function
- $\epsilon(x) = -\phi(x)/\alpha$ is the energy function

4. **Soft Value Functions**
Soft means “entropy-regularized"
(Soft) State-value function
  $$V_{soft}^{\pi}(s) = \mathbb{E}_{\tau \sim \pi(\tau)} \left[ \sum_{t=0}^{\infty} \gamma^t \left( r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot | s_t)) \right) | s_0 = s \right]$$
  
  (Soft) Action-value function
  $$Q_{soft}^{\pi}(s,a) = r(s,a) + \mathbb{E}_{\tau \sim \pi(\tau)} \left[ \sum_{t=1}^{\infty} \gamma^t \left( r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot | s_t)) \right) | s_0 = s, a_0 = a \right]$$
Soft Bellman Equation
$$
\begin{aligned}
V_{soft}^\pi(s) &= \mathbb{E}_{a \sim \pi(\cdot|s)}[ Q_{soft}^\pi(s,a)]+ \alpha \mathcal{H}(\pi(\cdot|s))\\
&= \mathbb{E}_{a \sim \pi(\cdot|s)} [ Q_{soft}^\pi(s,a) - \alpha \log \pi(a|s)] \\
\end{aligned}
$$

$$
\begin{aligned}
Q_{soft}^\pi(s,a) &= r(s,a) + \gamma \mathbb{E}_{s' \sim p(\cdot|s,a)} \left[ V_{soft}^\pi(s') \right] \\
&= r(s,a) + \gamma \mathbb{E}_{s' \sim p(\cdot|s,a)} \left[ \mathbb{E}_{a' \sim \pi(\cdot|s')} \left[ Q_{soft}^\pi(s',a') \right] + \alpha \mathcal{H}(\pi(a'|s')) \right]\\
&= r(s,a) + \gamma \mathbb{E}_{s' \sim p(\cdot|s,a)} \left[ \mathbb{E}_{a' \sim \pi(\cdot|s')} \left[ Q_{soft}^\pi(s',a') - \alpha \log \pi(a'|s') \right] \right]
\end{aligned}
$$

5. soft Q-Learning
discrete action space
目标函数：
$$L(\theta) = \mathbb{E}_{(s,a,s',r)\sim U(D)} \frac{1}{2} \left[ (r + \gamma V_{\theta^-}(s')) - Q_\theta(s,a) \right]^2$$

**连续动作空间挑战**：
- 需要近似采样：$\pi(\cdot | s_t ) = \exp(Q_\theta(s_t, \cdot)/\alpha) / Z(s_t)$
- 使用Stein变分梯度下降(SVGD)等方法

---
![[coop_notes/AI/DeepReinforcementLearning/pic/softQ.png]]
6. soft Actor-Critic (SAC)
- Actor网络：$\pi_{\theta}$
- 双Critic网络：$Q_{w1}$, $Q_{w2}$
	Critic损失：
$$L_Q(w) = \mathbb{E}_{(s,a,s',r)\sim U(D), a' \sim \pi_{\theta}(s')} \frac{1}{2} \left[ Q_w(s,a) - (r + \gamma (\min_{j=1,2} Q_{wj}(s',a') - \alpha \log \pi_{\theta}(a'|s'))) \right]^2$$

	Actor损失（使用重参数化技巧）：
$$\hat{a}_{\theta}(s,\xi) = \tanh(\mu_{\theta}(s) + \sigma_{\theta}(s) \odot \xi), \quad \xi \sim \mathcal{N}(0,I)$$
$$L_{\pi}(\theta) = \mathbb{E}_{s\sim U(D), \xi \sim \mathcal{N}(0,I)} \left[\alpha \log \pi_{\theta}(\hat{a}_{\theta}(s,\xi)|s) - \min_{j=1,2} Q_{wj}(s,\hat{a}_{\theta}(s,\xi))\right]$$

7. Adaptive Entropy Regularization)
	goal
$$\max_{\pi} \mathbb{E}_{\tau \sim \pi(\tau)} \left[ \sum_{t=0}^{\infty} \gamma^t r(s_t, a_t) \right]$$
	约束条件：
$$\mathbb{E}_{(s,a) \sim \rho^\pi} [-\log \pi(a|s)] \geq \mathcal{H}_0$$

	自适应调整
$$\mathcal{L}(\alpha) = \mathbb{E}_{s \sim U(D), a \sim \pi(\cdot|s)} [\alpha (-\log \pi(a|s) - \mathcal{H}_0)]$$

| 方法   | 动作空间  | 核心创新      | 主要优势  |
| ---- | ----- | --------- | ----- |
| 软Q学习 | 离散/连续 | 能量基策略     | 强探索性  |
| SAC  | 连续    | 双Q网络+自适应熵 | 稳定高效  |
| 传统RL | 任意    | 无熵正则      | 可能欠探索 |
# 9 Model-based RL
#### 9.1 Review: Learn an MDP Model
- **Motivation**: In real applications, the MDP model (state transition $P$ and reward function $r$) is often unknown. We need to learn it from observed episodes.
- **Key Steps**:
  1. **State Transition Probability**:  
     $$P(s'|s, a) = \frac{\text{Count}(s \rightarrow a \rightarrow s')}{\text{Count}(s \rightarrow a)}$$  
     This estimates the probability of transitioning to state $s'$ after taking action $a$ in state $s$.
  2. **Reward Function**:  
     $$r(s, a) = \text{average}\{r(s, a)^{(i)}\}$$  
     Computes the expected immediate reward for taking action $a$ in state $s$.

- **Advantages**:
  - Enables planning without direct interaction with the environment.
  - Efficient use of data by generalizing from observed transitions.
- **Weaknesses**:
  - Requires sufficient data to accurately estimate probabilities.
  - Sensitive to incomplete or noisy observations.
## 9.1 Model Classification
- **Distribution Model**: Provides all possible outcomes and their probabilities.  
  - Example: Predicting all possible sums of dice rolls.
- **Sample Model**: Generates a single outcome based on probabilities.  
  - Example: Rolling dice once to get one sum.

- **Advantages of Sample Model**: Computationally cheaper for large state spaces.
- **Weaknesses of Distribution Model**: High memory and computation requirements for complex environments.
## Planning & Learning: Introduction&Sampling&Decision-time Planning
## 9.2 Planning
- **Definition**: Planning is the process of using a model to derive a policy.
- **Types**:
  - **State-space Planning**: Searches for the optimal policy in the state space (focus of the course).
  - **Plan-space Planning**: Searches in the plan space (e.g., genetic algorithms).

- **General Framework**:
  1. Simulate experiences using the model.
  2. Update the value function using simulated data.
  3. Improve the policy based on the updated value function.

- **Example**: Dynamic Programming  
  Formula:  
  $$V(s) \leftarrow \max_a \left[ r(s, a) + \gamma \sum_{s'} P(s'|s, a) V(s') \right]$$

## 9.3 Dyna Framework
- **Integration**: Combines planning, learning, and acting.
- **Steps**:
  1. Interact with the environment to collect real experiences.
  2. Update the model using real experiences.
  3. Simulate experiences using the model.
  4. Update the value function and policy using both real and simulated experiences.

- **Algorithm: Dyna-Q**:
  1. Initialize $Q(s, a)$ and the model.
  2. Repeat:
     - Take action $a$, observe $r$ and $s'$.
     - Update $Q(s, a)$ using real experience.
     - Update the model with $(s, a, r, s')$.
     - Perform $n$ planning steps using simulated experiences.

- **Advantages**:
  - Balances exploration and exploitation.
  - Improves sample efficiency by leveraging simulated data.
- **Weaknesses**:
  - Model inaccuracies can propagate errors.
## 9.4 Sampling Methods
- **Uniform Random Sampling**: Updates all states equally, which can be inefficient.
- **Priority Sampling**: Focuses updates on states with significant value changes.
  - Formula for priority:  
    $$P \leftarrow \left| r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right|$$

- **Advantages of Priority Sampling**:
  - Faster convergence by prioritizing important updates.
- **Weaknesses**:
  - Requires maintaining a priority queue, adding computational overhead.
## 9.5 Expected vs. Sample Updates
- **Expected Update**:  
  $$Q(s, a) \leftarrow \sum_{s'} P(s'|s, a) \left[ r + \gamma \max_{a'} Q(s', a') \right]$$  
  - Advantages: Accurate, unbiased.  
  - Weaknesses: Computationally expensive.

- **Sample Update**:  
  $$Q(s, a) \leftarrow Q(s, a) + \alpha \left( r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right)$$  
  - Advantages: Computationally cheap.  
  - Weaknesses: Subject to sampling error.
## 9.6 Trajectory Sampling
- **Definition**: Samples trajectories based on the current policy.
- **Advantages**:
  - Focuses on relevant states.
  - Efficient for deterministic environments.
- **Weaknesses**:
  - May overfit to frequently visited states.
## Model-based Deep Reinforcement Learning
## 9.7 Model-based Deep RL (MBRL)
- **Key Questions**:
  1. How to train a deep model accurately?
  2. When to trust the model?
  3. How to use the model to improve policy training?
  4. Does the model improve data efficiency?

- **Approaches**:
  - **Model Predictive Control (MPC)**: Plans actions using the model without learning a policy.
  - **MBPO (Model-based Policy Optimization)**: Uses branched rollouts to balance model error and sample efficiency.
    - Formula for policy improvement:  
      $$\eta[\pi] \geq \hat{\eta}[\pi] - C(\epsilon_m, \epsilon_\pi)$$  
      where $C$ bounds the error due to model inaccuracies.

- **Advantages of MBRL**:
  - Higher sample efficiency than model-free methods.
- **Weaknesses**:
  - Sensitive to model errors, especially in stochastic environments.
## PETS (Probabilistic ensembles with trajectory sampling)
In this ensemble, each single model is Gaussian process built by neural networks
1. uncertainty: epistemic (model var 认知不确定性，很少数据认识不到位), aleatoric (stochastic env 环境不确定性)
2. To capture two uncertainty construct B NNs with the same network framework：Inputs are all state-action pairs, and outputs are the mean vector and covariance matrix in the next state  Their parameters are randomly initialized in different ways, and different data are randomly sampled from real data for training every time
3. Trajectory sampling: Choose one model from B NNs in each prediction  Sampling a trajectory (simulated)will use multiple environmental model. Reduce the variance.
4. Simulated data -> train the agent
## MBPO
1. Initialize policy 𝜋𝜙, predictive model 𝑃𝜃, env. Dataset 𝒟𝑒𝑛𝑣, and model dataset 𝒟𝑚𝑜𝑑𝑒𝑙 2. Repeat 𝑁 epochs { a) Train model 𝑃𝜃 on 𝒟𝑒𝑛𝑣 via maximum likelihood b) For step 𝑡=1→𝑇 { Interact with the environment by policy 𝜋𝜙 Add generated trajectories into 𝒟𝑒𝑛𝑣 For M model rollouts { Sample state 𝑠𝑡 uniformly from 𝒟𝑒𝑛𝑣 Perform 𝑘-step model rollout by PETS starting from 𝑠𝑡 using policy 𝜋𝜙 on model 𝑃𝜃 Add the generated trajectory into 𝒟𝑚𝑜𝑑𝑒𝑙 } For G gradient updates { Update policy 𝜋𝜙 by SAC on 𝒟𝑚𝑜𝑑𝑒𝑙: 𝜙←𝜙−𝜆𝜋∇𝜙𝒥𝜙;𝒟𝑚𝑜𝑑𝑒𝑙 } } }
	真实数据采集一部分，用来生成人造数据，然后训练agent
	
##  Future Directions
1. **Environment Model Learning**: Improve accuracy and generalization.
2. **Understanding Bounds**: Tighten theoretical guarantees for policy improvement.
3. **Multi-agent MBRL**: Extend to collaborative or competitive settings.

# 10 Imitation Learning
part of off-line RL.
In the complex env like autonomous driving, robotics, dialog, the reward function is difficult to design. So we need to learn straight from the expert (human driver etc), we will get the optimal strategy. Then try to get the max reward from the policy, so called inverse learning: infer reward function from demonstrations (rollouts) of expert policy.

1. Imitation Learning: 
	1. Given: demonstrations or demonstrator
	2. Goal: train a policy to mimic demonstrations
2. 状态分布一样，policy也一样。
3. 广义上，现在Learning from expert demonstration (LfD), Imitation learning, behavior cloning, inverse RL, apprenticeship learning 都属于imitation learning.
# Terminologies

- $\overset{.}{=}$: equality relationship that is true by definition
- $\approx$: approximately equal
- $\propto$: proportional to
- $Pr\{X = x\}$: probability that a random variable $X$ takes on the value $x$
- $X \sim p$: random variable $X$ selected from distribution $p(x)$
- $E[X]$: expectation of a random variable $X$, i.e.,
  $E[X] \overset{.}{=} \sum_x p(x)x$
- $\arg\max_{a} f(a)$: a value of $a$ at which $f(a)$ takes its maximal value
- $\ln x$: natural logarithm of $x$
- $e^x$: the base of the natural logarithm, $e \approx 2.71828$, carried to power $x$; $e^{\ln x} = x$
- $\mathbb{R}$: set of real numbers
- $f: X \to Y$: function $f$ from elements of set $X$ to elements of set $Y$
- $(a, b]$: the real interval between $a$ and $b$ including $b$ but not including $a$
- $\epsilon$: probability of taking a random action in an $\epsilon$-greedy policy
- $\alpha, \beta$: step-size parameters
- $\gamma$: discount-rate parameter
- $\lambda$: decay-rate parameter for eligibility traces
- $\mathbb{1}_\text{predicate}$:  indicator function. = 1 if the predicate is true, else 0.
### MAB:
- $k$: number of actions (arms)
- $t$: discrete time step or play number
- $q_*(a)$: true value (expected reward) of action $a$
- $Q_t(a)$: estimate at time $t$ of $q_*(a)$
- $N_t(a)$: number of times action $a$ has been selected up to time $t$
- $H_t(a)$: learned preference for selecting action $a$ at time $t$
- $\pi_t(a)$: probability of selecting action $a$ at time $t$
- $\bar{R}_t$: estimate at time $t$ of the expected reward given $\pi_t$
### Temporal Difference Learning

- $\delta_t$: temporal-difference (TD) error at time $t$
- $\delta_t^s, \delta_t^a$: state- and action-specific forms of the TD error
- $n$: in n-step methods, $n$ is the number of steps of bootstrapping
### Eligibility Traces

- $w, w_t$: weight vector in function approximation
- $\mathbf{w}, \mathbf{w}_t$: weight vector notation
- $x(s)$: vector of features visible in state $s$
- $x(s, a)$: vector of features visible in state $s$ taking action $a$
- $\mathbf{x}(s)$, $\mathbf{x}(s, a)$: feature vectors in bold
- $\mathbf{w}^T \mathbf{x}$: inner product of weight vector and feature vector
### Policy Gradient Methods

- $\theta, \theta_t$: parameter vector of target policy
- $\pi(a | s, \theta)$: probability of taking action $a$ in state $s$ given parameter $\theta$
- $\nabla \pi(a | s, \theta)$: gradient of policy function
- $J(\theta)$: performance measure for policy $\pi_\theta$
- $\nabla J(\theta)$: gradient of performance measure
- $b(a|s)$: behavior policy used to select actions while learning about target policy $\pi$
### Importance Sampling

- $\rho_t:h$: importance sampling ratio for time $t$ through time $h$
- $\rho_t$: importance sampling ratio for time $t$ alone, $\rho_t = \rho_{t:t}$
- $r(\pi)$: average reward (reward rate) for policy $\pi$
- $\bar{R}_t$: estimate of $r(\pi)$ at time $t$


# References

[1]. Lecture notes by Dr. Jianxiong Guo.
[2]. CrashCourse. (2019, Oct 12). Reinforcement learning: Crash course AI #9. [Video]. YouTube. https://www.youtube.com/watch?v=nIgIv4IfJ6s.
[3]. Sutton, R.,S. & Barto, A.,G. (2018). Reinforcement learning: An introduction. (2 e.d.)

# Footnote
multi-agent RL is not covered.

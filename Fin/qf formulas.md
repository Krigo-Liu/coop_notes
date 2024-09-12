## 私货，施工中

\text{Excess demand }

$$\Delta{z} = z_\text{+} - z_\text{-}$$


  

\text{Instantaneous return }

\begin{equation} \label{eu_eqn2}

$$r(t)=r(t,\Delta{t})=\frac{p(t)-p(t-\Delta{t})}{p(t-\Delta{t})}$$

\end{equation}

  

\begin{equation} \label{eu_eqn3}

$$r(t)=\frac{\Delta{t}}{\gamma}$$

$$\frac{dr}{dt}=\frac{1}{\gamma}$$

\end{equation}

  

\begin{equation} \label{eu_eqn4}

$$\frac{d(\Delta{z})}{dt}$$

\end{equation}

  

\text{Absorb capacity of the market makers}

\begin{equation} \label{eu_eqn5}

 $$\frac{d(\Delta{z})}{dt}|_\text{MM} \\ = \frac{dz_+}{dt}|_\text{MM} - \frac{dz_-}{dt}|_\text{MM} = -\alpha_+ z_+ +\alpha_-z_-$$

\end{equation}

  

\text{Efficient market maker}

\begin{equation} \label{eu_eqn6}

$$\frac{d(\Delta{z})}{dt}|_\text{MM}= -\alpha_\text{MM}\Delta{z} = \gamma\alpha_\text{MM}r$$

\end{equation}

\text{Speculator}

\begin{equation} \label{eu_eqn7}

$$ \frac{d(\Delta{z})}{dt}|_\text{SP} = -\delta_\text{SP}r$$

\end{equation}

  

\text{Hedger}

\begin{equation} \label{eu_eqn8}

 $$\frac{d(\Delta{z})}{dt}|_\text{HG} = -(\delta_\text{HG} - \nu_\text{HG}r^2)r$$

\end{equation}

  

\text{Investor}

\begin{equation} \label{eu_eqn9}

$$\frac{d(\Delta{z})}{dt}|_\text{IV} = (\delta_\text{IV} - \nu_\text{IV}r^2)r$$

\end{equation}

  

\text{All participants}

\begin{equation} \label{eu_eqn10}

\begin{split}

 $$\frac{d(\Delta{z})}{dt} = \frac{d(\Delta{z})}{dt}|_\text{MM} +\frac{d(\Delta{z})}{dt}|_\text{SP} + \frac{d(\Delta{z})}{dt}|_\text{HG} + \frac{d(\Delta{z})}{dt}|_\text{IV}$$

    $$\\= -\gamma\alpha_\text{MM}r-\delta_\text{SP}r+(\delta_\text{HG} - \nu_\text{HG}r^2)r +(\delta_\text{IV} - \nu_\text{IV}r^2)r

    \\= -\delta{r}+\nu{r^3}$$

\end{split}

\end{equation}

  

\begin{equation} \label{eu_eqn11}

$$\frac{dr}{dt} = \gamma\frac{d\Delta{z}}{dt}= -\gamma\delta{r}+\gamma\nu{r^3}$$

\end{equation}

  

\begin{equation} \label{eu_eqn12}

$$\delta = \gamma\alpha_\text{MM}+\delta_\text{SP}+\delta_\text{HG}-\delta_\text{IV}$$

\end{equation}

  

\begin{equation} \label{eu_eqn13}

$$\nu = \nu_\text{HG} - \nu_\text{IV}$$

\end{equation}

  

\text{Potential energy model}

\begin{equation} \label{eu_eqn14}

\begin{split}

$$V(r)= \int{(-\gamma\eta\delta{r} + \gamma\eta\nu{r^3})dr} \\

= \frac{\gamma\eta\delta}{2}r^3-\frac{\gamma\eta\nu}{4}r^4.$$

\end {split}

\end{equation}

$\eta$ is the market resistance coefficient.

  

\text{Financial particle}

\begin{equation} \label{eu_eqn15}

$$\hat{H}= {\frac{-\hbar}{2m}}{r^2}+ V(r)$$

\end{equation}

  

Schr$\ddot{o}$dinger equation

\begin{equation} \label{eu_eqn16}

\begin{split}

$$[({\frac{-\hbar}{2m}}*{\frac{d^2}{dr^2}}+(\frac{\gamma\eta\delta}{2}r^2 - \frac{\gamma\eta\nu}{4}r^4)]\phi(r) = E\phi(r)$$

\end{split}

\end{equation}

  

\par where E is the eigen-energy of the financial market and $\phi(r)$ is the corresponding eigen-function. Then, perform action space search by solving the QFSE.

  

\par Quantumn anharmonic oscillator

\begin{equation} \label{eu_eqn17}

$$H^m(\lambda)\Psi=-{\frac{d^2\Psi}{dx^2}}+(x^2+\lambda{x^\text{2m}})\Psi=E\Psi$$

\end{equation}

  

Energy term E

\begin{equation} \label{eu_eqn18}

$$(\frac{E(m,n)}{n+1})^\text{(m+1)}-(\frac{E(m,n)}{(n+1)})^\text{(m-1)}=(K_0^\text{m,n})^\text{(m+1)}\lambda$$

\end{equation}

Where $E^(m,n)$ is the n-level energy, $K_0^\text{m,n}$ is a constant.

  

set m=2:

\begin{equation} \label{eu_eqn19}

$$-{\frac{d^2\Psi_r}{dr^2}}+(r^2+\lambda{r^4})\Psi=E\Psi_r$$

\end{equation}

  
  

\begin{equation} \label{eu_eqn20}

$$(\frac{E(n)}{n+1})^3-(\frac{E(n)}{n+1})=(K_0(n)^\text{3+1})^\lambda$$

\end{equation}

  

Since:

\begin{equation} \label{eu_eqn21}

$$K_0(n)=(\frac{1.1924+33.2383n+56.216n^2}{1+43.6196n})^{\frac{1}{3}}$$

\end{equation}

  
  

\begin{equation} \label{eu_eqn22}

$$\lambda=|\frac{r_\text{-1}^2\Psi_\text{-1}- r_\text{+1}^2\Psi_\text{+1}}{r_\text{+1}^4\Psi_\text{+1}-r_\text{-1}^4\Psi_\text{-1}}|$$

\end{equation}

\par Where $\Psi$ is the wave-function indicating the probability distribution of the historical price return, $r_\text{-1}$ and $r_\text{+1}$ are adjacent to the $r_0$, and $r_0$ stands for the return with maximum probability.

  

Use Gerolamo Cardano’s method to solve the depressed cubic equation:

\begin{equation} \label{eu_eqn23}

$$E(n)=\sqrt[3]{-\frac{q}{2} + \sqrt{\frac{q^2}{4}+\frac{p^3}{27}}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\frac{q^2}{4}+\frac{p^3}{27}}}$$

\end{equation}

\par Where $$p= -(2n+1)^2q=\lambda(2n+1)^3[K_0(n)]^3$$
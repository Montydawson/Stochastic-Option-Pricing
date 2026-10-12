# The Heston Model

A fundamental issue with the Black-Scholes model is the assumption of constant volatility, whereas the variation of market-implied volatility across strikes/maturities provides evidence this assumption is inadequate. The Heston model is a popular example of a Stochastic volatility model. <br>
The process is defined as: <br>

$$
\begin{cases}
dS_t = \mu_tS_tdt + \sqrt{\nu_t}S_tdZ^{(1)}_t \\
d\nu_t = \lambda(\bar{\nu} - \nu_t)dt + \eta\sqrt{\nu_t}dZ^{(2)}_t \\
\langle dZ^{(1)}_t, dZ^{(2)}_t \rangle = \rho dt
\end{cases}
$$

with:

$$
\begin{align*}
S_t &:= \text{the stock price at time $t$} \\
\nu_t &:= \text{the variance of said stock price at $t$} \\
\mu_t &:= \text{the instantaneuous drift of the stock's proportional returns} \\
\eta &:= \text{the volatility of the variance process} \\
\bar{\nu} &:= \text{the long-term mean of $\nu$} \\
\lambda &:= \text{the speed of reversion of $\nu_t$ to its long-term mean} \\
\rho &:= \text{the instantaneous correlation between the two Weiner processes $Z^{(1)}_t$ and $Z^{(2)}_t$}
\end{align*}
$$

The Feller Condition: this implies that the variance process is strictly positive if the following condition is satisfied (note in practice this is often not the case):

$$
2\lambda \bar{\nu} > \eta^{2}
$$

### Explanation of parameters and modelling choices:

Under this model the variance process follows a mean-reverting Cox-Ingersoll-Ross (CIR) process, there are currently no closed-form solutions to this however it can be converted into an additive noise SDE via a Lamperti transform. Modelling the volatility as a mean-reverting process is desirable and reflective of the behaviour observed in markets.

## Sketch of Solution Derivation

Under stochastic volatility models, volatility itself is stochastic and so contributes to additional uncertainty. An option is therefore exposed not only to movements in the underlying asset, but also to unexpected changes in its volatility. Mathematically, a 'price of volatility risk' emerges: the compensation associated with exposure to this additional source of risk. Since the volatility risk factor is not traded, this risk cannot be completely hedged using the underlying asset and the risk-free asset. Therefore, the market is incomplete, so the risk-neutral measure is not unique, and the behaviour of volatility is different under different probability measures.<br>

It is essential to consider which probability measure the model is defined under. In Heston's $1993$ paper, the market price of volatility risk is modelled as linear in $\nu$, motivated by the consumption-based model of Breeden $(1979)$ and the general equilibrium model of Cox, Ingersoll, and Ross $(1985)$. This preserves the form of the proposed model when changing from the statistical/real-world measure to the risk-neutral measure. Heston notes that the resulting pricing equations are obtained by arbitrage and do not depend on the other assumptions of these models. <br>

Furthermore, as argued by Gatheral in 'The Volatility Surface: A Practitioner's Guide' $(2006)$, we assume that Heston's model, with parameters fitted to option prices, directly generates the risk-neutral measure. This is appropriate for our purposes because we are concerned only with pricing rather than modelling the statistical behaviour of the underlying asset/volatility risk premium. European option prices are determined by the risk-neutral distribution of future payoffs, rather than by the statistical distribution itself. Hence, if the risk-neutral measure can be recovered from European option prices, there is no need to specify or estimate the statistical measure in order to price the options considered here. We therefore work directly under the risk-neutral measure and make the switch $\mu_t \rightarrow r$. <br>

Derivation: <br>

Let the current value of an option at time $t$ be $V_t = V(S_t, \nu_t, t)$, by Itô's Lemma:

$$
dV_t = \frac{\partial V}{\partial S}dS_t + \frac{\partial V}{\partial \nu} d\nu_t + \frac{\partial V}{\partial t}dt + \frac{1}{2}\frac{\partial^2V}{\partial S^2}(dS_t)^{2} + \frac{1}{2}\frac{\partial^2V}{\partial \nu^2}(d\nu_t)^2 + \frac{\partial^2V}{\partial S\partial \nu}d\nu_t dS_t
$$

Furthermore:

$$
\begin{align*}
(dS_t)^{2} &= \nu_tS_t^{2}dt \\
(d\nu_t)^{2} &= \eta^2\nu_tdt \\
d\nu_t dS_t &= \eta\rho\nu_tS_tdt
\end{align*}
$$

Substituting in we get:

$$
dV_t = \left(\frac{\partial V}{\partial S}rS_t + \frac{\partial V}{\partial \nu}\lambda(\bar{\nu}-\nu_t) + \frac{\partial V}{\partial t}+ \frac{1}{2}\frac{\partial^2V}{\partial S^2}\nu_tS_t^2 + \frac{1}{2}\frac{\partial^2V}{\partial \nu^2}\eta^2\nu_t +\frac{\partial^2V}{\partial S\partial \nu}\eta\rho\nu_tS_t\right)dt + \frac{\partial V}{\partial S}\sqrt{\nu_t}S_tdZ^{(1)}_t + \frac{\partial V}{\partial \nu}\eta\sqrt{\nu_t}dZ^{(2)}_t 
$$

Now considering the discounted asset price $\tilde V_t = e^{-rt}V_t$:

$$
d\tilde V_t = e^{-rt}dV_t - re^{-rt}V_tdt
$$

This is a martingale under the Fundamental Theorem of Asset Pricing, so its drift is $0$ resulting in the following equation:

$$
\frac{\partial V}{\partial S}rS_t + \frac{\partial V}{\partial \nu}\lambda(\bar{\nu}-\nu_t) + \frac{\partial V}{\partial t}+ \frac{1}{2}\frac{\partial^2V}{\partial S^2}\nu_tS_t^2 + \frac{1}{2}\frac{\partial^2V}{\partial \nu^2}\eta^2\nu_t +\frac{\partial^2V}{\partial S\partial \nu}\eta\rho\nu_tS_t -rV_t = 0
$$

Now, following Gatheral, we make the following substitutions: $T$ is the time of expiration, $F$ the time $T$ forward price of the stock, i.e. $F = e^{r(T-t)}S_t$,  $\;x := \ln (\frac{F}{K})$, $\tau = T-t$, and $C$ is the future value of the option at the expiration date: $C = e^{r\tau}V$. The reason for these substitutions are to simplify the above equation, one can think of it as considering the relevant quantities as their future value at expiration date (under risk-free rate). As a result, the substitutions remove the effects of risk-free growth and discounting, taking the $r$ terms out of the equation. The resulting equation is:

$$
-\dfrac{\partial C}{\partial \tau} + \dfrac{1}{2}\nu C_{xx} -\dfrac{1}{2}\nu C_{x} + \dfrac{1}{2}\eta^2 \nu C_{\nu\nu} + \rho\eta\nu C_{x\nu} - \lambda(\nu - \bar{\nu})C_{\nu} = 0
$$

The solution of this equation is shown to have the form:

$$
C(x, \nu, \tau) = K \left(e^{x}P_1(x, \nu, \tau) - P_0(x, \nu, \tau)\right)
$$

where, for $j=0,1$, $P_j(x,\nu,\tau)$ is given by:

$$
P_j(x,\nu,\tau) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \mathop{\mathrm{Re}}\left(\frac{\exp\{C_j(u,\tau)\bar{\nu} + D_j(u,\tau)\nu + iux\}}{iu}\right)du.
$$

Here, $u$ is the Fourier integration variable and $\mathop{\mathrm{Re}}$ denotes the real part. The functions $C_j(u,\tau)$ and $D_j(u,\tau)$ are given by:

$$
C_j(u,\tau) = \lambda\left[r_-^{(j)}\tau - \frac{2}{\eta^2}\ln\left(\frac{1-g_j e^{-d_j\tau}}{1-g_j}\right)\right]
$$

$$
D_j(u,\tau) = r_-^{(j)}\frac{1-e^{-d_j\tau}}{1-g_j e^{-d_j\tau}}
$$

where

$$
d_j = \sqrt{\beta_j^2 - 4\alpha_j\gamma},
$$

$$
r_\pm^{(j)} = \frac{\beta_j \pm d_j}{\eta^2},
$$

and

$$
g_j = \frac{r_-^{(j)}}{r_+^{(j)}}.
$$

The remaining quantities are defined as

$$
\alpha_j = -\frac{u^2}{2} - \frac{iu}{2} + iju,
$$

$$
\beta_j = \lambda - \rho\eta j - \rho\eta iu,
$$

and

$$
\gamma = \frac{\eta^2}{2}.
$$

This integration can be performed using numerical methods. 

## Numerical scheme

Numerical evaluation of the given semi-analytical solution proves complex. In Heston's paper the function $C$ is written as:

$$
C(u, \tau) = \lambda \left(r_{+}\tau - \frac{2}{\eta^2}\ln\left(\dfrac{e^{d\tau} - g}{1 - g}\right) \right)
$$

This is algebraically equivalent to Gatheral's expression. However, when implementing numerical schemes they are not. Taking the principal branch in the above expression results in discontinuity jumps ecah time the imaginary part crosses the negative real axis, causing problems with numerical scheme implementation. Gatheral's expression seemingly removes this problem because it appears the argument never cuts the negative real axis. However, this is yet to be proven and remains a conjecture. To resolve this, we will use an approach given by Kahl and Jäckel $(2005)$.

### Kahl and Jäckel - Not-so-complex logarithms in the Heston Model $(2005)$

Kahl and Jäckel provide a formulation of the Heston pricing equation designed to avoid numerical difficulties associated with the evaluation of the complex logarithm. The call price is given by:

$$
C(S,K,\nu,\tau)=P(\tau)\left[\frac{1}{2}(F-K)+\frac{1}{\pi}\int_0^\infty\left(Ff_1(u)-Kf_2(u)\right)du\right],
$$

where

$$
f_1(u)=\mathop{\mathrm{Re}}\left(\frac{e^{-iu\ln(K)}\phi(u-i)}{iuF}\right),
$$

and

$$
f_2(u)=\mathop{\mathrm{Re}}\left(\frac{e^{-iu\ln(K)}\phi(u)}{iu}\right).
$$

Here,

$$
F=Se^{r\tau},
$$

is the forward price and

$$
P(\tau)=e^{-r\tau}
$$

is the discount factor. The characteristic function is defined as

$$
\phi(u)=\mathbb{E}\left[e^{iu\ln(S_\tau)}\right].
$$

The numerical evaluation of $f_1$ and $f_2$ requires careful treatment of the complex logarithm. Kahl and Jäckel give an explicit procedure for obtaining a continuous logarithm by correcting the argument for discontinuities.

### Evaluation of $f_1$ and $f_2$

Kahl and Jäckel give an explicit procedure for the discontinuity-corrected evaluation of $f_2$, summarised in their Algorithm 1. Using the notation adopted here:

**Algorithm 1: Evaluate $f_2(u)$**

**Require:** $F$, $K$, $\lambda$, $\bar{\nu}$, $\eta$, $\tau>0$, $\nu_0\geq0$ and $\rho\in(-1,1)$.

1. $d:=\sqrt{(\rho\eta ui-\lambda)^2+\eta^2(ui+u^2)}$
2. $c:=\dfrac{\lambda-\rho\eta ui+d}{\lambda-\rho\eta ui-d}$
3. $t_c:=\arg(c)$
4. $G_D:=c-1$
5. $m:=\mathrm{int}\left[\dfrac{t_c+\pi}{2\pi}\right]$
6. $G_N:=ce^{d\tau}-1$
7. $n:=\mathrm{int}\left[\dfrac{t_c+\mathop{\mathrm{{Im}}}(d)\tau+\pi}{2\pi}\right]$
8. $\ln G:=\ln\left(\dfrac{|G_N|}{|G_D|}\right)+i\left(\arg(G_N)-\arg(G_D)+2\pi(n-m)\right)$
9. $D:=\dfrac{\lambda-\rho\eta ui+d}{\eta^2}\left(\dfrac{e^{d\tau}-1}{ce^{d\tau}-1}\right)$
10. $C:=\dfrac{\lambda\bar{\nu}}{\eta^2}\left[(\lambda-\rho\eta ui+d)\tau-2\ln G\right]$
11. $\phi:=\exp(C+D\nu_0+iu\ln(F))$
12. $f_2(u):=\mathop{\mathrm{{Re}}}\left(\dfrac{e^{-iu\ln(K)}\phi}{iu}\right)$

For sufficiently large $\mathop{\mathrm{{Re}}}(d)\tau$, direct evaluation of $G_N$ can cause numerical overflow. Kahl and Jäckel therefore use the condition

$$
\mathop{\mathrm{{Re}}}(d)\tau>-\ln(\mathrm{DBL\_EPSILON}),
$$

under which the subtraction of $1$ in steps 6 and 9 can be neglected and the corresponding logarithmic terms are evaluated directly in logarithmic coordinates.

The evaluation of $f_1(u)$ follows the same procedure, with $u$ replaced by $u-i$ in all steps except the final step, followed by division by $F$ as required by its definition.

### Final Numerical Formulation

The remaining semi-infinite integral can be transformed to a finite interval. Kahl and Jäckel show that, in practice, the calculations above can be combined into a single numerical integration for the undiscounted call price:

$$
\frac{C(S,K,\nu_0,\tau)}{P(\tau)} = \int_0^1y(x)dx,
$$

where

$$
y(x):= \frac{1}{2}(F-K) + \frac{Ff_1(-\frac{\ln(x)}{C_\infty})-Kf_2(-\frac{\ln(x)}{C_\infty})}{x\pi C_\infty},
$$

and

$$
C_\infty = \frac{\sqrt{1-\rho^2}}{\eta}\left(\nu_0+\lambda\bar{\nu}\tau\right)
$$

The endpoint limits required for numerical integration are

$$
\lim_{x\to0}y(x)=\frac{1}{2}(F-K),
$$

and

$$
\lim_{x\to1}y(x) = \frac{1}{2}(F-K) + \frac{F\lim_{u\to0}f_1(u)-K\lim_{u\to0}f_2(u)}{\pi C_\infty}
$$

with

$$
\lim_{u\to0}f_1(u) = \ln \left(\frac{F}{K}\right) + \mathop{\mathrm{Im}}(C'(-i)) + \mathop{\mathrm{Im}}(D'(-i))V_0
$$

where

$$
\mathop{\mathrm{{Im}}}(C'(-i))=\frac{e^{(\rho\eta-\lambda)\tau}\lambda\bar{\nu}+\lambda\bar{\nu}\left((\lambda-\rho\eta)\tau-1\right)}{2(\lambda-\rho\eta)^2}
$$

and

$$
\mathop{\mathrm{{Im}}}(D'(-i))=\frac{1-e^{-(\lambda-\rho\eta)\tau}}{2(\lambda-\rho\eta)}
$$

provided that $\lambda-\rho\eta\neq0$. When $\lambda-\rho\eta=0$, these become

$$
\mathop{\mathrm{{Im}}}(C'(-i))=\frac{\lambda\bar{\nu}\tau^2}{4}
$$

and

$$
\mathop{\mathrm{{Im}}}(D'(-i))=\frac{\tau}{2}.
$$

Similarly,

$$
\lim_{u\to0}f_2(u)=\ln\left(\frac{F}{K}\right)+\mathop{\mathrm{{Im}}}(C'(0))+\mathop{\mathrm{{Im}}}(D'(0))\nu_0
$$

where

$$
\mathop{\mathrm{{Im}}}(C'(0))=-\frac{e^{-\lambda\tau}\lambda\bar{\nu}+\lambda\bar{\nu}(\lambda\tau-1)}{2\lambda^2}
$$

and

$$
\mathop{\mathrm{{Im}}}(D'(0))=-\frac{1-e^{-\lambda\tau}}{2\lambda}.
$$

This converts the original semi-infinite integration problem into the evaluation of a single integral over the finite interval $[0,1]$. Gauss-Lobatto quadrature can then be used to numerically evaluate this integral.
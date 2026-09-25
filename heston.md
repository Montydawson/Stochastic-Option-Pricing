# The Heston Model

A fundamental issue with the Black-Scholes model is the assumption of constant volatility, whereas the variation of market-implied volatility across strikes/maturities provides evidence this assumption is inadequate. The Heston model is a popular example of a Stochastic volatility model. <br>
The process is defined as: <br>

$$
\begin{cases}
dS_t = \mu_tS_tdt + \sqrt{\nu_t}S_tdZ^{(1)}_t \\
d\nu_t = \lambda(\bar{\nu} - \nu_t)dt + \eta\sqrt{\nu_t}dZ^{(2)}_t \\
\langle Z^{(1)}_t, Z^{(2)}_t \rangle = \rho dt
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

The Feller Condition: this implies that the variance process is strictly positive if the following condition is satisfied:

$$
2\lambda \bar{\nu} > \eta^{2}
$$


### Explanation of parameters and modelling choices:
Under this model the variance process follows a mean-reverting Cox-Ingersoll-Ross (CIR) process, there are currently no closed-form solutions to this however it can be converted into an additive noise SDE via a Lamperti transform. Modelling the volatility as a mean-reverting process is desirable and reflective of the behaviour observed in markets. 

## Sketch of Solution Derivation
Under stochastic volatility models, volatility itself is stochastic and so contributes to additional uncertainty. An option is therefore exposed not only to movements in the underlying asset, but also to unexpected changes in its volatility. Mathematically, a 'price of volatility risk' emerges: the compensation associated with exposure to this additional source of risk. Since the volatility risk factor is not traded, this risk cannot be completely hedged using the underlying asset and the risk-free asset. Therefore, the market is incomplete, so the risk-neutral measure is not unique, and the behaviour of volatility is different under different probability measures.<br> 

It is essential to consider which probability measure the model is defined under. In Heston's $1993$ paper, the market price of volatility risk is modelled as linear in $\nu$, motivated by the consumption-based model of Breeden $(1979)$ and the general equilibrium model of Cox, Ingersoll, and Ross $(1985)$. This preserves the form of the proposed model when changing from the statistical/real-world measure to the risk-neutral measure. Heston notes that the resulting pricing equations are obtained by arbitrage and do not depend on the other assumptions of these models. <br>

Furthermore, as argued by Gatheral in 'The Volatility Surface: A Practitioner's Guide', we assume that Heston's model, with parameters fitted to option prices, directly generates the risk-neutral measure. This is appropriate for our purposes because we are concerned only with pricing rather than modelling the statistical behaviour of the underlying asset/volatility risk premium. European option prices are determined by the risk-neutral distribution of future payoffs, rather than by the statistical distribution itself. Hence, if the risk-neutral measure can be recovered from European option prices, there is no need to specify or estimate the statistical measure in order to price the options considered here. We therefore work directly under the risk-neutral measure and make the switch $\mu_t \rightarrow r$. <br>

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




















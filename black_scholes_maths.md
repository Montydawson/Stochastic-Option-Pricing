# European Call Pricing Derivation 
### Stock Price 

To start we let Stock Price $S_t$ at time $t$ evolve according to the following SDE (Samuelson):

$$
dS_t = \mu S_t dt + \sigma S_t dB_t, \quad S_0 = s_0
$$

with $\mu$ as the drift, $\sigma \geq 0$ the volatility, and $B_t$ the Brownian increment. This a GBM SDE so use the substitution $X_t = f(S_t) = ln(S_t)$, and applying Itô's Lemma:

$$
dX_t = (\mu - \frac{1}{2}\sigma^2)dt + \sigma dB_t \\
X_t - X_0 = (\mu - \frac{1}{2}\sigma^{2})t + \sigma B_t
$$

hence

$$
S_t = S_0 \exp((\mu - \frac{1}{2}\sigma^2)t + \sigma B_t)
$$

## Option Pricing
 - **FTAP: The market is arbitrage free iff there exists a risk-neutral probability measure $\tilde{\mathbb{P}}$ under which discounted stock/asset prices are martingales.** <br>

Following this one can conclude:

$$
V_0 = e^{-rT}\mathbb{E}^{\tilde{\mathbb{P}}}\left[h(S_T)\right]
$$

where $h(S_T)$ is the payoff function of the option at maturity $T$, i.e $h(S_T) = V_T$, and $r$ is the risk-free rate. It is important to note that under a different probability measure the drift of the SDE changes. Via Girsanov's Theorem (https://en.wikipedia.org/wiki/Girsanov_theorem): <br>

$$
dS_t = rS_tdt + \sigma S_t dW_t \\
S_t = S_0 \exp((r - \frac{1}{2}\sigma^2)t + \sigma W_t)
$$

With $ W_t$ Brownian motion under the risk-neutral proabability measure. So continuing to find $V_0$, using European call as an example with strike price $K$: <br>

$$
V_0 = e^{-rT}\mathbb{E}^{\tilde{\mathbb{P}}}\left[(S_T - K)^{+}\right] \\ 
$$

Noting that $S_T$ is lognormally distributed we take:

$$
\mu := \ln(S_0) + (r-\frac{1}{2}\sigma^{2})T \\
$$

$$
Z(T) := \dfrac{\ln(S_T) - \mu}{\sigma \sqrt{T}} \sim \mathcal{N}(0,1) \quad \text{under} \quad \tilde{\mathbb{P}}
$$

such that

$$
S_T = \exp(\mu + \sigma \sqrt{T} Z)
$$

and for limits:

$$
S_T > K \quad \iff \quad Z(T) > \dfrac{\ln(K) - \mu}{\sigma \sqrt{T}} =: w
$$

Thus,

$$
V_0 = e^{-rT}\int_{w}^{\infty} \left(\exp(\mu + \sigma \sqrt{T} z) - K\right) \phi(z) dz \\
$$

$$
V_0 = e^{-rT}\left(\int_{w}^{\infty}\dfrac{\exp(\mu + \sigma \sqrt{T}z -\frac{z^{2}}{2})}{\sqrt{2\pi}} - K\phi(z)dz\right) 
$$

And completing the square for the first integral:

$$
V_0 = e^{-rT + \mu + \frac{\sigma^{2}T}{2}}\int_{w}^{\infty}\phi(z-\sigma \sqrt{T})dz - e^{-rT}\int_{w}^{\infty}K\phi(z)dz
$$

$$
V_0 = e^{-rT + \mu + \frac{\sigma^{2}T}{2}}\int_{w-\sigma\sqrt{T}}^{\infty}\phi(x)dx - e^{-rT}\int_{w}^{\infty}K\phi(z)dz
$$

$$
V_0 = S_0 \Phi(\sigma \sqrt{T} - w) - e^{-rT}K\Phi(-w)
$$

taking:

$$
d_1 := \dfrac{\ln(\frac{S_0}{K}) + (r+\frac{1}{2}\sigma^{2})T}{\sigma\sqrt{T}}
$$

$$
d_2 := \dfrac{\ln(\frac{S_0}{K}) + (r-\frac{1}{2}\sigma^{2})T}{\sigma\sqrt{T}}
$$

We finally obtain the Black-Scholes Merton formula:

$$
V_0 = S_0\Phi(d_1) - e^{-rT}K\Phi(d_2)
$$

Note this is for a non-dividend-paying stock.


### Extending to dividend paying stock

Suppose the stock pays a continuous dividend yield $q$, such that the dividend payment over the time period $[t,t+dt]$ is modelled as $qS_tdt$, where $q$ is a constant dividend yield. Also define the time remaining until maturity as:

$$
\tau:=T-t
$$

Where $\tau$ represents the fraction of a year remaining until maturity, so that is consistent with the other annualised parameters. Under the risk-neutral probability measure, the SDE must account for dividend payments such that:

$$
dS_t=(r-q)S_tdt+\sigma S_tdW_t
$$

where $W_t$ is Brownian motion under the risk-neutral probability measure. The solution between time $t$ and maturity $T$ is therefore:

$$
S_T=S_t\exp((r-q-\frac{1}{2}\sigma^2)\tau+\sigma(W_T-W_t))
$$

So the risk-neutral pricing equation for a European call becomes:

$$
V_t=e^{-r\tau}\mathbb{E}^{\tilde{\mathbb{P}}}\left[(S_T-K)^+\mid\mathcal{F}_t\right]
$$

similar to before. Also similarly we take

$$
\mu:=\ln(S_t)+(r-q-\frac{1}{2}\sigma^2)\tau
$$

$$
Z(T):=\dfrac{\ln(S_T)-\mu}{\sigma\sqrt{\tau}}\sim\mathcal{N}(0,1)\quad \text{under} \; \tilde{\mathbb{P}}
$$

and hence:

$$
S_T=\exp(\mu+\sigma\sqrt{\tau}Z)
$$

Following the same steps as above, we obtain:

$$
\boxed{V_t=S_te^{-q\tau}\Phi(d_1)-Ke^{-r\tau}\Phi(d_2)}
$$

where:

$$
d_1:=\dfrac{\ln(\frac{S_t}{K})+(r-q+\frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}
$$

$$
d_2:=\dfrac{\ln(\frac{S_t}{K})+(r-q-\frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}
$$

with:

$$
d_2=d_1-\sigma\sqrt{\tau}
$$

This is the Black-Scholes-Merton formula for a European call on a stock paying a continuous dividend yield $q$. Setting $q=0$ and $t=0$ gives the standard Black-Scholes-Merton formula above.

# Limitations of Black-Scholes Model

 - It assumes the terminal price of the underlying follows a log-normal distribution, and thus is always positive. Equivalently, log returns are normally distributed, giving the model thin tails compared with many empirical return distributions. In practice, these returns are often leptokurtic (sharper peak and fatter tails than normal distribution). As a result Black-Scholes can underestimate the probability of extreme price movements. A small error in estimating the probability of extreme price movements can have a disproportionate impact on the estimated risk of an option.

 - Assumes constant volatility thus not explaining the 'volatility smile/skew'.

 - Implied volatility is obtained by calibrating the Black–Scholes model to observed option prices. This is not an independent measure of volatility or evidence that the model is accurate, since the volatility is chosen to reproduce the observed price.

 - Assumes idealised frictionless market: no transaction costs/fees and continuous trading and borrowing/lending.

 - Assumes constant risk free rate.

 - Limited to pricing European options.
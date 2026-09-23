## Option Pricing Example including derivation of Stock price 
#### Derivation of Stock Price 

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

### Option Pricing
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

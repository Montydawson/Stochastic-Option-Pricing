# Greeks for European Call

The greeks represent the sensitivity of the pricing of a derivative to the parameters used in said pricing. In the following we will use the Black-Scholes formula previously derived, for a European Call on a stock paying a continuous dividend yield $q$. We have from before:

$$
V_t = S_te^{-q\tau}\Phi(d_1) - Ke^{-r\tau}\Phi(d_2)
$$

where $S_t$ is the stock price at time $t$, $K$ is strike price and maturity is at time $T$, with $\tau=T-t$, and

$$
d_1 := \dfrac{\ln(\frac{S_t}{K}) + (r-q+\frac{1}{2}\sigma^{2})\tau}{\sigma\sqrt{\tau}}
$$

$$
d_2 := \dfrac{\ln(\frac{S_t}{K}) + (r-q-\frac{1}{2}\sigma^{2})\tau}{\sigma\sqrt{\tau}}
$$

## Delta

$$
\Delta := \dfrac{\partial V_t}{\partial S_t}
$$

$$
\Delta = e^{-q\tau}\Phi(d_1) + S_te^{-q\tau}\frac{\partial d_1}{\partial S_t}\phi(d_1) - Ke^{-r\tau}\frac{\partial d_2}{\partial S_t}\phi(d_2)
$$

noticing $d_2 = d_1 - \sigma \sqrt{\tau}$:

$$
\frac{\partial d_1}{\partial S_t} = \frac{1}{S_t \sigma \sqrt{\tau}} = \frac{\partial d_2}{\partial S_t}
$$

thus

$$
\Delta = e^{-q\tau}\Phi(d_1) + \frac{1}{\sigma \sqrt{\tau}}\left(e^{-q\tau}\phi(d_1) - e^{-r\tau}\frac{K}{S_t}\phi(d_2)\right)
$$

using the identity $(1)$:

$$
S_te^{-q\tau}\phi(d_1) = Ke^{-r\tau}\phi(d_2) 
$$

this simplifies nicely to:

$$
\boxed{\Delta = e^{-q\tau}\Phi(d_1)}
$$

Delta represents the sensitivity of the option (call in this case) value to its underlying asset price. Due to the CDF and finiteness: $0 < \Delta < e^{-q\tau}$

**Put-Call Parity:**

Using the Put-Call Parity formula:

$$
C_t-P_t=S_te^{-q\tau}-Ke^{-r\tau}
$$

where $C_t$ and $P_t$ are the time-$t$ prices of European Call and Put options respectively, and $\tau=T-t$. One can show simply that:

$$
\Delta_C-\Delta_P=e^{-q\tau}
$$

This makes intuitive sense if one considers being long a call and short a put, this position is equivalent to being long the underlying asset while accounting for the present value of its dividends and borrowing the present value of the strike price. The resulting position has Delta $=e^{-q\tau}$.

Furthermore, for a portfolio $\Delta$ is clearly additive which gives the basis of Delta hedging: By taking a position in the underlying asset such that the overall portfolio has $\Delta=0$, the portfolio becomes locally insensitive to small movements in the underlying price. This approximation holds over a short time period and does not account for changes in volatility, interest rates, or other market conditions.




## Gamma

$$
\Gamma := \frac{\partial^{2} V_t}{\partial S_t^{2}} = \frac{\partial \Delta}{\partial S_t}
$$

$$
\Gamma = e^{-q\tau}\frac{\partial d_1}{\partial S_t}\phi(d_1)
$$

$$
\boxed{\Gamma = \dfrac{e^{-q\tau}}{S_t\sigma\sqrt{\tau}}\phi(d_1)}
$$

$\Gamma$ is positive for standard vanilla options under Black-Scholes. This makes sense because for calls: as $S_t$ increases so does $\Delta$ (from $0$ to $e^{-q\tau}$), and for puts: as $S_t$ increases so does $\Delta$ (from $-e^{-q\tau}$ to $0$). $\Gamma$ can be used in conjunction with $\Delta$ in Delta hedging as one may want to minimise $\Gamma$ such that the portfolio value is less sensitive to larger swings in the underlying asset price.

## Vega

$$
\nu := \dfrac{\partial V_t}{\partial \sigma}
$$

$$
\nu = S_te^{-q\tau}\frac{\partial d_1}{\partial \sigma}\phi(d_1) - Ke^{-r\tau}\frac{\partial d_2}{\partial \sigma}\phi(d_2)
$$

and once again using identity $(1)$ from above

$$
\nu = S_te^{-q\tau}\phi(d_1)\left(\frac{\partial d_1}{\partial \sigma} - \frac{\partial d_2}{\partial \sigma}\right)
$$

$$
\boxed{\nu = S_te^{-q\tau}\phi(d_1)\sqrt{\tau}}
$$

$\nu$ measures the option value's sensitivity to volatility. Clearly $\nu>0$, so option values increase with volatility. Often part of a strategy is to obtain 'vega neutral' positions such that the portfolio's value is less sensitive to changes in volatility.

## Theta

$$
\Theta := - \dfrac{\partial V}{\partial \tau}
$$

$$
\Theta = -\left(-qS_te^{-q\tau}\Phi(d_1) + S_te^{-q\tau}\frac{\partial d_1}{\partial \tau}\phi(d_1) +rKe^{-r\tau}\Phi(d_2) - Ke^{-r\tau}\frac{\partial d_2}{\partial \tau}\phi(d_2)\right)
$$

$$
\Theta = qS_te^{-q\tau}\Phi(d_1) - rKe^{-r\tau}\Phi(d_2) + S_te^{-q\tau}\phi(d_1)(\frac{\partial d_2}{\partial \tau} - \frac{\partial d_1}{\partial \tau})
$$

$$
\boxed{\Theta = -e^{-q\tau}\dfrac{S_t\phi(d_1)\sigma}{2\sqrt{\tau}} + qS_te^{-q\tau}\Phi(d_1) - rKe^{-r\tau}\Phi(d_2)}
$$

By convention $\Theta$ is presented as the negative of the rate of change of the value with respect to the remaining time until expiry. This is because as time goes on $\tau$ decreases and the option typicaly loses value, so it is from the perspective of current time 'passed' increasing so as to convey the idea of value loss as time progresses. This is even clearer when using the chain rule and $\dot{\tau} = -1$. Importantly, option value does not always decrease as one gets closer to the expiry date. Although the loss of extrinsic (or time) value typically causes the option's value to decrease, this can be offset by other effects, such as the reduced impact of discounting as maturity approaches. For sufficiently deep in-the-money options, this effect can dominate, resulting in a positive theta.

## Rho

$$
\rho := \dfrac{\partial V}{\partial r}
$$

$$
\rho = S_te^{-q\tau}\frac{\partial d_1}{\partial r}\phi(d_1) + K\tau e^{-r\tau}\Phi(d_2) - Ke^{-r\tau}\phi(d_2)\frac{\partial d_2}{\partial r}
$$

and using identity $(1)$:

$$
\boxed{\rho = K\tau e^{-r\tau}\Phi(d_2)}
$$

Rho is typically expressed as the amount of money, per share of the underlying, that the value of the option will gain or lose as the risk-free interest rate rises or falls $1.0\%$ per annum
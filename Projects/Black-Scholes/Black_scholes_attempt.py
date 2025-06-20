import blackscholes as bs
from jax.experimental.pallas.ops.tpu.splash_attention.splash_attention_mask_info import process_mask
from jax.scipy.stats import norm as jnorm
import yfinance as yf
import jax.numpy as jnp
import jax as grad

def black_scholes(S,K,T,r,sigma,q=0,otype="call"):
    d1= (jnp.log(S/K)+(r+(sigma**2)/2)*T)/(sigma*jnp.sqrt(T))
    d2= d1 - sigma*jnp.sqrt(T)
    if otype == "call":
        call = jnorm.cdf(d1)*S - jnorm.cdf(d2)*K*jnp.exp(-r*T)
        return call
    elif otype == "put":
        put = K*jnp.exp(-r*T)*jnorm.cdf(-d2)-S*jnorm.cdf(-d1)
        return put
    else:
        raise ValueError("otype must be 'call' or 'put'")

def stock_data(stock):
    stock_data = yf.Ticker(stock).history(period="max")
    S=stock_data["Close"].iloc[-1]
    return S

def get_riskfree_rate():
    r_data = yf.Ticker("^IRX")
    r_df = r_data.history(period="5d")
    if r_df.empty:
        raise ValueError("No data returned for ^IRX. Check internet connection or ticker.")
    else:
        r = r_df['Close'].iloc[-1] / 100
        return r


def diff_function(S,K,T,r,sigma_est,price,q=0,otype="call"):
    theoretical = black_scholes(S,K,T,r,sigma_est,q)
    market_value = price
    return theoretical - market_value

loss_grad = grad.grad(diff_function,argnums=4)

def implied_volatility(stock,K,sigma_est,price,T=1,q=0,otype="call",E=0.01,iter=40):
    S=stock_data(stock)
    r=get_riskfree_rate()
    Error = 1
    diff = diff_function(S, K, T, r, sigma_est, price, q, otype)
    iterations=0
    while abs(diff) > E and iterations < iter:
        if diff<E:
            break
    else:
        iterations += 1
        diff = diff_function(S, K, T, r, sigma_est, price, q, otype)
        diff_grad = loss_grad(S,K,T,r,sigma_est,price,q,otype)
        sigma_est = sigma_est + diff/diff_grad
    return sigma_est





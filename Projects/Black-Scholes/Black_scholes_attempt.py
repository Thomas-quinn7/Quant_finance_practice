import blackscholes as bs
from jax.experimental.pallas.ops.tpu.splash_attention.splash_attention_mask_info import process_mask
from jax.scipy.stats import norm as jnorm
import yfinance as yf
import jax.numpy as jnp
from jax import grad

def black_scholes(S,K,T,r,sigma,q=0,otype="call"):
    d1= (jnp.log(S/K)+(r-q+(sigma**2)/2)*T)/(sigma*jnp.sqrt(T))
    d2= d1 - sigma*jnp.sqrt(T)
    if otype == "call":
        call = jnorm.cdf(d1)*S*jnp.exp(-q*T) - jnorm.cdf(d2)*K*jnp.exp(-r*T)
        return call
    elif otype == "put":
        put = K*jnp.exp(-r*T)*jnorm.cdf(-d2)-S*jnorm.cdf(-d1)*jnp.exp(-q*T)
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
    return theoretical - price

def implied_volatility(stock,K,sigma_est,price,T=1,q=0,otype="call",E=0.01,iter=40):
    S=stock_data(stock)
    r=get_riskfree_rate()
    iterations=0
    diff = diff_function(S, K, T, r, sigma_est, price, q, otype)
    loss_grad = grad(diff_function,argnums=4)
    while abs(diff) > E and iterations < iter:
        diff = diff_function(S,K,T,r,sigma_est,price,q,otype)
        diff_grad = loss_grad(S,K,T,r,sigma_est,price,q,otype)
        if diff_grad == 0:
            print("Gradient is zero or invalid; stopping.")
            break

        iterations += 1
        if abs(diff) < E:
            break
        sigma_est = sigma_est - diff / diff_grad
    return sigma_est

def greeks(S,K,T,r,sigma,q=0,otype="call"):
    S = float(S)
    K = float(K)
    T = float(T)
    r = float(r)
    sigma = float(sigma)
    q = float(q)
    Delta_func = grad(black_scholes,argnums=0)
    Gamma_func = grad(Delta_func,argnums=0)
    Theta_func = grad(black_scholes,argnums=2)
    Vega_func = grad(black_scholes,argnums=4)
    Rho_func = grad(black_scholes,argnums=3)
    Delta = Delta_func(S,K,T,r,sigma,q,otype)
    Gamma = Gamma_func(S,K,T,r,sigma,q,otype)
    Theta = Theta_func(S,K,T,r,sigma,q,otype)
    Vega = Vega_func(S,K,T,r,sigma,q,otype)
    Rho = Rho_func(S,K,T,r,sigma,q,otype)
    return Delta, Gamma, Theta, Vega, Rho


import blackscholes as bs
import jax.numpy as jnp
from jax.experimental.pallas.ops.tpu.splash_attention.splash_attention_mask_info import process_mask
from jax.scipy.stats import norm as jnorm
import yfinance as yf
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

loss_grad = jnp.grad(diff_function,argnums=4)

def implied_volatility(stock,K,T=1,sigma_est,price,q=0,otype="call",E=0.01,iter=40):
    S=stock_data(stock)
    r=get_riskfree_rate()
    diff = diff_function(S,K,T,r,sigma_est,price,q,otype)
    Error = 1
    iterations=0
    while E<Error and iterations<iter:
        diff = diff_function(S,K,T,r,sigma_est,price,q,otype)
        Error=abs(diff)
        iterations+=1
        if iterations=iter:
            break
        else:
            sigma_est = sigma_est - diff/loss_grad(S,K,T,r,sigma_est,price,q,otype)
            continue
    return sigma_est
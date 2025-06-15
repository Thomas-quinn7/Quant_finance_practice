import blackscholes as bs
import jax.numpy as jnp
from jax.scipy.stats import norm as jnorm
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


import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from pandas.core.groupby.base import plotting_methods

MSFT = yf.Ticker('MSFT')
hist_mist = MSFT.history(period='max')
print(hist_mist)
print(MSFT.actions)


tickers = ['^GSPC', '^DJI', '^IXIC', '^FTSE', '^GDAXI', '^FCHI', '^N225', '^HSI']
data = yf.download(tickers, period="5y")
closing_prices = data['Close']
closing_prices=closing_prices.iloc[0]
closing_prices.plot(kind='bar', title='Closing Prices for Major Indices (1d)')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

closing_prices = data['Close']

# Plot
closing_prices.plot(figsize=(12, 6), title='Closing Prices Over Time')
plt.ylabel('Price')
plt.xlabel('Date')
plt.grid(True)
plt.tight_layout()
plt.legend(title="Index")
plt.show()


print(closing_prices["^DJI"].iloc[0])
five_diff = closing_prices.iloc[-1]/closing_prices.iloc[0]
print(five_diff)

five_diff.plot(kind='bar',figsize=(12, 6))#
plt.ylabel('5 Year Growth')
plt.xlabel('Date')
plt.show()
one_yr_diff = (five_diff)**(1/5)-1

one_yr_diff.plot(kind='bar',figsize=(10, 5))
plt.ylabel('5 Year Growth')
plt.xlabel('Date')
plt.show()
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
plt.plot(hist_mist)
plt.show()

major_indices = pd.read_html("https://finance.yahoo.com/markets/world-indices")[0]
MI=yf.Search("indices")

# make function to collect options data
import yfinance as yf
import pandas as pd
from datetime import datetime


def options_data(start, end, min_maturity, max_maturity, min_money, max_money, strikes, ticker = '^SPX'):
    spx = yf.Ticker(ticker)
    observation_date = datetime.strptime(start, '%Y-%m-%d')

    for expiry in spx.options:
        # find tau
        expiry_date = datetime.strptime(expiry, '%Y-%m-%d')
        tau = (expiry_date - observation_date).days / 365

    


spx = yf.Ticker('^SPX')
#print(spx.option_chain(spx.options[0]).calls)
print(spx.options)
spx.head()

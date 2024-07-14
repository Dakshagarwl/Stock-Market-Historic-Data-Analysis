import yfinance as yf
import pandas as pd


equity_details= pd.read_csv('ind_nifty50list.csv')

for name in equity_details.Symbol:
    data=yf.download(f'{name}.NS')
    data.to_csv(f'./Datacollection/{name}.csv')
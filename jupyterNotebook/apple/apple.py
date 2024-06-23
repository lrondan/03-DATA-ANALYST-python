import yfinance as yf
import pandas as pd
import json

apple = yf.Ticker('AAPL')

with open('apple/apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    print("Type:", type(apple_info))
apple_info['country'] #key donde se busca info

apple_share_price_data = apple.history(period='max')
print(apple_share_price_data.head())
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.plot(x='Date', y='Open'))
apple.dividends
print(apple.dividends.plot())



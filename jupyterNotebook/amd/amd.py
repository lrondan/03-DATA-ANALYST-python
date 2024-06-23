import json
import pandas as pd
import yfinance as yf

amd = yf.Ticker('AMD')

with open('amd/amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    print("Type:", type(amd_info))
amd_info['country', 'sector']

amd_share_price_data = amd.history(period='max') #se convierte en un data frame
print(amd_share_price_data.head(1)) #vizualiza la primera fila del Df
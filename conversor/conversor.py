import pandas as pd
import json


with open('./apple.json', 'r') as json_file:
    apple_info = json.load(json_file)

state = apple_info['state']
city = apple_info['city']
phone = apple_info['phone']
country = apple_info['country']

d = {'state':[state], 'city':[city], 'phone':[phone], 'contry':[country]}

df = pd.DataFrame(data=d)

df.to_csv('./results.csv', sep=',')
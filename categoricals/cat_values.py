import pandas as pd

datas = {'carros':['A','B','C','D'], 'Fuel':['gas', 'diesel','gas','gas']}

df = pd.DataFrame(data=datas)
df1 = pd.get_dummies(df['Fuel'])

print(df1)
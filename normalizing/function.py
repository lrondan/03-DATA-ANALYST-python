import pandas as pd
import csv

path = 'normalizing/example1.csv'

df = pd.read_csv(path)


#identificar el tipo de dato y convertirlo en entero
df['column2'] = df['column2'].astype('int')

#normalizacion Simple-Feature-Scaling
df1 = df['column2']/df['column2'].max()

#normalizacion Min-Max
df2 = (df['column2'] - df['column2'].min()) / (df['column2'].max() - df['column2'].min())

#normalizacion Z-score
df3 = df['column2'] - df['column2'].mean()/ df['column2'].std()
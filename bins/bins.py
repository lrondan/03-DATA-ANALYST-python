import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
precio = {'precio':[5000,10000,12000,12000,30000,31000,39000,44000,45000]}

df = pd.DataFrame(data=precio)

bins = np.linspace(min(df['precio']), max(df['precio']), 4)
grupo = ['low','med','high']

df['precio_binned'] = pd.cut(df['precio'], bins, labels= grupo, include_lowest=True)

mpl.hist(df['precio_binned'])
mpl.show()
print(df)
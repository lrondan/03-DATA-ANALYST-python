import pandas as pd

d = {'drive':['toyota','MW', 'lambo'], 'drive_weels':[45, 665,54]}
df = pd.DataFrame(data=d)

drive_counts = df['drive'].value_counts()

drive_counts.renamecolumns= {'drive': 'valve_counts'}
drive_counts.index.name='drive weels'

print(drive_counts)

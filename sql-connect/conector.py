import pandas as pd
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost', user='root', password='Luis*001126', database='data_schema1'
)

cursor = conexion.cursor()
cursor.execute('select `Month-Year of Purchase`,`Units Sold` from data_schema1.data')
for row in cursor:
    for i in row:
        columna = i
        print(columna)
print('_______________________________________________________________')
cursor.execute('select `Units Sold` from data_schema1.data')
for suma in cursor:
    for j in suma:
        j:int = j.sum()
        print(j)
    

conexion.close()
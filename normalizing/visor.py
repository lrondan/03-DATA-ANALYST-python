import function as function

print('Para ver los siguientes metodos de normalizacion')
print('pulse unos de los siguientes numeros')
print('1. Normalizacion Simple-Feature-Scaling')
print('2. Normalizacion Min-Max')
print('3. Normalizacion Z-score')
print('4. Ver el dataframe')
print('5. Salir')

valor = int(input('Seleccione: '))

if valor > 5 or valor < 1:
    print('ERROR')
else:
    if valor ==1:
        print('normalizacion Simple-Feature-Scaling\n',function.df1)
    elif valor ==2:
        print('normalizacion Min-Max\n',function.df2)
    elif valor==3:
        print('normalizacion Z-scored\n',function.df3)
    elif valor==4:
        print(function.df)
    else:
        exit()
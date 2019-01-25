
# Receta 5-2: Crear un DataFrame.

import pandas as pd

diccionario = {'col1': [1, 2, 3, 4, 5], 'col2': [2, 3, 5, 7, 11]}

df = pd.DataFrame(data=diccionario)

# print(df.head())
print(df.tail(2))

print(df.columns)

print(df.describe())

print(type(df['col2']))

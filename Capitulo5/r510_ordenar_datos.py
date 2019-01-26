
# Receta 5-10: Ordenar datos en un DataFrame.

import pandas as pd

datos = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

df = pd.DataFrame(data=datos, index=['b', 'c', 'a'])

print(df.head())

print(df.sort_index())

print(df.sort_values(by='col2', ascending=False))

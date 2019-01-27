
# Receta 5-13: Iterar un DataFrame.

import pandas as pd

datos = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

df = pd.DataFrame(data=datos)

# Iteración por columnas:
for columna in df:
    print(df[columna])

# Iterar índice, fila:
for indice, fila in df.iterrows():
    print('Índice: {}'.format(indice))
    print(fila)

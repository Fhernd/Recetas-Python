
# Receta 5-4: Importar archivo CSV

import pandas as pd

paises = pd.read_csv('paises.csv')

print(paises.columns)

print(paises.shape)

print(len(paises))

print(paises['pais'])

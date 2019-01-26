
# Receta 5-6: Importar archivo de Excel.

import pandas as pd

df = pd.read_excel('paises.xlsx', sheet_name='suramerica')

print(df.head())

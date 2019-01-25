
# Receta 5-1: Crear un objeto Series.

# pip install pandas

import pandas as pd

datos = [1, 2, 3, 4, 5]

serie = pd.Series(datos)

print(serie + 7)

print(serie.dtype)

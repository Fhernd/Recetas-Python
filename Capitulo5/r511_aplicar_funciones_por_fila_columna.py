
# Receta 5-11: Aplicar una función sobre una fila o columna

import pandas as pd
import numpy as np

datos = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

df = pd.DataFrame(data=datos, index=['b', 'c', 'a'])

print(df.apply(np.mean))

print(df.apply(np.mean, axis=1))

print(df.apply(lambda x: 2 * x, axis=0))

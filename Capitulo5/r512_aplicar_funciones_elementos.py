
# Receta 5-12: Aplicar una función a cada elemento de un DataFrame o Series.

import pandas as pd

datos = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

# 1. applymap: se usa sobre un DataFrame
# 2. map: se usa sobre un Series

df = pd.DataFrame(data=datos)

print(df.applymap(lambda x: x ** 3))

print(df.col2.map(lambda x: x ** 2))

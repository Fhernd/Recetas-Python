
# Receta 5-3: Crear un objeto Panel

import pandas as pd

dict1 = {'col1': list(range(0, 5)), 'col2': list(range(5, 10))}
dict2 = {'colA': list(range(10, 15)), 'colB': list(range(15, 20))}

df1 = pd.DataFrame(data=dict1)
df2 = pd.DataFrame(data=dict2)

panel = pd.Panel({'dict1': df1, 'dict2': df2})

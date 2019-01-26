
# Receta 5-7: Guardar contenido DataFrame en un archivo de Excel.

import pandas as pd

ids = [1, 2, 3, 4, 5]
paises_europeos = ['Albania', 'Bélgica', 'Chipre', 'Eslovenia', 'Dinamarca']

df = pd.DataFrame(data={'id': ids, 'pais': paises_europeos})

print(df.head())

df.to_excel('paises_europeos.xlsx', sheet_name='europa', index=False)


# Receta 5-5: Guardar contenido DataFrame en archivo CSV.

import pandas as pd

paises = ['Albania', 'Bélgica', 'Chipre', 'Eslovenia', 'Dinamarca', 'España']

paises_df = pd.DataFrame(data={'pais': paises})

# print(paises_df)

paises_df.to_csv('paises_europeos.csv', index=False)

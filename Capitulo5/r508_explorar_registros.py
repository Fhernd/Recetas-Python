
# Receta 5-8: Explorar los registros de un DataFrame

# head() y tail()

import pandas as pd

peliculas = pd.read_csv('movies.csv')

print(peliculas.head(20))

print(peliculas.tail(15))


# Receta 5-9: Obtener estadísticas básicas en un DataFrame.

import pandas as pd

peliculas = pd.read_csv('movies.csv')

print(peliculas.describe())

print(peliculas.movie_facebook_likes.max())

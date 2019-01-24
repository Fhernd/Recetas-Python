
# Receta 4-8: Guardar datos como objetos

import pickle

# paises = {'Colombia': 'Bogotá', 'Argentina': 'Buenos Aires'}
#
# archivo_paises = open('paises.pickle', 'wb')
#
# pickle.dump(paises, archivo_paises)

archivo = open('paises.pickle', 'rb')

paises_recuperados = pickle.load(archivo)

print(paises_recuperados)

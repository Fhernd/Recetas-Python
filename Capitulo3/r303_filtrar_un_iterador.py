
# Receta 3-3: Filtrar un iterador

numeros =range(10)

print(list(numeros))

impares_iterador = filter(lambda numero: numero % 2, numeros)

print(next(impares_iterador))
print(next(impares_iterador))
print(next(impares_iterador))

lista_impares = list(filter(lambda numero: numero % 2, numeros))

print(lista_impares)

import itertools

lista_pares = list(itertools.filterfalse(lambda numero: numero % 2, numeros))

print(lista_pares)

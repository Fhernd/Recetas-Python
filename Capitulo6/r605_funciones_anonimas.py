
# Receta Python 6-5: Uso de funciones anónimas.

# Operador lambda

numeros = [1, 2, 3, 4, 5]

numeros_cuadrados = list(map(lambda numero: numero ** 2, numeros))

print(numeros_cuadrados)

elevar_al_cuadrado = lambda numero: numero ** 2

numeros_cuadrados = list(map(elevar_al_cuadrado, numeros))

print(numeros_cuadrados)

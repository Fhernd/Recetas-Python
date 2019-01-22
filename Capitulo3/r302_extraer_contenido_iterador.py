
# Receta 3-2: Extraer el contenido de un iterador

# enumerate()

lenguajes = ['Python', 'Java', 'C#', 'PHP', 'C++']

enumerador_lenguajes = enumerate(lenguajes)

print(next(enumerador_lenguajes))
print(next(enumerador_lenguajes))
print(next(enumerador_lenguajes))

enumerador_lenguajes2 = enumerate(lenguajes, 5)

print(next(enumerador_lenguajes2))
print(next(enumerador_lenguajes2))
print(next(enumerador_lenguajes2))

for indice, elemento in enumerate(lenguajes):
    print(indice, elemento)

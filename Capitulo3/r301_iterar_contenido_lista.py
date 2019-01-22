
# Receta 3-1: Iterar una lista

primos = [2, 3, 5, 7, 11]

for primo in primos:
    print(primo)

iterador = iter(primos)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

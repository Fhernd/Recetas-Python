
# Receta 3-5: Iterar datos que tienen un iterador


def generar_cuadrado(valor=0):
    while True:
        valor += 1

        yield (valor - 1) ** 2


generador = generar_cuadrado()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

generador = generar_cuadrado(5)

print()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

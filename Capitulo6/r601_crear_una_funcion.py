
# Receta Python 6-1: Crear una función.


def calcular_cubo(x):
    """
    Calcula el cubo de un número.
    :param x: Número a calcular el cubo.
    :return: Cubo de un número.
    """
    cubo = x ** 3

    return cubo


print(calcular_cubo(3))
print(calcular_cubo(4))

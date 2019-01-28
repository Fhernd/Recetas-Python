
# Receta Python 6-2: Orden arbitrario de parámetros en una función


def calcular_cubo(x):
    """
    Calcula el cubo de un número.
    :param x: Número a calcular el cubo.
    :return: Cubo del número dado.
    """
    cubo = x ** 3

    return cubo


print(calcular_cubo(x=5))


def multiplicar(a, b, c):
    """
    Multiplica tres números.
    :param a: Número a
    :param b: Número b
    :param c: Número c
    :return: Multiplicación entre a, b y c
    """
    return a * b *c


print(multiplicar(2, 5, 7))
print(multiplicar(c=7, a=2, b=5))

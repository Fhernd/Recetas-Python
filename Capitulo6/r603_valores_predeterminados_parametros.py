
# Receta Python 6-3: Usar valores predeterminados para parámetros


def calcular_potencia(base, exponente=2):
    """
    Calcula la potencia.
    :param base: Base
    :param exponente: Exponente
    :return: Potencia.
    """
    return base ** exponente


print(calcular_potencia(5, 2))
print(calcular_potencia(7, 2))
print(calcular_potencia(8, 2))

print(calcular_potencia(5))
print(calcular_potencia(7))
print(calcular_potencia(8))

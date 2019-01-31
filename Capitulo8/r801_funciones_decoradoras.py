
# Receta Python 8-1: Crear funciones decoradoras.


def cambiar_a_mayusculas_decorador(funcion):
    def envoltura():
        resultado = funcion()

        mayusculas = resultado.upper()

        return mayusculas

    return envoltura


@cambiar_a_mayusculas_decorador
def saludar():
    return 'Hola... Bienvenidos al mundo Python'


print(saludar())

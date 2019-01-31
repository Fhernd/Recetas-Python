
# Receta Python 8-2: Decorar con wraps.

from functools import wraps


def funcion_decoradora(funcion):

    @wraps(funcion)
    def envoltura(*args, **kwds):
        print('Función decoradora invocada.')

        return funcion(*args, **kwds)

    return envoltura


@funcion_decoradora
def saludo():
    print('Hola')


saludo()


# Receta Python 8-5: Crear una metaclase.


class NoInstanciar(type):

    def __call__(self, *args, **kwargs):

        raise TypeError('No se pueden crear objetos de esta clase.')


class Constantes(metaclass=NoInstanciar):
    PI = 3.141592
    E = 2.718182
    EULER = 0.577215


# Generar error:
# c = Constantes()

print(Constantes.EULER)

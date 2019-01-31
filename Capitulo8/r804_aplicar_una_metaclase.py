
# Receta Python 8-4: Aplicar una metaclase.


# Tomado desde StackOverflow:

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConexionBaseDatos(metaclass=Singleton):
    pass


conexion1 = ConexionBaseDatos()
conexion2 = ConexionBaseDatos()

print(id(conexion1))
print(id(conexion2))

print(conexion1 == conexion2)

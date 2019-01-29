
# Receta Python 7-2: Crear una clase.


class Persona:
    def __init__(self, nombres, edad, id):
        self.nombres = nombres
        self.edad = edad
        self.id = id

    def __str__(self):
        return 'Nombres: {} - Edad: {} - ID: {}'.format(self.nombres, self.edad, self.id)


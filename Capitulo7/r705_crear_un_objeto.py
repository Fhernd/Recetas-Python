
# Receta Python 7-5: Crear una instancia u objeto de una clase.


class Persona:
    def __init__(self, nombres, edad, id):
        self.nombres = nombres
        self.edad = edad
        self.id = id

    def __str__(self):
        return 'Nombres: {} - Edad: {} - ID: {}'.format(self.nombres, self.edad, self.id)


fernanda = Persona('Fernanda Gómez', 29, '123852951')

print(fernanda)

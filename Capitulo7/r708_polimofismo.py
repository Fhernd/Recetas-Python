
# Receta Python 7-8: Crear comportamiento polimórfico.


class Perro:
    def hacer_sonido(self):
        print('Wow')


class Gato:
    def hacer_sonido(self):
        print('Meow')


def hacer_sonido(animal):
    animal.hacer_sonido()


gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)

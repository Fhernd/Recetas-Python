
# Receta Python 7-7: Cambiar el estado de un objeto.


class NumeroComplejo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def __lt__(self, otro):
        if self.real < otro.real and self.imaginaria < otro.imaginaria:
            return True
        else:
            return False

    def __gt__(self, otro):
        if self.real > otro.real and self.imaginaria > otro.imaginaria:
            return True
        else:
            return False

    def __eq__(self, otro):

        return self.real == otro.real and self.imaginaria == otro.imaginaria


numero1 = NumeroComplejo(1, 3)
print(numero1.real, numero1.imaginaria)

numero1.real = -5
numero1.imaginaria = 7
print(numero1.real, numero1.imaginaria)

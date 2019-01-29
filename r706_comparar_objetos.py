
# Receta Python 7-6: Comparar objetos.


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


numero1 = NumeroComplejo(3, 5)
numero2 = NumeroComplejo(2, 1)
numero3 = NumeroComplejo(3, 5)

print(numero1 > numero2)
print(numero1 == numero3)

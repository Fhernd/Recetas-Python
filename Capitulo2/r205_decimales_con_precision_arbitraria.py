
# Receta 2-5: Decimales con precisión arbitraria

from decimal import *

print(getcontext())

print(Decimal(1)/Decimal(3))

getcontext().prec = 7

print(Decimal(1)/Decimal(3))

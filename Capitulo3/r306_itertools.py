
# Receta 3-6: Módulo itertools

# accumulate
# combinations

rango = range(0, 10)

# 0 1 2 3 4 ...
# 0 1 3 6 ...

import itertools

acumulador = itertools.accumulate(rango)

print(next(acumulador))
print(next(acumulador))
print(next(acumulador))
print(next(acumulador))

combinaciones = itertools.combinations(rango, 2)

print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))

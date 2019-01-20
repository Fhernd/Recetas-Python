
# Receta 2-3: Redondear reales a enteros

pi = 3.1415

# 1. int()
# 2. trunc() del paquete math
# 3. round()

# 1:
print(type(pi))
print(int(pi))
print(type(int(pi)))

# 2:

from math import trunc

print()
print(trunc(pi))
print(type(trunc(pi)))

# 3:

print()
print(round(pi))

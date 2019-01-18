
# Conversión de cadenas de caracteres en valores numéricos:

# int(), float(), long(), y complex()

literal_entero = '123'
literal_decimal = '3.1415'
literal_entero_largo = '123456789456789456951753215679515647'
literal_complejo = '5+8j'

entero = int(literal_entero)
print(type(entero))
print(entero)

decimal = float(literal_decimal)
print(type(decimal))
print(decimal)

# Funciona para Python 2.x
# entero_largo = long(literal_entero_largo)
# print(type(entero_largo))
# print(entero_largo)

entero_largo = int(literal_entero_largo)
print(type(entero_largo))
print(entero_largo)

complejo = complex(literal_complejo)
print(type(complejo))
print(complejo)


# Receta 2-10: Convertir cadenas en horas y fechas

from datetime import datetime

fecha1 = datetime(year=1972, month=1, day=1)

print(fecha1)

fecha2 = datetime.strptime('1972-01-01', '%Y-%m-%d')

print(fecha2)

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

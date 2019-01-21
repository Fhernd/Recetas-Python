
# Receta 2-7: Obtener fecha y hora actuales

import datetime

hora_fecha_actual = datetime.datetime.now()

print(hora_fecha_actual)

hora = hora_fecha_actual.time()
fecha = hora_fecha_actual.date()

print(hora)
print(fecha)

print(hora.hour, hora.minute, hora.second)
print(fecha.year, fecha.month, fecha.day)

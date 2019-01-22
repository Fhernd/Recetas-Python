
# Receta 2-9: Formatear fechas

from datetime import datetime

fecha = datetime.now()

print(fecha)

print(fecha.strftime('%A, %d. %B %Y %I:%M:%S'))

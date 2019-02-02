
# Receta Python 9-6: Leer el contenido de una página Web.

import urllib.request

pagina_web = urllib.request.urlopen('https://www.python.org/')

print(pagina_web.read(200))

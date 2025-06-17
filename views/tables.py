import sys
import os

# Obtener la ruta actual del script
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta del directorio padre
ruta_padre = os.path.abspath(os.path.join(ruta_actual, ".."))

# Agregar la ruta del padre a la ruta de búsqueda (si no está ya)
if ruta_padre not in sys.path:
    sys.path.append(ruta_padre)

from cvs.read_cv import read_db

def p1():

    result = read_db()

    print(result)

p1()
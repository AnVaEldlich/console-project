"""
pequeño proyecto con python y mysql en consola
- Abrir asistente
- login o registro
- Si elegimos registro creare un usuario en la base de datos
- Si elegimos login verificare si el usuario existe
- Crear nota, mostrar notas, borrarlas.

"""

from usuarios import acciones

hazEl = acciones.Acciones()
print("""

Bienvenido al sistema

Acciones disponibles:

1. Login
2. Registro

""")

ac = input("Elige una accion: ")

if ac == "2":
   hazEl.registro()

elif ac == "1":
   hazEl.login()


// hkhlkhl// jkjkjk// jkjkjk
// jkjkjk
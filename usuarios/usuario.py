import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3080",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)


class Usuario:

    def __init__(self, nombre, appelido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password


    def registrar(self):
        return self.nombre
    
    def identificar(self):
        return self.nombre


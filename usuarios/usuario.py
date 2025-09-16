import mysql.connector
import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3080",
    database="master_python",
    port=3306
)

cursor = db.cursor(buffered=True)


class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password


    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO users  VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.password, fecha)
        cursor.execute(sql, usuario)
        db.commit()

        return [cursor.rowcount, self]

    def identificar(self):
        return self.nombre



import datetime
import hashlib
import usuarios.conexion as conexion

conn = conexion.connect()
db = conn[0]
cursor = conn[1]


class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password


    def registrar(self):
        fecha = datetime.datetime.now()

        # Encriptar contraseña
        hash = hashlib.sha256()
        hash.update(self.password.encode('utf-8'))
        self.password = hash.hexdigest()

        sql = "INSERT INTO users  VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.password, fecha)

        try:
            cursor.execute(sql, usuario)
            db.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            # Podríamos loguear e para depurar, pero en consola mostramos un mensaje simple
            result = [0, self]

        return result

    def identificar(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        hash = hashlib.sha256()
        hash.update(self.password.encode('utf-8'))
        self.password = hash.hexdigest()

        usuario = (self.email, self.password)

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result

        


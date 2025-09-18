
import usuarios.conexion as conexion

conn = conexion.connect()
db = conn[0]
cursor = conn[1]

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, Now())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        
        cursor.execute(sql, nota)
        db.commit()

        return [cursor.rowcount, self]
        
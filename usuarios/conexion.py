import mysql.connector

def connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3080",
        database="master_python",
        port=3306
    )

    cursor = db.cursor(buffered=True)

    return [db, cursor]

# Mantener compatibilidad con el nombre mal escrito existente en el código
def conncet():
    return connect()



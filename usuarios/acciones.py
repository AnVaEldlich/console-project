import usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarte")
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")    

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con exito")
        else:
            print("\nNo se ha registrado correctamente")

    def login(self):
        print("\nOk, vamos a loguearte")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")

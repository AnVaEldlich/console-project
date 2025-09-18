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
            print(f"\nPerfecto {registro[1].nombre} te has registrado con exito con el correo {registro[1].email}")
        else:
            print("\nNo se ha registrado correctamente")

    def login(self):
        print("\nOk, vamos a loguearte")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        usuario = modelo.Usuario('', '', email, password)
        try: 

            login = usuario.identificar()

            # login puede ser None si no se encuentra el usuario o las credenciales son incorrectas
            if not login:
                print("\nCredenciales incorrectas o usuario no encontrado.")
                return

            # Estructura esperada: (id, nombre, apellido, email, password, fecha)
            if email == login[3]:
                print("\nPerfecto has iniciado sesión con éxito")
                self.proximasAcciones(login)
            else:
                print("\nCredenciales incorrectas o usuario no encontrado.")
          

        except Exception as e:
            print(e)
            print(f"El login es incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        
        ¿Que quieres hacer?  

        1. Crear nota
        2. Mostrar notas
        3. Borrar nota
        4. Salir

        """)

        accion = input("Elige una accion: ")

        if accion == "1":
            print("\nOk, vamos a crear una nota")
            titulo = input("Introduce el titulo de la nota: ")
            descripcion = input("Introduce el contenido de la nota: ")

            usuario.crearNota(titulo, descripcion)
            print("\nPerfecto has creado la nota con exito")

        elif accion == "2":
            print("\nOk, vamos a mostrar tus notas")
            usuario.mostrarNotas()

        elif accion == "3":
            print("\nOk, vamos a borrar una nota")
            usuario.borrarNota()

        elif accion == "4":
            print(f"\nOk, vamos a salir, hasta pronto {usuario[1]}")
            exit()



     
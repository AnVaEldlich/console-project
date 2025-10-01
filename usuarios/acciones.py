import usuarios.usuario as modelo
import usuarios.notas.acciones as notas_acciones

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
        hazEl = notas_acciones.Acciones()

        if accion == "1":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "2":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "3":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "4":
            print(f"\nOk, vamos a salir, hasta pronto {usuario[1]}")
            exit()



     
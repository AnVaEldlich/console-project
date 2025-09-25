from usuarios.notas import nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk, {usuario[1]} vamos a crear una nota")
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("\nPerfecto has creado la nota con exito")
        else:
            print("\nNo se ha creado la nota correctamente")

    def mostrar(self, usuario):
        print(f"\nOk, {usuario[1]} vamos a mostrar tus notas")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print("\n--------------------------------")
            print(nota[2])
            print(nota[3])
            print("--------------------------------\n")


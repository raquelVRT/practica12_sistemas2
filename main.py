from alquiler import alquiler
from libro import libro
from usuario import usuario


class main:
    def __init__(self):
        self.catalogo = []  # Catálogo de libros en un array
        self.alquiler_instance = alquiler()  # Crear una instancia de la clase alquiler
        self.usuario = usuario(self.alquiler_instance, self.catalogo)  # Crear un usuario con el alquiler y el catálogo

    # Método para agregar un nuevo libro al catálogo
    def agregar_libro_catalogo(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        cantidad = int(input("Ingrese la cantidad de libros: "))
        nuevo_libro = libro(titulo, autor, cantidad)
        self.catalogo.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado al catálogo.")

    # Método para mostrar el menú y ejecutar la opción seleccionada
    def ejecutar(self):
        while True:
            print("\nBienvenido a la biblioteca Rib, ¿qué quieres hacer?")
            print("Opción 1: Añadir un libro al catálogo")
            print("Opción 2: Mostrar el catálogo de libros")
            print("Opción 3: Alquilar un libro")
            print("Opción 4: Mostrar tu lista de alquiler actual")
            print("Opción 5: Buscar un libro por ID")
            print("Opción 6: Salir")

            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.agregar_libro_catalogo()
                elif opcion == 2:
                    self.usuario.mostrar_catalogo()
                elif opcion == 3:
                    self.usuario.alquilar_libro()
                elif opcion == 4:
                    self.alquiler_instance.mostrar_alquiler()
                elif opcion == 5:
                    id_libro = int(input("Ingrese el ID del libro a buscar: "))
                    print(self.alquiler_instance.buscar_libro_por_id(id_libro))
                elif opcion == 6:
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")


# Ejecuta la aplicación solo si el script se ejecuta directamente
if __name__ == "__main__":
    print("Ejecutando el programa...")
    app = main()  # Crear la instancia de la aplicación
    app.ejecutar()  # Ejecutar el menú de la aplicación
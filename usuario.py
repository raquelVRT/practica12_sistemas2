import math

import libro

class usuario:
    def __init__(self, alquiler_instance, catalogo):
        self.alquiler = alquiler_instance  # Instancia de la clase alquiler
        self.catalogo = catalogo  # Catalogo de libros para el usuario

    # Método para alquilar un libro desde el catálogo
    def alquilar_libro(self):
        id_libro = int(input("Ingrese el ID del libro que desea alquilar: "))
        libro = next((lib for lib in self.catalogo if lib.id == id_libro), None)
        if libro:
            self.alquiler.agregar_libro(libro)
        else:
            print("Libro no encontrado en el catálogo.")

    # Método para mostrar el catálogo de libros disponibles
    def mostrar_catalogo(self):
        if not self.catalogo:
            print("El catálogo está vacío.")
        else:
            print("\nCatálogo de libros disponibles:")
            for libro in self.catalogo:
                print(libro.mostrar_info())
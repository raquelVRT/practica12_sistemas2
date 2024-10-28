import math

class alquiler:
    def __init__(self):
        self.libros = []  # Lista vacía para almacenar los libros en alquiler
        self.max_libros = 3  # Máximo de libros permitidos en alquiler

    # Método para agregar un libro al alquiler con límite de 3 libros
    def agregar_libro(self, libro):
        if len(self.libros) >= self.max_libros:
            print("No puedes alquilar más de tres libros.")
        else:
            self.libros.append(libro)
            print(f"Libro '{libro.titulo}' agregado al alquiler.")
            print(f"Libros en el alquiler: {len(self.libros)}/{self.max_libros}")

    # Método para mostrar todos los libros en el alquiler
    def mostrar_alquiler(self):
        if not self.libros:
            print("El alquiler está vacío.")
        else:
            for libro in self.libros:
                print(libro.mostrar_info())

    # Método para buscar un libro por ID con manejo de excepciones
    def buscar_libro_por_id(self, id_libro):
        try:
            libro = next(lib for lib in self.libros if lib.id == id_libro)
            return libro.mostrar_info()
        except StopIteration:
            return "Libro no encontrado."
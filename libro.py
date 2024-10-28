import math


class libro:
    id_contador = 1  # Contador de ID para cada libro

    def __init__(self, titulo, autor, cantidad):
        self.id = libro.id_contador  # Asigna el valor actual del contador como ID único
        libro.id_contador += 1  # Incrementa el contador para el próximo libro
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    # Método para mostrar la información del libro
    def mostrar_info(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Cantidad: {self.cantidad}"

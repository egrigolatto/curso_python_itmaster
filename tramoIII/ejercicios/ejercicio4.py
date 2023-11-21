'''Cree una clase Biblioteca y una clase Estante. Una biblioteca tiene muchos estantes, pero un estante puede existir sin pertenecer a ninguna biblioteca.'''

class Biblioteca:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre  # Nombre de la biblioteca
        self.ubicacion = ubicacion  # Ubicación de la biblioteca
        self.estantes = []  # Inicialmente, la lista de estantes está vacía

    def agregar_estante(self, nombre):
        nuevo_estante = Estante(nombre)
        self.estantes.append(nuevo_estante)
        return nuevo_estante

class Estante:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del estante

    def __str__(self):
        return f"Estante: {self.nombre}"

# Ejemplo de uso:
biblioteca1 = Biblioteca("Biblioteca Central", "Ciudad Y")  # Creamos una biblioteca
estante1 = biblioteca1.agregar_estante("Ficción")  # Agregamos un estante a la biblioteca
estante2 = Estante("No-Ficción")  

print(f"{biblioteca1.nombre} tiene los siguientes estantes:")
for estante in biblioteca1.estantes:
    print(estante)

print(f"Estante independiente: {estante2.nombre}")

'''
Cree clases Escritor y Libro. Un escritor ha escrito varios libros, pero un libro solo tiene un escritor.
'''

class Escritor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre  # Nombre del escritor
        self.nacionalidad = nacionalidad  # Nacionalidad del escritor
        self.libros_escritos = []  # Inicialmente, la lista de libros escritos está vacía

    def escribir_libro(self, titulo, genero):
        # Método para que el escritor escriba un libro
        nuevo_libro = Libro(titulo, genero, self)  # Creamos un nuevo objeto Libro
        self.libros_escritos.append(nuevo_libro)  # Agregamos el libro a la lista de libros escritos por el autor
        return nuevo_libro  # Devolvemos el libro recién creado

class Libro:
    def __init__(self, titulo, genero, autor):
        self.titulo = titulo  # Título del libro
        self.genero = genero  # Género del libro
        self.autor = autor  # Referencia al autor del libro

    def __str__(self):
        return f"Libro: {self.titulo}, Género: {self.genero}, Autor: {self.autor.nombre}"

# Ejemplo de uso:
autor1 = Escritor("J.K. Rowling", "Británica")  # Creamos un autor
libro1 = autor1.escribir_libro("Harry Potter y la Piedra Filosofal", "Fantasía")  # El autor escribe un libro
libro2 = autor1.escribir_libro("Harry Potter y la Cámara Secreta", "Fantasía")  # El autor escribe otro libro

print(f"{autor1.nombre} ha escrito los siguientes libros:")
for libro in autor1.libros_escritos:
    print(libro)

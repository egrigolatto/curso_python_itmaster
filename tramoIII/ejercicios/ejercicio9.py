'''Cree clases Página, Capítulo y Libro. Un libro está compuesto por varios capítulos, y cada capítulo tiene varias páginas. Si se destruye el libro, se destruyen los capítulos y sus respectivas páginas.'''

class Página:
    def __init__(self, contenido):
        self.contenido = contenido  # Contenido de la página

class Capítulo:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del capítulo
        self.páginas = []  # Lista de páginas del capítulo

class Libro:
    def __init__(self, capítulos):
        self.capítulos = capítulos  # Lista de capítulos en el libro

    def destruir_libro(self):
        # Al destruir el libro, los capítulos y sus páginas también se destruyen
        for capítulo in self.capítulos:
            for página in capítulo.páginas:
                del página
            del capítulo

# Ejemplo de uso:
página1 = Página("Contenido de la página 1")
página2 = Página("Contenido de la página 2")
capítulo1 = Capítulo("Introducción")
capítulo1.páginas.extend([página1, página2])
página3 = Página("Contenido de la página 3")
página4 = Página("Contenido de la página 4")
capítulo2 = Capítulo("Desarrollo")
capítulo2.páginas.extend([página3, página4])
mi_libro = Libro([capítulo1, capítulo2])

# Destruir el libro
mi_libro.destruir_libro()

# Intentar acceder a los capítulos o páginas después de la demolición generará errores
# Por ejemplo, esto generará un error:
# print(capítulo1.nombre)


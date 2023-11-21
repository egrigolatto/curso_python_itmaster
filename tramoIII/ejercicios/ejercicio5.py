'''Defina clases Orquesta y Instrumento. Una orquesta utiliza varios instrumentos, pero un instrumento puede existir sin estar en ninguna orquesta.'''

class Orquesta:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la orquesta
        self.instrumentos = []  # Inicialmente, la lista de instrumentos utilizados está vacía

    def agregar_instrumento(self, nombre_instrumento):
        nuevo_instrumento = Instrumento(nombre_instrumento)
        self.instrumentos.append(nuevo_instrumento)
        return nuevo_instrumento

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del instrumento

    def __str__(self):
        return f"Instrumento: {self.nombre}"

# Ejemplo de uso:
orquesta1 = Orquesta("Orquesta Sinfónica")  # Creamos una orquesta
instrumento1 = orquesta1.agregar_instrumento("Violín")  # Agregamos un instrumento a la orquesta
instrumento2 = Instrumento("Piano")  # Creamos un instrumento independiente

print(f"{orquesta1.nombre} utiliza los siguientes instrumentos:")
for instrumento in orquesta1.instrumentos:
    print(instrumento)

print(f"Instrumento independiente: {instrumento2.nombre}")

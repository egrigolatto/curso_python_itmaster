'''Cree clases Cuarto, Puerta y Casa. Una casa está compuesta por varios cuartos, y cada cuarto tiene una puerta. Si la casa es demolida, los cuartos y las puertas también se destruyen.'''

class Cuarto:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del cuarto
        self.puerta = Puerta(self)  # Cada cuarto tiene una puerta

class Puerta:
    def __init__(self, cuarto):
        self.cuarto = cuarto  # Referencia al cuarto al que pertenece

class Casa:
    def __init__(self, cuartos):
        self.cuartos = cuartos  # Lista de cuartos en la casa

    def demoler_casa(self):
        # Al demoler la casa, los cuartos y las puertas también se destruyen
        for cuarto in self.cuartos:
            del cuarto

# Ejemplo de uso:
cuarto1 = Cuarto("Sala de estar")
cuarto2 = Cuarto("Dormitorio")
cuarto3 = Cuarto("Cocina")
mi_casa = Casa([cuarto1, cuarto2, cuarto3])

# Demoler la casa
mi_casa.demoler_casa()

# Intentar acceder a los cuartos o puertas después de la demolición generará errores
# Por ejemplo, esto generará un error:
# print(cuarto1.nombre)

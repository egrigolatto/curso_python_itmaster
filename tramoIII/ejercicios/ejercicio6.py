'''Cree clases Aeropuerto y Avión. Un aeropuerto puede tener varios aviones estacionados, pero un avión puede existir sin pertenecer a ningún aeropuerto.'''

class Aeropuerto:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre  # Nombre del aeropuerto
        self.ubicacion = ubicacion  # Ubicación del aeropuerto
        self.aviones_estacionados = []  # Inicialmente, la lista de aviones estacionados está vacía

    def estacionar_avion(self, numero_serie):
        nuevo_avion = Avion(numero_serie)
        self.aviones_estacionados.append(nuevo_avion)
        return nuevo_avion

class Avion:
    def __init__(self, numero_serie):
        self.numero_serie = numero_serie  # Número de serie del avión

    def __str__(self):
        return f"Avión con Número de Serie: {self.numero_serie}"

# Ejemplo de uso:
aeropuerto1 = Aeropuerto("Aeropuerto Internacional", "Ciudad Z")  # Creamos un aeropuerto
avion1 = aeropuerto1.estacionar_avion("ABC123")  # Estacionamos un avión en el aeropuerto
avion2 = Avion("XYZ789")  # Creamos un avión independiente

print(f"{aeropuerto1.nombre} tiene los siguientes aviones estacionados:")
for avion in aeropuerto1.aviones_estacionados:
    print(avion)

print(f"Avión independiente: {avion2.numero_serie}")

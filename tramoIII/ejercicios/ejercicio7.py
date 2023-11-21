'''Cree clases Motor, Rueda y Coche. Un coche está compuesto por un motor y cuatro ruedas. Si el coche es destruido, el motor y las ruedas también lo son.'''

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo  # Tipo de motor

class Rueda:
    def __init__(self, marca):
        self.marca = marca  # Marca de la rueda

class Coche:
    def __init__(self, motor, ruedas):
        self.motor = motor  # Motor del coche
        self.ruedas = ruedas  # Lista de cuatro ruedas del coche

    def destruir_coche(self):
        # Al destruir el coche, el motor y las ruedas también se destruyen
        del self.motor
        for rueda in self.ruedas:
            del rueda

# Ejemplo de uso:
motor_del_coche = Motor("Gasolina")  # Creamos un motor para el coche
ruedas_del_coche = [Rueda("Michelin"), Rueda("Michelin"), Rueda("Michelin"), Rueda("Michelin")]  # Creamos cuatro ruedas para el coche
coche = Coche(motor_del_coche, ruedas_del_coche)  # Creamos el coche

# Destruir el coche
coche.destruir_coche()

# Intentar acceder a los componentes del coche después de la destrucción generará errores
# Por ejemplo, esto generará un error:
# print(coche.motor)

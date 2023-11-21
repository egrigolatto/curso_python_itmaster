'''Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes'''

class Boleteria:
    def __init__(self, evento, cantidad_localidades):
        self.evento = evento
        self.cantidad_total_localidades = cantidad_localidades
        self.localidades_vendidas = 0

    def vender_localidades(self, cantidad):
        if self.localidades_vendidas + cantidad > self.cantidad_total_localidades:
            raise ValueError("No hay localidades suficientes")
        self.localidades_vendidas += cantidad

    def localidades_agotadas(self):
        return self.localidades_vendidas == self.cantidad_total_localidades

    def __str__(self):
        return f"Evento: {self.evento} - Localidades vendidas: {self.localidades_vendidas} de {self.cantidad_total_localidades}"

# Ejemplo de uso:
b = Boleteria("Rush", 500)
print(b)  # Imprime "Evento: Rush - Localidades vendidas: 0 de 500"
print(b.localidades_agotadas())  # False

b.vender_localidades(100)
b.vender_localidades(400)

print(b.localidades_agotadas())  # True
print(b)  # Imprime "Evento: Rush - Localidades vendidas: 500 de 500"

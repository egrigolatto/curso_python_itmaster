'''Implementar la clase CajaFuerte, que recibe en su constructor la cantidad de objetos que puede contener, y tiene el siguiente comportamiento:

c = CajaFuerte(12345,20)    
c.abrir(12345)
c.poner("Reloj")
c.poner("Cadena")
c.poner(1000)
c.cerrar()
c.poner("Reloj Oro") ==> ValueError ("La caja esta cerrada")
c.abrir(3456) ==> ValueError ("Error en la clave")
c.abrir(12345)
c.sacar("Cadena")
c.sacar("Tortuga")  ==> ValueError ("El objeto Tortuga no esta en la caja")
c.abrir(12345) ==> ValueError("La caja esta abierta")
c.cerrar()'''

class CajaFuerte:
    def __init__(self, clave, capacidad):
        self.clave = clave
        self.capacidad = capacidad
        self.abierta = False
        self.contenido = []

    def abrir(self, clave_ingresada):
        if not self.abierta:
            if clave_ingresada == self.clave:
                self.abierta = True
            else:
                raise ValueError("Error en la clave")
        else:
            raise ValueError("La caja está abierta")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
        else:
            raise ValueError("La caja está cerrada")

    def poner(self, objeto):
        if self.abierta:
            if len(self.contenido) < self.capacidad:
                self.contenido.append(objeto)
            else:
                raise ValueError("La caja está llena")
        else:
            raise ValueError("La caja está cerrada")

    def sacar(self, objeto):
        if self.abierta:
            if objeto in self.contenido:
                self.contenido.remove(objeto)
            else:
                raise ValueError(f"El objeto {objeto} no está en la caja")
        else:
            raise ValueError("La caja está cerrada")

# Ejemplo de uso:
c = CajaFuerte(12345, 20)
c.abrir(12345)
c.poner("Reloj")
c.poner("Cadena")
c.poner(1000)
c.cerrar()

try:
    c.poner("Reloj Oro")
except ValueError as e:
    print(e)

try:
    c.abrir(3456)
except ValueError as e:
    print(e)

c.abrir(12345)
c.sacar("Cadena")

try:
    c.sacar("Tortuga")
except ValueError as e:
    print(e)

try:
    c.abrir(12345)
except ValueError as e:
    print(e)

c.cerrar()

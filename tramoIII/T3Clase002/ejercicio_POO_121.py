"""
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la
cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes
"""
class Boleteria:
    def __init__(self,nombre_evento,cantidad_localidades) -> None:
        self.nombre_evento = nombre_evento
        self.cantidad_localidades = cantidad_localidades
        self.cantidad_actual = 0


    def vender_localidades(self,cantidad)->None:
        self.cantidad_actual -= cantidad

    def localidades_agotadas(self)->bool:
        return self.cantidad_actual == self.cantidad_localidades
    
    def __str__(self) -> str:
        pass


class EmpresaVentaEntradas:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.boleterias:list[Boleteria] = []

    def agregar_boleteria(self,boleteria:Boleteria)->None:
        self.boleterias.append(boleteria)    
    
    def comprar_entrada(self,nombre_evento,cantidad_entradas)->None:
        evento_encontrado = self.__buscar_evento(nombre_evento)
        if evento_encontrado:
            if evento_encontrado.localidades_agotadas():
                print("Localidades agotadas")
            elif evento_encontrado.

    def __buscar_evento(self,nombre_evento)->Boleteria:
        for evento in self.boleterias:
            if evento.nombre_evento == nombre_evento:
                return evento
        return None


def main():
    b = Boleteria("Palito Ortega",1000)


main()
from os import system
from txtcolores import strclr
import utilidades as util
from abc import ABC, abstractmethod
from cartas import CartaPoker, Carta, CartaEspaniola
from mazos import Mazo, MazoBlackJack
import random


class JugadorCartas(ABC):

    def __init__(self, nombre: str, mazo: Mazo) -> None:
        self.__nombre: str = nombre
        self.__mano: Mazo = mazo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def mano(self) -> Mazo:
        return self.__mano

    def __str__(self) -> str:
        return f"{self.nombre} ==< {self.mano}"




class Plantable(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def me_planto(self) -> bool:
        pass


class JugadorBlackJack(JugadorCartas, Plantable):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre, MazoBlackJack())

    def poner_carta(self, carta: CartaPoker, index: int = None) -> None:
        self.mano.poner_carta(carta, index)

    def sacar_carta(self, index: int = None) -> CartaPoker:
        return self.mano.sacar_carta(index)

    def sumar_cartas(self) -> int:
        cantidad_unos = 0
        suma_numeros = 0
        for carta in self.mano:
            if carta.numero == 1:
                cantidad_unos += 1
            elif carta.numero >= 10:
                suma_numeros += 10
            else:
                suma_numeros += carta.numero
        
        suma = 0
        if cantidad_unos == 0:
            suma = suma_numeros
        elif cantidad_unos == 1:
            if 11 + suma_numeros > 21:
                suma = 1 + suma_numeros
            else:
                suma = 11 + suma_numeros
        else:
            if 11 + suma_numeros  + (cantidad_unos - 1) > 21:
                suma = cantidad_unos + suma_numeros
            else:
                suma = 11 + suma_numeros +  (cantidad_unos - 1)
        
        return suma


class Croupier(JugadorBlackJack):
    def __init__(self) -> None:
        super().__init__('Sr. Croupier')

    def me_planto(self) -> bool:
        respuesta = True
        suma = self.sumar_cartas()
        print(f"{str(self)} ({suma})")
        if suma > 21:
            print(strclr("Se paso", 'red'))
            system('pause')
        elif suma >= 17:
            print("¿Se planta? [S/N]: S")
            system('pause')
        else:
            respuesta = False
        return respuesta


class Apostable(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def apuesto(self) -> int:
        pass


class Cliente(JugadorBlackJack, Apostable):
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre)
        self.__fichas: int = fichas

    @abstractmethod
    def me_retiro(self)->bool:
        pass

    @property
    def fichas(self) -> int:
        return self.__fichas

    def ganar_fichas(self, cantidad: int) -> None:
        self.__fichas += cantidad

    def perder_fichas(self, cantidad: int) -> None:
        self.__fichas -= cantidad

    def __str__(self) -> str:
        return f"{super().__str__()} ${self.fichas} ({self.sumar_cartas()})"


class Humano(Cliente):
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)

    def apuesto(self) -> int:
        print(self)
        return util.leer_entero("Cantidad fichas: ", 1, self.fichas)

    def me_planto(self) -> bool:
        respuesta = True
        print(self)
        suma = self.sumar_cartas()
        if suma > 21:
            print(strclr("Se paso", 'red'))
            system('pause')

        elif suma == 21:
            print("¿Se planta? [S/N]: S")
            system('pause')

        else:
            respuesta = util.continua("¿Se planta?")
        return respuesta

    def me_retiro(self) -> bool:
        return super().me_retiro()


class JugadorAlien:
    pass

class AdaptadorCliente(Cliente):
    def __init__(self, jugador:JugadorAlien) -> None:
        super().__init__("Alien", 0)
        self.__atributo_alien:JugadorAlien = jugador

    def me_planto(self) -> bool:
        pass    
    
    def apuesto(self) -> int:
        pass
    
    def me_retiro(self) -> bool:
        return super().me_retiro()

class Compu(Cliente):
    TRAN: int = 1
    LOCO: int = 100

    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)
        self.__personalidad: int = self.__obtener_personalidad()

    @property
    def personalidad(self) -> int:
        return self.__personalidad

    def apuesto(self) -> int:
        print(self)
        pensamiento = self.__pensar()
        if pensamiento < self.personalidad: # personalidad 10
            desde = self.fichas//2
            hasta = self.fichas
        else:
            desde = 1
            hasta = self.fichas//2
        cantidad = random.randint(desde, hasta)
        print(f"Cantidad fichas: {cantidad}")
        #system("pause")
        return cantidad

    def me_planto(self) -> bool:
        respuesta = True
        print(self)
        suma = self.sumar_cartas()
        if suma > 21:
            print(strclr("Se paso", 'red'))
            #system('pause')
            return True  # ******************************* no!!
        elif suma == 21:
            letra = 'S'
        else:  # DONDE SE PIENSA
            pensamiento = self.__pensar()  # PERSONALIDAD
            if suma >= 12:
                if pensamiento < self.personalidad:
                    respuesta = False
                    letra = 'N'
                else:
                    respuesta = True
                    letra = 'S'
            else:
                letra = 'N'
        print(f"¿Se planta? [S/N]: {letra}")
        #system('pause')
        return respuesta

    def me_retiro(self) -> bool:
        return super().me_retiro()

    def __pensar(self) -> int:
        return random.randint(Compu.TRAN, Compu.LOCO)

    def __obtener_personalidad(self) -> int:
        return random.randint(Compu.TRAN, Compu.LOCO)


if __name__ == "__main__":
    
    m = MazoBlackJack()
    m.llenar()
    m.barajar()
    print(len(m))
    cr = Croupier()
    c = m.sacar_carta()
    c.tapar()
    cr.poner_carta(c)
    cr.poner_carta(m.sacar_carta())
    print(cr)

    h = Humano("Juan", 200)
    h.poner_carta(m.sacar_carta())
    h.poner_carta(m.sacar_carta())
    print(h)
    c = h.sacar_carta()
    c.tapar()
    h.poner_carta(c, 0)
    print(h)
    print(len(m))

    otro = AdaptadorCliente()
    
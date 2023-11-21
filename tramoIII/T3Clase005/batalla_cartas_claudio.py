"""
Reglas del Juego "Batalla de Cartas":
El juego se juega entre dos jugadores.
Cada jugador recibe la mitad del mazo (26 cartas) al azar.
Los jugadores revelan la carta superior de su mazo.
El jugador con la carta de mayor valor toma ambas cartas y las coloca en el fondo de su mazo.
Si ambas cartas son del mismo valor, se coloca en un "pozo" y se revela la siguiente carta. 
El jugador con la carta de mayor valor en la siguiente ronda toma todas las cartas del 
"pozo" y las coloca en el fondo de su mazo.
El juego termina cuando uno de los jugadores no tiene más cartas o después de un número 
determinado de rondas (por ejemplo, 50 rondas). 
El jugador con más cartas al final gana.
"""
from cartas import CartaPoker
from mazos import MazoPoker


class BatallaCartas:

    
    def __init__(self, jugador1:str, jugador2:str) -> None:
        self.__jugador1:str = jugador1
        self.__jugador2:str = jugador2
        self.__mazo1 = MazoPoker()
        self.__mazo2 = MazoPoker()
        self.__pozo = MazoPoker()

    def repartir(self)->None:
        mazo_original = MazoPoker(True, True)
        mazo_original.barajar()

        orden = 1
        while not mazo_original.isvacio():
            carta = mazo_original.sacar_carta()
            if orden%2 == 0:
                self.__mazo1.poner_carta(carta)
            else:
                self.__mazo2.poner_carta(carta)
            orden += 1 

    def jugar(self)->None:

        self.repartir()

        num = 0
        while (not self.__mazo1.isvacio()) and (not self.__mazo2.isvacio()) and (num < 50) : 

            carta1 = self.__mazo1.sacar_carta()
            carta2 = self.__mazo2.sacar_carta()
            carta2.destapar()
            carta1.destapar()
            print(f'JUGADA {num+1}: Carta de {self.__jugador1} ====> {carta1} {carta2} <==== Carta de {self.__jugador2}')
            carta2.tapar()
            carta1.tapar()

            if carta1.get_numero() > carta2.get_numero():
                ganador = self.__mazo1
            elif carta1.get_numero() < carta2.get_numero():
                ganador = self.__mazo2
            else:
                ganador = self.__pozo
            
            ganador.poner_carta(carta1)
            ganador.poner_carta(carta2)
            while not self.__pozo.isvacio() and ganador != self.__pozo:
                carta = self.__pozo.sacar_carta()
                ganador.poner_carta(carta) 

            num += 1

                
        print(f'Mazo de {self.__jugador1}: {self.__mazo1}')
        print(f'Mazo de {self.__jugador2}: {self.__mazo2}')

        if self.__mazo1.__len__() > self.__mazo2.__len__():
            print(f'El ganador es {self.__jugador1} con {self.__mazo1.__len__()} cartas, contra {self.__mazo2.__len__()} de {self.__jugador2}')
        elif self.__mazo1.__len__() < self.__mazo2.__len__():
            print(f'El ganador es {self.__jugador2} con {self.__mazo2.__len__()} cartas, contra {self.__mazo1.__len__()} de {self.__jugador1}')
        else:
            print(f'Empataron con {self.__mazo1.__len__()}')
        


def main():
    BatallaCartas('Juan', 'Pepe').jugar()

main()










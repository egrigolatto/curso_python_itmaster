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

class Jugador:
    """
    Clase Jugador, se inicializa con un nombre.

    Métodos públicos:

    juega_carta()   -> pone una carta en la mesa y la misma se muestra.
    toma_carta()    -> toma una carta de la mesa y se la queda.
    toma_pozo()     -> toma las cartas del pozo.

    """
    def __init__(self,nombre:str) -> None:
        """
        Inicializa un jugador con un nombre.

        Args:
            nombre (str): Nombre del jugador.

        Raises:
            ValueError: Si el número o palo no es válido.
        """
        self.__nombre = nombre
        self.__cartas: list[CartaPoker] = []

    def juega_carta(self) -> CartaPoker:
        """
        Hace que el jugador juegue una carta en la mesa, la misma se muestra.

        Args:
            Ninguno.

        Returns:
            La carta (CartaPoker) jugada.
        """
        carta= self.__cartas.pop(0)
        print (f"{self.__nombre} juega {carta}")
        return carta

    def toma_carta(self, carta:CartaPoker) -> None:
        """
        Hace que el jugador tome una carta de la mesa.

        Args:
            Una carta (CartaPoker).

        Returns:
            Nada.
        """
        self.__cartas.append(carta)

    def toma_pozo(self, pozo: MazoPoker) -> MazoPoker:
        """
        Hace que el jugador tome todas las cartas del pozo.

        Args:
            El pozo (MazoPoker).

        Returns:
            El pozo (MazoPoker) vacío.
        """
        for i in range(pozo.__len__()):
            self.__cartas.append(pozo.sacar_carta())
        return pozo

    def __str__(self) -> str:
        return f"Cartas {self.__nombre} ==> {''.join([str(carta) for carta in self.__cartas])}"

    def __len__(self) -> int:
        return len(self.__cartas)
    
    def get_nombre(self) -> str:
        return self.__nombre
   


class BatallaCartas:
    
    def __init__(self,nombre_jug1:str,nombre_jug2:str, rondas:int=500) -> None:
        self.__jugador1 = Jugador(nombre_jug1)
        self.__jugador2 = Jugador(nombre_jug2)
        self.__RONDAS= rondas

    def __repartir_mazo(self, jug1: Jugador, jug2: Jugador) -> None:
        mazo= MazoPoker(True)
        mazo.barajar()

        for a in range(0,52):
            carta= mazo.sacar_carta()
            if a%2==0:
                jug1.toma_carta(carta)
            else:
                jug2.toma_carta(carta)

    def __compara_cartas(self, jug1: Jugador, jug2: Jugador, pozo: MazoPoker) -> MazoPoker:
        carta_jug1= jug1.juega_carta()
        carta_jug2= jug2.juega_carta()

        if carta_jug1.get_numero()>carta_jug2.get_numero():
            jug1.toma_carta(carta_jug1)
            jug1.toma_carta(carta_jug2)
            print (f"Gana {jug1.get_nombre()}")
            if pozo.__len__()>0:
                jug1.toma_pozo(pozo)

        elif carta_jug1.get_numero()<carta_jug2.get_numero():
            jug2.toma_carta(carta_jug2)
            jug2.toma_carta(carta_jug1)
            print (f"Gana: {jug2.get_nombre()}")
            if pozo.__len__()>0:
                jug2.toma_pozo(pozo)
        else:
            pozo.poner_carta(carta_jug1)
            pozo.poner_carta(carta_jug2)
            print (f"Empate, pozo: {pozo}")

        print (f"{jug1.get_nombre()}: {jug1.__len__()} - {jug2.get_nombre()}: {jug2.__len__()} - Pozo: {pozo.__len__()}\n")

        return pozo    

                
    def jugar(self):
        self.__repartir_mazo(self.__jugador1,self.__jugador2)
        pozo= MazoPoker()
        mano= 1
        print(f"\n{self.__jugador1}")
        print(f"{self.__jugador2}\n")

        while len(self.__jugador1)>0 and len(self.__jugador2)>0 and mano<self.__RONDAS:
            print (f"Ronda {mano}")
            self.__compara_cartas(self.__jugador1, self.__jugador2, pozo)
            mano += 1

        if mano==self.__RONDAS:
            print (f"Juego finalizado por alcanzar {mano} rondas")
        else:
            print (f"Juego finalizado en {mano} rondas")

def main():
    BatallaCartas("Juana", "Pablo").jugar()


main()

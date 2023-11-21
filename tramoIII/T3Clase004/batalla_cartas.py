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
    

    def jugar(self):
        pass

def main():
    BatallaCartas().jugar()

main()










"""
Reglas del Juego "Batalla de Cartas":
--El juego se juega entre dos jugadores.
--Cada jugador recibe la mitad del mazo (26 cartas) al azar.
--Los jugadores revelan la carta superior de su mazo.
--El jugador con la carta de mayor valor toma ambas cartas y las coloca en el fondo de su mazo.
--Si ambas cartas son del mismo valor, se coloca en un "pozo" y se revela la siguiente carta. 
--El jugador con la carta de mayor valor en la siguiente ronda toma todas las cartas del 
    "pozo" y las coloca en el fondo de su mazo.
--El juego termina cuando uno de los jugadores no tiene más cartas o después de un número 
    determinado de rondas (por ejemplo, 50 rondas). 
--El jugador con más cartas al final gana.
"""
from mazos import MazoPoker


# Crear jugador
mazo = MazoPoker(con_cartas=True)
mazo.barajar()
# carta = mazo.sacar_carta()
# print(carta)
cartas_j1 = []
cartas_j2 = []
pozo = []


class Jugador:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__carta = mazo.sacar_carta()

    def mostrar_carta(self):
        return self.__carta

    def __str__(self) -> str:
        return f"{self.__nombre} ====> {self.__carta}"


class BatallaCartas:

    def __init__(self, jug1: str, jug2: str) -> None:
        self.__jugador1 = Jugador(jug1)
        self.__jugador2 = Jugador(jug2)

    def jugar(self):

        # print(mazo)
        j1 = self.__jugador1.mostrar_carta()
        print(f"carta jugadors 1: {j1}")
        j2 = self.__jugador2.mostrar_carta()
        print(f"carta jugadors 2: {j2}")
        # print(mazo)

        if j1.get_numero() > j2.get_numero():
            cartas_j1.append(j1.get_numero())
            cartas_j1.append(j2.get_numero())
            if len(pozo) > 0:
                p = len(pozo)

                for i in range(p):
                    cartas_j1.append(pozo.pop(0))

            print(f"Jugador 1 {self.__jugador1} Wins!")
        elif j1.get_numero() < j2.get_numero():
            cartas_j2.append(j1.get_numero())
            cartas_j2.append(j2.get_numero())
            if len(pozo) > 0:
                pq = len(pozo)

                for x in range(pq):
                    cartas_j2.append(pozo.pop(0))
            print(f"Jugador 2 {self.__jugador2} Wins!")
        else:
            pozo.append(j1.get_numero())
            pozo.append(j2.get_numero())
            print("Empate")

        # print((cartas_j1))
        # print((cartas_j2))
        # print((pozo))
        if mazo.isvacio() == True:
            a = len(cartas_j1)
            b = len(cartas_j2)
            print("Jugador 1 cantidad de cartas: ==>", a)
            print("jugador 2 cantidad de cartas: ==>", b)
            print()
            if a > b:
                print(f"El Ganador del Juego es: \n\n {self.__jugador1} \n\n 'Felicidades Winner' \n\n")
            elif a < b:
                print(f"El Ganador del Juego es:\n\n {self.__jugador2} \n\n 'Felicidades Winner' \n\n")
            else:
                print("\n\nJUEGO EMPATADO FIN\n\n")


def main():
    cont = 0
    while cont <= 50:
        BatallaCartas("juan", "Saul").jugar()
        cont += 1
        if mazo.isvacio() == True:

            break


main()

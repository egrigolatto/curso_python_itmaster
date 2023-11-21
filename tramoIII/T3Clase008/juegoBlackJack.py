from mazos import MazoBlackJack
from jugadores import Croupier, Cliente, Humano, Compu
from os import system
import utilidades as util

class BlackJack:
    def __init__(self) -> None:
        self.__croupier = Croupier()
        self.__mazo = MazoBlackJack()
        self.__jugadores: list[Cliente] = []
        self.__apuestas: list[int] = []

    @property
    def jugadores(self) -> list[Cliente]:
        return self.__jugadores

    @property
    def mazo(self) -> MazoBlackJack:
        return self.__mazo

    @property
    def croupier(self) -> Croupier:
        return self.__croupier

    @property
    def apuestas(self) -> list[int]:
        return self.__apuestas

    def agregar_jugador(self, cliente: Cliente) -> None:
        self.jugadores.append(cliente)

    def __hay_jugadores_en_la_mesa(self) -> bool:
        return len(self.jugadores) > 0

    def __croupier_reparte_dos_cartas_a_los_jugadores(self) -> None:

        for jug in self.jugadores:
            jug.poner_carta(self.mazo.sacar_carta())
            jug.poner_carta(self.mazo.sacar_carta())

    def __croupier_se_reparte_dos_cartas(self) -> None:
        c = self.mazo.sacar_carta()
        c.darvuelta()
        self.croupier.poner_carta(c)
        self.croupier.poner_carta(self.mazo.sacar_carta())

    def __jugadores_apuestan(self) -> None:
        system('cls')
        print(util.titulo("los jugadores apuestan"))
        print(f"\n{self.croupier}\n")
        for jug in self.jugadores:            
            self.apuestas.append(jug.apuesto())
            

    def __jugadores_juegan(self) -> None:
        system('cls')
        print(util.titulo("los jugadores juegan"))
        for jug in self.jugadores:
            print(f"\n{self.croupier}\n")
            while not jug.me_planto():
                jug.poner_carta(self.mazo.sacar_carta())

    def __croupier_juega(self) -> None:
        c = self.croupier.sacar_carta()
        c.destapar()
        self.croupier.poner_carta(c,0)
        print(f"\n{self.croupier}\n")
        while not self.croupier.me_planto():
            self.croupier.poner_carta(self.mazo.sacar_carta())

    def __croupier_reparte_premios(self) -> None:
        pass

    def __jugadores_se_descartan(self) -> None:
        for jug in self.jugadores:
            while not jug.mano.isvacio():
                self.mazo.poner_carta(jug.sacar_carta())
        while not self.croupier.mano.isvacio():
            self.mazo.poner_carta(self.croupier.sacar_carta())
    
    def __jugadores_se_retiran(self) -> None:
        pass

    def jugar(self) -> None:
        self.mazo.llenar()

        while self.__hay_jugadores_en_la_mesa():
            system('cls')
            print(util.titulo("nueva mano"))
            self.mazo.barajar()
            self.apuestas.clear()            
            self.__croupier_reparte_dos_cartas_a_los_jugadores()
            self.__croupier_se_reparte_dos_cartas()
            self.__jugadores_apuestan()
            self.__jugadores_juegan()
            self.__croupier_juega()
            self.__croupier_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()


def main():
    bj = BlackJack()
    bj.agregar_jugador(Humano("Raulito", 100))
    #bj.agregar_jugador(Humano("Patricia", 100))
    bj.agregar_jugador(Compu("CompuRosa", 100))
    #bj.agregar_jugador(Compu("CompuPablo", 100))
    bj.jugar()


main()

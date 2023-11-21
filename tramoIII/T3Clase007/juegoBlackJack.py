



class BlackJack:
    def __init__(self) -> None:
        self.__croupier = Croupier()
        self.__mazo = MazoBlackJack()
        self.__jugadores = []
        self.__apuestas = []
    
    @property
    def jugadores(self)->list[Cliente]:
        return self.__jugadores

    @property
    def mazo(self)->MazoBlackYack:
        return self.__mazo
    
    def agregar_jugador(self,cliente:Cliente)->None:
        self.jugadores.append(cliente)

    
    def __hay_jugadores_en_la_mesa(self)->bool:
        return len(self.jugadores) > 0
    
    def jugar(self)->None:
        while self.__hay_jugadores_en_la_mesa():


def main():
    bj = BlackJack()
    bj.agregar_jugador(Humano("Raulito",100))
    bj.agregar_jugador(Humano("Patricia",100))
    bj.agregar_jugador(Computadora("CompuRosa",100))
    bj.agregar_jugador(Computadora("CompuPablo",100))
    bj.jugar()


main()
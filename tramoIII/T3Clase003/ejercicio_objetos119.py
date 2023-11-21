"""
Implementar una clase Carta, que se crea a partir de un palo y un valor. 
Las cartas deben poder imprimirse de la forma <valor> de <palo>. 

Las cartas deben poder compararse entre ellas: 

Una carta vale menos que otra si al ser del mismo palo su valor es menor, 
    o si al ser de distintos palos el propio es menor que el palo de la otra carta 
    Implementar una clase Palo, 
    que implementa los métodos __eq__, __lt__ y __str__).
"""


import random


class CartaPoker:
    # ATRIBUTOS DE LA CLASE (CONSTANTES)
    PALOS =   ("#","♥","♦","♣","♠")
    # index     0   1   2   3   4
    NUMEROS = ("#","A","2","3","4","5","6","7","8","9","10","J","Q","K")
    # index     0   1   2   3   4   5   6   7   8   9   10  11  12  13

    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        self.__numero: int = numero
        self.__palo: int = palo
        self.__tapada = tapada

    def get_numero(self) -> int:

        return self.__numero

    def get_palo(self) -> int:
        return self.__palo

    def istapada(self) -> bool:
        return self.__tapada
    
    def tapar(self)->None:
        self.__tapada = True

    def destapar(self)->None:
        self.__tapada = False

    def isroja(self)->bool:
        return self.__palo in (1,2)

    def isnegra(self)->bool:
        return self.__palo in (3,4)

    def __str__(self) -> str:
        if self.istapada():
            cadena = f"[{CartaPoker.NUMEROS[0]}{CartaPoker.PALOS[0]}]"    
        else:
            cadena = f"[{CartaPoker.NUMEROS[self.__numero]}{CartaPoker.PALOS[self.__palo]}]"

        return cadena

class MazoPoker:
    
    CANTIDAD_CARTAS:int = 52 

    def __init__(self) -> None:
        self.__cartas:list[CartaPoker] = []

    def __len__(self)->int:
        return len(self.__cartas)

    def isvacio(self)->bool:
        return len(self) == 0
    
    def islleno(self)->bool:
        return len(self) == MazoPoker.CANTIDAD_CARTAS

    def poner_carta(self,carta:CartaPoker,index:int=None)->None:
        if carta is None or not isinstance(carta,CartaPoker) or self.islleno():
            raise ValueError("Hay un error en el tipo o es None o esta lleno")
        
        if index is None:
            self.__cartas.append(carta)
        else:
            self.__cartas.insert(index,carta)

    def sacar_carta(self,index:int=None)->CartaPoker:
        if  self.isvacio():
            raise ValueError("Error en el indice")
        if index is None:
            index = 0
        return self.__cartas.pop(index)

    def llenar(self)->None:
        for n in range(1,14):
            for p in range(1,5):
                self.poner_carta(CartaPoker(n,p))

    def mezclar(self)->None:
        random.shuffle(self.__cartas)


    def __str__(self) -> str:
        return ''.join(    [str(carta)  for carta in self.__cartas]  )

def main():
    c1 = CartaPoker(2,3)
    print(c1)

    print(len(MazoPoker()))
    m = MazoPoker()
    m.llenar()
    print(m)
    print("\n\n")
    m.mezclar()
    print(m)
    
main()
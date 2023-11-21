

class Gato:

    def __init__(self, nombre='', color='', edad=0) -> None:
        self.__nombre = nombre
        self.__color = color
        self.__edad = edad

    def getnombre(self) -> str:
        return self.__nombre

    def getedad(self) -> int:
        return self.__edad

    def getcolor(self) -> str:
        return self.__color

    def setnombre(self, nombre) -> None:
        self.__nombre = nombre

    def setedad(self, edad) -> None:
        self.__edad = edad

    def setcolor(self, color) -> None:
        self.__color = color

    def __str__(self) -> str:
        return f'{self.__nombre} ({self.__edad}Años) [Color: {self.__color}]'

    def ruido(self)-> str:
        return f"{str(self)} ==> Miauuu"




def main():
    a = int(8)
    print(a)
    print(str(a))

    g1 = Gato()
    print("g1:", g1)
    g1.setnombre('Michi')
    g1.setcolor('Negro')
    g1.setedad(3)
    
    print("g1:", g1)
    print("str(g1):", str(g1))
    print(g1.ruido())
    g2 = Gato("Pepe", "Blanco", 5)
    print('g2:', g2)
    print(g2.ruido())

main()

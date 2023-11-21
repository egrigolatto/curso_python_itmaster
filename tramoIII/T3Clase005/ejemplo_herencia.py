
import math


class Figura(object):
    def __init__(self,nombre) -> None:
        super().__init__()
        self.__nombre = nombre
    
    def get_nombre(self)->str:
        return self.__nombre

    def __str__(self) -> str:
        return f"{self.__nombre} ==> Superficie: {self.superficie()}"

    def superficie(self)->float:
        pass


class Circulo(Figura):
    def __init__(self,radio) -> None:
        super().__init__("Circulo")
        self.__radio = radio

    def __str__(self) -> str:
        return f"{super().__str__()} Radio: {self.__radio}"

    def get_radio(self)->float:
        return self.__radio

    def superficie(self) -> float:
        return math.pi * self.__radio**2

class Triangulo(Figura):
    def __init__(self,base,altura) -> None:
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura

    def __str__(self) -> str:
        return f"{super().__str__()} Base: {self.__base} Altura: {self.__altura}"

    def get_base(self)->float:
        return self.__base
    
    def get_altura(self)->float:
        return self.__altura

    def superficie(self) -> float:
        return self.__base * self.__altura / 2


class Cuadrado(Figura):
    def __init__(self,lado) -> None:
        super().__init__('Cuadrado')
        self.__lado = lado

    def get_lado(self)->float:
        return self.__lado

    def __str__(self) -> str:
        return f"{super().__str__()} Lado: {self.__lado}"

    def superficie(self) -> float:
        return self.__lado**2


def main():
    o = object()
    print(f"o: {o}")
    f1 = Circulo(3)
    print(f"f1: {f1}")
    f2 = Cuadrado(2)
    print(f"f2: {f2}")
    f3 = Triangulo(4,3)
    print(f"f3: {f3}")


main()


"""
Piedra, Papel y Tijeras en Python

Objetivo: Implementar el juego clásico de "Piedra, Papel y Tijeras" utilizando clases 
y objetos en Python.

Requisitos:

El juego consiste en dos jugadores, cada uno selecciona uno de los tres gestos posibles: 
    piedra, papel o tijera.

El juego debe decidir el ganador basado en las reglas clásicas:

Piedra aplasta tijera.
Tijera corta papel.
Papel cubre piedra.

Si ambos jugadores eligen el mismo gesto, es un empate.
El juego se juega en rondas, y el primer jugador que gane dos rondas 
será declarado el ganador final.
Los gestos de los jugadores deben ser seleccionados al azar.

Instrucciones:

Defina una clase Gesto que represente uno de los gestos posibles. 
    Esta clase debe ser capaz de generar un gesto aleatorio y 
    mostrarlo como una cadena de texto.
Defina una clase Jugador que represente a un jugador del juego. 
    Cada jugador tiene un nombre y un gesto actual.
Defina una clase Juego que coordine el juego entre dos jugadores. 
    Debe ser capaz de determinar el ganador de una ronda y seguir la puntuación.

Implemente una función main que inicialice y comience el juego.

Ejecute el programa y observe los resultados de cada ronda hasta que un jugador gane.

Consejos:

Utilice constantes para representar los gestos posibles, esto hará que su código sea más legible.
Descomponga el problema en partes manejables y enfoque su atención en una clase a la vez.
Pruebe cada clase individualmente para asegurarse de que funcione correctamente antes de combinarlas.
"""


import random

class Gesto:
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3

    GESTOS = {PIEDRA:"PIEDRA",PAPEL:"PAPEL",TIJERA:"TIJERA"}
    
    def __init__(self) -> None:
        self.__caracter:int = self.__obtener_gesto_random()
    
    def get_caracter(self)->int:
        return self.__caracter
    
    def __str__(self) -> str:
        return Gesto.GESTOS[self.__caracter]
    
    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value,Gesto):
            return False
        return self.__caracter == __value.__caracter

    def __obtener_gesto_random(self)->int:
        return random.randint(Gesto.PIEDRA,Gesto.TIJERA)






class Jugador:
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.__gesto = Gesto()

    def hacer_gesto(self)->None:
        self.__gesto = Gesto()
    
    def get_nombre(self)->str:
        return self.__nombre

    def get_gesto(self)->Gesto:
        return self.__gesto
    
    def __str__(self) -> str:
        return f"{self.__nombre} ====> {str(self.__gesto)}"

class PiPaTi:

    def __init__(self,nombre_jug1:str,nombre_jug2:str) -> None:
        self.__jugador1 = Jugador(nombre_jug1)
        self.__jugador2 = Jugador(nombre_jug2)
    
    def __quien_gana(self)->Jugador:
        gesto1 = self.__jugador1.get_gesto()
        gesto2 = self.__jugador2.get_gesto()

        if  gesto1 == gesto2:
            return None
        
        if gesto1.get_caracter() == Gesto.PIEDRA and gesto2.get_caracter() == Gesto.TIJERA or \
            gesto1.get_caracter() == Gesto.PAPEL and gesto2.get_caracter() == Gesto.PIEDRA or \
                gesto1.get_caracter() == Gesto.TIJERA and gesto2.get_caracter() == Gesto.PAPEL:
            return self.__jugador1
        
        return self.__jugador2

    def jugar(self)->None:
        terminar = False
        victorias_jugador1 = 0
        victorias_jugador2 = 0
        while not terminar:
            self.__jugador1.hacer_gesto()
            print(self.__jugador1)
            self.__jugador2.hacer_gesto()
            print(self.__jugador2)

            ganador = self.__quien_gana()

            if ganador is self.__jugador1:
                victorias_jugador1 += 1
                print(f"Gana: {ganador.get_nombre()}")
            elif ganador is self.__jugador2:
                victorias_jugador2 += 1
                print(f"Gana: {ganador.get_nombre()}")
            else:
                print("EMPATE")

            if victorias_jugador1 == 2 or victorias_jugador2 == 2:
                terminar = True
        print(f"GANADORRRRRR: {ganador.get_nombre()}")

def main():
    
    PiPaTi("Juan","Pinchame").jugar()
    
    """
    # juego = PiPaTi("Juan","Pinchame")
    # juego.jugar()

    for _ in range(10):
        print(Gesto())


    jug1 = Jugador("Juan Manuel")
    jug2 = Jugador("Juan Manuel")
    print(jug1)
    print(jug2)
    g = jug2.get_gesto()
    if jug1.get_gesto() == g :
        print('iguales')
    else:
        print('distintos')
    
    g = None
    
    if jug1.get_gesto() == g :
        print('iguales')
    else:
        print('distintos')
        g = jug2.get_gesto()
    
    if jug1.get_gesto() == "Pepe" :
        print('iguales')
    else:
        print('distintos')
    """

main()




"""
Implementar la clase Caramelera

Recibe en su constructor la cantidad de caramelos que puede contener.

Tiene el siguiente comportamiento:

c = Caramelera(20)            
c.poner_caramelos(10)        
c.sacar_caramelos(4)         

c.caramelos() ==> 6                
              
print(c)  ==> Caramelera con 6/20 caramelos                       

c.sacar_caramelos(50) ==> ValueError: No quedan tantos caramelos!       

c.poner_caramelos(50) ==> ValueError: No queda lugar para tantos caramelos
"""

class Caramelera:
    def __init__(self,capacidad:int) -> None:
        if not isinstance(capacidad,int) or capacidad < 1:
            raise ValueError("La capacidad de la caramelera no es un entero o es menor a cero")
        self.__capacidad = capacidad
        self.__cantidad_actual = 0

    def poner_caramelos(self,cantidad:int)->None:
        if not isinstance(cantidad,int) or cantidad < 1:
            raise ValueError("No se puede!!")
        if cantidad > (self.__capacidad - self.__cantidad_actual):
            raise ValueError("No queda lugar para tantos caramelos")
        
        self.__cantidad_actual += cantidad

    def sacar_caramelos(self,cantidad:int)->None:
        if not isinstance(cantidad,int) or cantidad < 1:
            raise ValueError("No se puede!!")
        if cantidad > self.__cantidad_actual:
            raise ValueError("No quedan tantos caramelos!")
        
        self.__cantidad_actual -= cantidad

    def __str__(self) -> str:
        return f"Caramelera con {self.__cantidad_actual}/{self.__capacidad} caramelos"

    def caramelos(self)->int:
        return self.__cantidad_actual

def main():

    try:
        c = Caramelera(20)   
        c.poner_caramelos(19)        
        c.sacar_caramelos(1) 
        c.caramelos() # ==> 6      
        print(c)  # ==> Caramelera con 6/20 caramelos                       
        c.sacar_caramelos(5) # ==> ValueError: No quedan tantos caramelos!       
        c.poner_caramelos(5) # ==> ValueError: No queda lugar para tantos caramelos
    except Exception as e:
        print(f"Nos colgamos: {e}")


main()


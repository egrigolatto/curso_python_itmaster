"""
Crea un diccionario en el cual las llaves sean números enteros 
y los valores sean sus cuadrados. 
Haz esto para n numeros.
"""
import random


def crear_tuple_cuadrados_pares(cantidad:int)->tuple:
    return tuple( numero**2 for numero in range(cantidad) if numero%2 == 0 )

def crear_tuple_cuadrados(cantidad:int)->tuple:
    return tuple( numero**2 for numero in range(cantidad) )

def crear_tuple_cubos(cantidad:int)->tuple:
    return tuple( numero**3 for numero in range(cantidad) )

def crear_list_cuadrados(cantidad:int)->list:
    return [ numero**2 for numero in range(cantidad)]

def crear_dic_cuadrados(cantidad:int)->dict:
    return { numero:numero**2 for numero in range(cantidad)}

def main():
    print(crear_dic_cuadrados(20))
    print(crear_list_cuadrados(20))
    print(crear_tuple_cuadrados(20))
    print(crear_tuple_cubos(3))
    print(crear_tuple_cuadrados_pares(20))

main()
"""

Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). 
La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). 
Mostrar al final cómo se llama la persona más joven.
"""
from sys import path
path.append('recursos/')
import funciones as fun
from datos import obtener_nombre_completo
from random import randint


def generar_datos(cantidad:int)->list:
    nombres_edades = []

    for x in range(cantidad):
        nombre = obtener_nombre_completo()    
        edad = randint(1,100)
        nombres_edades.append((nombre,edad))


    return nombres_edades


def mas_joven(nombres, edades):
    menor = float("inf")    
    for index,edad in enumerate(edades):
        if edad < menor:
            menor = edad
            pos_menor = index

    print(f"{nombres[pos_menor]} es el mas joven con {edades[pos_menor]} años")

def orden_nombre(t:tuple)->str:
    return t[0]

def orden_edad(t:tuple)->int:
    return t[1]

def main():
    personas:list[tuple[str,int]] = generar_datos(1000)    
    # personas[('juan',14),  ('rosa',16),(alf,59)]
    #             0     1      0    1    0   1
    #               0           1         2 
    
    personas.sort(key = orden_edad)
    
    #for index,tupla in enumerate(personas):
        #nombre,edad = tupla
        #print(f"{nombre[:30]:30} {edad:4}")
    print(('aaaa',10,7) > ('aaaa',10))

main()

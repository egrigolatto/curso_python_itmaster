"""

Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). 
La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). 
Mostrar al final cómo se llama la persona más joven.
"""
from sys import path
path.append('recursos/')
import funciones as fun



def ingreso_datos():
    nombres = []
    edades = []

    nombre = input("Ingrese Nombre: ")
    while nombre != "*":
        nombres.append(nombre)
        edad = fun.leer_entero(f"Ingrese edad de {nombre}: ",1,100)
        edades.append(edad)
        
        nombre = input("Ingrese Nombre: ")

    return nombres, edades


def mas_joven(nombres, edades):
    menor = float("inf")    
    for index,edad in enumerate(edades):
        if edad < menor:
            menor = edad
            pos_menor = index

    print(f"{nombres[pos_menor]} es el mas joven con {edades[pos_menor]} años")


def main():
    nombres,edades = ingreso_datos()
    print(list(enumerate(nombres)))
    mas_joven(nombres, edades)


main()

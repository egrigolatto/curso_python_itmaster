"""
Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.
"""

from random import randint

def main():
    cont = 0
    suma = 0
    num = randint(0, 10)
    while num != 0:
        cont += 1
        suma += num
        print(num)
        num = randint(0, 10)


    print(f"Cantidad: {cont}, Suma: {suma}, Promedio: {suma/cont}")




main()
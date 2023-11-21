"""
Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.
"""

from random import randint

los_numeros = 'Numeros: '

cantidad = randint(1,15)

print(cantidad)
maximo = -float('inf')
cont = 0
while cont < cantidad:
    numero = randint(1,1000)
    los_numeros += f'{numero} '
    if numero > maximo:
        maximo = numero
        posicion = cont+1
    cont+=1

print(los_numeros)
print(f'Mayor: {maximo} Posicion: {posicion}')
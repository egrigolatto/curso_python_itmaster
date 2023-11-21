"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.

"""

# while, por que no sabemos cuantos numeros vamos a procesar

from random import randint

desde = -10
hasta = 10

numero = randint(desde,hasta)

# metodo del absurdo

maximo = float('-inf') # numero mas pequeño del mundo, infinitamente pequeño
minimo = float('inf')

while numero != 0:
    print(numero)
    if numero > maximo:
        maximo = numero
    if numero < numero:
        minimo = numero
    numero = randint(desde,hasta)

print(f"Maximo: {maximo}")


 # --------------------------------------------------------------------------------------------
# # Inicializar una variable para almacenar el máximo
# maximo = None

# # Leer números enteros hasta que se ingrese un 0
# while True:
#     numero = int(input("Ingrese un número entero (ingrese 0 para detener): "))
    
#     if numero == 0:
#         break  # Salir del bucle si se ingresa 0
    
#     if maximo is None or numero > maximo:
#         maximo = numero

# # Mostrar el máximo
# if maximo is not None:
#     print(f"El número máximo ingresado es: {maximo}")
# else:
#     print("No se ingresaron números.")

'''
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

'''

import random

# Inicializar variables para almacenar la suma y el conteo de números generados
suma = 0
conteo = 0

# Generar números enteros aleatorios hasta que se genere un 0
while True:
    numero = random.randint(0, 10)  # Generar número aleatorio entre 1 y 10
    
    if numero == 0:
        break  # Salir del bucle si se genera un 0
    
    suma += numero
    conteo += 1
    print(numero)

# Calcular el promedio si se generaron números
if conteo > 0:
    promedio = suma / conteo
    print(f"El promedio de los números generados aleatoriamente es: {promedio:.2f}")
else:
    print("No se generaron números.")

"""
Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".
"""

nro1 = int(input("Ingrese numero 1: "))
nro2 = int(input("Ingrese numero 2: "))
nro3 = int(input("Ingrese numero 3: "))

suma = nro1 + nro2 + nro3

print(f"{nro1} + {nro2} + {nro3} = {suma}")
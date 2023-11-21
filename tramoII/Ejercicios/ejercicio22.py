"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

# Ingresar tres números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Determinar el número mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostrar el resultado
print("El número mayor es:", mayor)

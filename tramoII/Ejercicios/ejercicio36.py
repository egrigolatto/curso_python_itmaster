'''
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

'''
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

if operacion == '+':
    resultado = numero1 + numero2
elif operacion == '-':
    resultado = numero1 - numero2
elif operacion == '*':
    resultado = numero1 * numero2
elif operacion == '/':
    if numero2 == 0:
        resultado = 'ERROR'
    else:
        resultado = numero1 / numero2
else:
    resultado = 'Operación inválida'

print(f"Resultado: {resultado}")

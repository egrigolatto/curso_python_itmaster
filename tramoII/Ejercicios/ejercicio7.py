"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:

a. Multiplicado por 10. (utilizar el operador *) a. Dividido por 10. (utilizar el operador /) a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una línea distinta.
"""

numeroEntero = int(input("Ingrese un numero entero: "))

print(f"{numeroEntero}*10 = {numeroEntero*10}\n{numeroEntero}/10 = {numeroEntero/10}\n{numeroEntero}**2 = {numeroEntero**2}")
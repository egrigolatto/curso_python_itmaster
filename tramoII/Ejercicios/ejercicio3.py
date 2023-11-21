"""
Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".
"""


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
anios = int(input("Ingrese un valor en años: "))

print(f"Hola, {nombre}. Dentro de {anios} años tendras {edad + anios} años")
"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese 'F' o 'M' segun su genero: ")

if edad >= 1 and edad <= 120:
    if genero == 'F' or genero == 'f':
        if edad >= 60:
            print(f"{nombre} esta en edad de jubilarse")
        else:
            print(f"{nombre} aun no esta en edad de jubilarse")
    if genero == 'M' or genero == 'm':
        if edad >= 65:
            print(f"{nombre} esta en edad de jubilarse")
        else:
            print(f"{nombre} aun no esta en edad de jubilarse")
else:
    print("Error: la edad debe ser un valor entre 1 y 120")


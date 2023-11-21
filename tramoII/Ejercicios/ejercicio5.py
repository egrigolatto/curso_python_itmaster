"""
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
"""

nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))

promedio = float((nota1 + nota2)/2)


print(f"Notas: {nota1}, {nota2} ==> Promedio: {promedio:4.3}")
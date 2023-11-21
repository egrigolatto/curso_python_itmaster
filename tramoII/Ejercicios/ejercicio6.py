"""
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.
"""

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3= float(input("Ingrese la nota 3: "))

promedio = float((nota1 + nota2 +nota3)/3)

print(f"Notas: {nota1}, {nota2}, {nota3} \nPromedio: {promedio:4.2}")
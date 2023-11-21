"""
Escribir un programa para resolver el siguiente problema:

Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
"""

inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))
inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))
inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

total = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2) 

print(f"Persona 1: {porcentaje_inversion_persona1}\nPersona 2: {porcentaje_inversion_persona2}\nPersona 3: {porcentaje_inversion_persona3}")
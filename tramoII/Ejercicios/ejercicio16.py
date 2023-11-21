"""
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.
"""

segundos = int(input("Ingrese un valor en segundos: "))

dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes

print(f"{segundos} segundos equivale a {dias} dias, {horas} horas, {minutos} minutos y {segundos_restantes} segundos")
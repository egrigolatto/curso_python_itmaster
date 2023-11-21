"""
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
"""

cantidad_invitados = int(input("Ingrese la cantidad de invitados: "))
cantidad_asientos = int(input("Ingrese la cantidad de asientos disponibles: "))

if cantidad_invitados <= cantidad_asientos:
    print("Los asientos alcanzan para todos los invitados.")
else:
    asientos_faltantes = cantidad_invitados - cantidad_asientos
    print("No hay suficientes asientos. Faltan", asientos_faltantes, "asientos para que todos los invitados puedan sentarse.")

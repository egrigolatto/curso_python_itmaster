'''
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.
'''

VIAJE_MINIMO = 50
TARIFA_UNO = 20 #$20/km
TARIFA_DOS = 15 #$15/km

cantidad_km = float(input("Ingrese la cantidad de km recorridos: "))

costo = VIAJE_MINIMO
if cantidad_km <= 10:
    costo = costo + cantidad_km*TARIFA_UNO
if cantidad_km > 10:
    costo = costo + cantidad_km*TARIFA_DOS

print(f'Costo del viaje: ${costo}')
'''
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
'''
costo = float(input("Ingrese el valor a cobrar: "))

if costo < 5500:
    descuento = 4.5/100
    precio_final = costo - costo*descuento
if 5500 < costo < 10000:
    descuento = 8/100
    precio_final = costo - costo*descuento
if costo > 10000:
    descuento= 10.5/100
    precio_final = costo - costo*descuento 

print(f'Costo Neto: ${costo}\nDescuento: {descuento*100}%\nPrecio a paga: ${precio_final}')
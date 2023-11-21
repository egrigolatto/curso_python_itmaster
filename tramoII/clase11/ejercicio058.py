"""
Ejercicio 058

Una empresa aplica el siguiente procedimiento en la 
comercialización de sus productos:

Aplica el precio base a la primera docena de unidades.

Aplica un 10% de descuento a todas las unidades entre 13 y 100.

Aplica un 25% de descuento a todas las unidades por encima de las 100.

Por ejemplo, supongamos que vende 230 unidades de un producto 
cuyo precio base es 100. 

El cálculo resultante sería:

100 * 12 + 90 * 88 + 75 * 130 = 18870, 
y el precio promedio será 18870 / 230 = 82,04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. 

El fin de carga se determina ingresando 0 como cantidad solicitada.

Al finalizar informar:

a) Cantidad de ventas realizadas total.
b) Cantidad de ventas que se aplicaron un 10% de descuento.
c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron       descuentos
"""
import random


def obtener_venta():
    return {'cantidad':random.randint(0,200),'precio':round(random.uniform(1.0,2500.0),2)}

def calcular(venta:dict):
    diez = False
    precio = 0
    if venta['cantidad'] <= 12:
        precio = venta['cantidad']*venta['precio']
    elif venta['cantidad'] <= 100:
        diez = True
        precio = 12*venta['precio'] + (venta['cantidad']-12)*venta['precio']*.9
    else:
        diez = True
        precio = 12*venta['precio'] + \
            (88*venta['precio']*.9) + \
                (venta['cantidad']-100) *.75 *venta['precio']

    precio_promedio = precio/venta['cantidad']
    
    return {'precio':precio,'diez':diez,'precio_prom':precio_promedio}



def main():    
    cant_10 = 0
    cantidad_ventas = 0
    venta = obtener_venta()
    while venta['cantidad'] != 0:
        cantidad_ventas += 1

        
        resultado = calcular(venta)

        print(venta," ",resultado['precio_prom'])

        if resultado['diez'] == True:
            cant_10 += 1
        

        venta = obtener_venta()
    
    # a) Cantidad de ventas realizadas total.
    print(f"Cantidad de ventas: {cantidad_ventas}")
    # b) Cantidad de ventas que se aplicaron un 10% de descuento.
    print(f"Cantidad de ventas que se aplicaron un 10% de descuento {cant_10}")
    # c) Cantidad de ventas que SOLO se aplicó el precio base, no se le 
    print(f'Cantidad de ventas que SOLO se aplicó el precio base: {cantidad_ventas -cant_10}')       
main()





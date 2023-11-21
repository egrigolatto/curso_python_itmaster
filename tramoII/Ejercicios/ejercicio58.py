'''
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada.
Al finalizar informar:
a- Cantidad de ventas realizadas total.
b- Cantidad de ventas que se aplicaron un 10% de descuento.
c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos
'''
def calcular_ventas():
    # Inicializamos las variables para contar las ventas.
    ventas_realizadas = 0
    ventas_con_descuento_10 = 0
    ventas_sin_descuento = 0

    while True:
        cantidad_solicitada = input("Ingrese la cantidad solicitada (-1 para finalizar): ")

        # Verificamos si el usuario desea finalizar la carga.
        if cantidad_solicitada == '-1':
            break

        try:
            cantidad_solicitada = int(cantidad_solicitada)
            precio_base = float(input("Ingrese el precio base del producto: "))

            if cantidad_solicitada <= 0 or precio_base <= 0:
                print("Cantidad o precio base no válidos. Intente nuevamente.")
                continue

            ventas_realizadas += 1

            if cantidad_solicitada <= 12:
                precio_total = cantidad_solicitada * precio_base
                ventas_sin_descuento += 1
            elif 13 <= cantidad_solicitada <= 100:
                precio_total = (12 * precio_base) + ((cantidad_solicitada - 12) * precio_base * 0.9)
                ventas_con_descuento_10 += 1
            else:
                precio_total = (12 * precio_base) + (88 * precio_base * 0.9) + ((cantidad_solicitada - 100) * precio_base * 0.75)

            precio_promedio = precio_total / cantidad_solicitada
            print(f"Valor total de la venta: {precio_total:.2f}")
            print(f"Precio promedio por unidad: {precio_promedio:.2f}")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    print(f"Cantidad de ventas realizadas total: {ventas_realizadas}")
    print(f"Cantidad de ventas con 10% de descuento: {ventas_con_descuento_10}")
    print(f"Cantidad de ventas sin descuento: {ventas_sin_descuento}")

# Llamamos a la función para ejecutar el programa.
calcular_ventas()

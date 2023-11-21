'''
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.

| Forma de Pago    | Total     |
| ---------------- | --------- | 
| Efectivo en Caja | $ xxxx.xx |
| Tarjeta Crédito  | $ xxxx.xx |
| Cheques          | $ xxxx.xx |
| Total de Venta   | $ xxxx.xx |
| Importe del IVA  | $ xxxx.xx |
'''
def calcular_ventas():
    total_efectivo = 0
    total_tarjeta = 0
    total_cheque = 0
    total_venta = 0
    total_iva = 0

    while True:
        forma_pago = input("Ingrese la forma de pago (C/E/T/F para finalizar): ").upper()

        # Verificamos si el usuario desea finalizar el día de ventas.
        if forma_pago == 'F':
            break

        importe_total = float(input("Ingrese el importe total de la venta: "))

        if forma_pago == 'C':
            importe_total *= 1.2  # Cheque, 20% de recargo.
            total_cheque += importe_total
        elif forma_pago == 'E':
            importe_total *= 0.9  # Efectivo, 10% de descuento.
            total_efectivo += importe_total
        elif forma_pago == 'T':
            importe_total *= 1.12  # Tarjeta, 12% de recargo.
            total_tarjeta += importe_total
        else:
            print("Forma de pago no válida. Intente nuevamente.")
            continue

        total_venta += importe_total

    total_iva = total_venta * 0.21  # IVA del 21%.

    # Formato de ticket
    print("\n**************************")
    print("     RESUMEN DE VENTAS    ")
    print("**************************")
    print(f"Efectivo en Caja:      ${total_efectivo:.2f}")
    print(f"Tarjeta de Crédito:    ${total_tarjeta:.2f}")
    print(f"Cheques:               ${total_cheque:.2f}")
    print(f"--------------------------")
    print(f"Total de Venta:        ${total_venta:.2f}")
    print(f"Importe del IVA:       ${total_iva:.2f}")
    print("**************************")

# Llamamos a la función para ejecutar el programa.
calcular_ventas()

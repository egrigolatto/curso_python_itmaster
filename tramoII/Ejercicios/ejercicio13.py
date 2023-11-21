"""
Escribir un programa para calcular el importe a cobrar por un vendedor, considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.

-Pensando los pasos para resolver el problema:
Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.

Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

Mostrar el importe a cobrar por el vendedor.
"""

sueldo_fijo = float(200000)

monto_ventas_realizadas = float(input("Ingrese el total de ventas realizadas: "))

monto_16 = monto_ventas_realizadas*0.16

monto_total = sueldo_fijo + monto_16

print(f"Total a cobrar: ${monto_total}")
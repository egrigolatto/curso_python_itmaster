"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?
"""

salario_base=300000
com_fija_venta=15000

nombre=input("Ingrese Nombre del Vendedor: ")
cant_ventas=int(input("Ingrese cantidad de ventas realizadas: "))
total_ventas=float(input("Ingrese importe total de las ventas del vendedor: $"))

print(f"El Vendedor: {nombre}, le corresponde un salario total de :$ {salario_base+(com_fija_venta*cant_ventas)+(total_ventas*5/100)}")
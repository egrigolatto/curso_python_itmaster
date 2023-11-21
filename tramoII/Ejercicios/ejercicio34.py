'''
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

Jubilación: 11%

Obra Social: 3%

Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
'''

sueldo_basico = float(input("Ingrese el sueldo básico del empleado: "))
antiguedad = int(input("Ingrese la antigüedad en años del empleado: "))
estado_civil = input("Ingrese el estado civil del empleado (s/c): ")

if estado_civil == "s":
    incremento_por_antiguedad = 0.05
elif estado_civil == "c":
    incremento_por_antiguedad = 0.07
else:
    incremento_por_antiguedad = 0.0

incremento_sueldo = sueldo_basico * antiguedad * incremento_por_antiguedad
salario_bruto = sueldo_basico + incremento_sueldo

descuento_jubilacion = salario_bruto * 0.11
descuento_obrasocial = salario_bruto * 0.03
descuento_sindicato = salario_bruto * 0.03

sueldo_neto = salario_bruto - descuento_jubilacion - descuento_obrasocial - descuento_sindicato

print(f"El sueldo neto del empleado es: ${sueldo_neto:.2f}")



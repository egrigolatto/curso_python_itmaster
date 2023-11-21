'''
Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:

Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
Si el empleado posee estudios superiores: aumento del 5%
Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.

Determinar: a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo. b. Sueldo nuevo promedio de la empresa.
'''

def calcular_sueldo_final():
    total_sueldo_final = 0
    total_empleados = 0

    while True:
        numero_empleado = int(input("Ingrese el número de empleado: "))
        sueldo_basico = float(input("Ingrese el sueldo básico: "))
        antiguedad = int(input("Ingrese la antigüedad en años: "))
        cantidad_hijos = int(input("Ingrese la cantidad de hijos: "))
        estudios_superiores = input("¿Tiene estudios superiores? (S/N): ").upper()

        aumento_por_antiguedad = 0
        aumento_por_hijos = 0
        aumento_por_estudios = 0

        if antiguedad > 10:
            aumento_por_antiguedad = sueldo_basico * 0.10

        if cantidad_hijos > 2:
            aumento_por_hijos = sueldo_basico * 0.10
        elif cantidad_hijos == 1:
            aumento_por_hijos = sueldo_basico * 0.05

        if estudios_superiores == 'S':
            aumento_por_estudios = sueldo_basico * 0.05

        sueldo_final = sueldo_basico + aumento_por_antiguedad + aumento_por_hijos + aumento_por_estudios

        print(f"Empleado #{numero_empleado}")
        print(f"Sueldo básico: ${sueldo_basico:.2f}")
        print(f"Nuevo sueldo: ${sueldo_final:.2f}")

        total_sueldo_final += sueldo_final
        total_empleados += 1

        continuar = input("¿Desea ingresar otro empleado? (S/N): ").upper()
        if continuar != 'S':
            break

    if total_empleados > 0:
        sueldo_promedio_empresa = total_sueldo_final / total_empleados
        print(f"Sueldo promedio de la empresa: ${sueldo_promedio_empresa:.2f}")
    else:
        print("No se ingresaron datos de empleados.")

# Llamamos a la función para ejecutar el programa.
calcular_sueldo_final()

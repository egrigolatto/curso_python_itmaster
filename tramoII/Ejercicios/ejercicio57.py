'''
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.

Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:

Cantidad de alumnos que aprobaron (nota >= 4). Cantidad de alumnos que desaprobaron el examen (nota < 4). Porcentaje de alumnos que están aplazados (nota == 1).


'''
def calcular_resultados():
    alumnos_aprobados = 0
    alumnos_desaprobados = 0
    alumnos_aplazados = 0
    total_alumnos = 0

    while True:
        legajo = input("Ingrese el número de legajo del alumno (-1 para finalizar): ")

        # Verificamos si el usuario desea finalizar la carga.
        if legajo == '-1':
            break

        try:
            legajo = int(legajo)
            nota = float(input("Ingrese la nota del examen final (1-10): "))

            # Validamos que la nota esté en el rango válido.
            if 1 <= nota <= 10:
                total_alumnos += 1

                if nota >= 4:
                    alumnos_aprobados += 1
                else:
                    alumnos_desaprobados += 1

                if nota == 1:
                    alumnos_aplazados += 1
            else:
                print("Nota no válida. Debe estar entre 1 y 10. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
            continue  # Volver al inicio del bucle si la entrada no es válida.

    print(f"Cantidad de alumnos aprobados: {alumnos_aprobados}")
    print(f"Cantidad de alumnos desaprobados: {alumnos_desaprobados}")
    if total_alumnos > 0:
        porcentaje_aplazados = (alumnos_aplazados / total_alumnos) * 100
        print(f"Porcentaje de alumnos aplazados: {porcentaje_aplazados:.2f}%")
    else:
        print("No se ingresaron datos.")

# Llamamos a la función para ejecutar el programa.
calcular_resultados()

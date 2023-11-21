'''
Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)
'''
def analizar_edades():
    edades = []
    edades_menores_de_18 = 0
    edades_18_o_mas = 0

    while True:
        edad = input("Ingrese una edad (999 para finalizar): ")

        # Verificamos si el usuario desea finalizar la lectura.
        if edad == '999':
            break

        try:
            edad = int(edad)
            if 0 <= edad <= 100:
                edades.append(edad)
                if edad < 18:
                    edades_menores_de_18 += 1
                else:
                    edades_18_o_mas += 1
            else:
                print("Edad no válida. Debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

    if len(edades) > 0:
        promedio_edad = sum(edades) / len(edades)
        print(f"Personas menores de 18 años: {edades_menores_de_18}")
        print(f"Personas de 18 años o más: {edades_18_o_mas}")
        print(f"Promedio de edad: {promedio_edad:.2f}")
    else:
        print("No se ingresaron edades válidas.")

# Llamamos a la función para ejecutar el programa.
analizar_edades()

'''
Escribir un programa que permita  ingresar la estatura (en metros con decimales) de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.
'''

def calcular_estatura_promedio():
    estaturas = []  # Creamos una lista vacía para almacenar las estaturas.

    while True:
        try:
            estatura = float(input("Ingrese la estatura del jugador en metros (0 para finalizar): "))
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
            continue  # Volver al inicio del bucle si la entrada no es válida.

        # Si el usuario ingresa 0, salimos del bucle.
        if estatura == 0:
            break

        # Agregamos la estatura a la lista de estaturas.
        estaturas.append(estatura)

    if len(estaturas) == 0:
        print("No se ingresaron estaturas.")
    else:
        # Calculamos la estatura promedio sumando todas las estaturas y dividiendo por la cantidad de jugadores.
        estatura_promedio = sum(estaturas) / len(estaturas)
        print(f"La estatura promedio del equipo es: {estatura_promedio:.2f} metros")

# Llamamos a la función para ejecutar el programa.
calcular_estatura_promedio()

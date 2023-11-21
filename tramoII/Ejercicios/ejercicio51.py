'''
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.

La computadora debe mostrar el número máximo y el número mínimo.
'''
def encontrar_maximo_minimo():
    
    numeros = []  # Creamos una lista vacía para almacenar los números.

    while True:
        entrada = input("Ingrese un número (0 para salir): ")

        # Intentamos convertir la entrada del usuario en un número.
        try:
            numero = float(entrada)
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
            continue  # Volver al inicio del bucle si la entrada no es válida.

        # Si el usuario ingresa 0, salimos del bucle.
        if numero == 0:
            break

        # Agregamos el número a la lista de números.
        numeros.append(numero)

    if len(numeros) == 0:
        print("No se ingresaron números.")
    else:
        maximo = max(numeros)  # Encontramos el número máximo en la lista.
        minimo = min(numeros)  # Encontramos el número mínimo en la lista.
        print(f"El número máximo es: {maximo}")
        print(f"El número mínimo es: {minimo}")

# Llamamos a la función para ejecutar el programa.
encontrar_maximo_minimo()


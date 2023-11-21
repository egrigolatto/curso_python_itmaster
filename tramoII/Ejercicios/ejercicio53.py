'''
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
'''

def encontrar_persona_mas_joven():

    personas = []  # Creamos una lista vacía para almacenar las personas.
    print(personas)

    while True:
        nombre = input("Ingrese el nombre de la persona (* para finalizar): ")

        # Si el usuario ingresa '*', salimos del bucle.
        if nombre == '*':
            break

        try:
            edad = int(input("Ingrese la edad de la persona: "))
        except ValueError:
            print("Edad no válida. Intente nuevamente.")
            continue  # Volver al inicio del bucle si la entrada no es válida.

        persona = {"nombre": nombre, "edad": edad}
        personas.append(persona)
        print(personas)

    if len(personas) == 0:
        print("No se ingresaron personas.")
    else:
        # Encontramos la persona más joven utilizando una función lambda como criterio de orden.
        persona_mas_joven = min(personas, key=lambda x: x["edad"])
        print(f"La persona más joven es {persona_mas_joven['nombre']} con {persona_mas_joven['edad']} años.")

# Llamamos a la función para ejecutar el programa.
encontrar_persona_mas_joven()

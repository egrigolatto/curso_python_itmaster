'''
Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.
'''
while True:
    opcion = input("¿Deseas continuar? [S/N]: ").lower()
    
    if opcion == 's':
        print("Continuando...")
        break
    elif opcion == 'n':
        print("Finalizando...")
        break
    else:
        print("Opción inválida. Por favor, ingresa 'S' o 'N'.")

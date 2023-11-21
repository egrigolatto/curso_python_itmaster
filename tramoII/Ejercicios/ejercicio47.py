'''
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
'''

while True:
    nota = float(input("Ingrese la nota del examen (entre 0 y 10): "))
    
    if 0 <= nota <= 10:
        print("Nota válida. ¡Gracias!")
        break
    else:
        print("La nota ingresada no está en el rango válido (entre 0 y 10). Por favor, intente nuevamente.")

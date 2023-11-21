'''
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10.
'''

while True:
    nota = float(input("Ingrese la nota del examen (entre 0 y 10): "))
    
    if 0 <= nota <= 10:
        if nota == 0:
            print("Ausente.")
        elif nota == 1 or nota == 3:
            print("Nota no válida (no se utiliza).")
        else:
            print("Nota válida. ¡Gracias!")
        break
    else:
        print("La nota ingresada no está en el rango válido (entre 0 y 10). Por favor, intente nuevamente.")

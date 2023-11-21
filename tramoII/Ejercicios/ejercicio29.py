"""
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

- Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
- Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
- Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

nombre = input('Ingrese el nombre del alumno: ')
parcial_uno = int(input('Ingrese la nota del primer parcial: '))
parcial_dos = int(input('Ingrse la nota del segundo parcial: '))

condicion_entrada = (parcial_uno >= 0 and parcial_uno <= 10) and (parcial_dos >= 0 and parcial_dos <= 10)

if condicion_entrada :
    print('joya')
    if parcial_uno >= 7 and parcial_dos >=7:
        print(f"Promocionaste {nombre}!! Felicidades!!")
    elif parcial_uno >= 4 and parcial_dos >=4:
        print(f"Aprobaste {nombre}, respando")
    else:
        print(f"Que paso {nombre}, reprobaste burro")

else:
    print("Datos incorrectos, los valores ingresados tienen que estar entre 0 y 10")

    """
    def main():
    try:
        nota_parcial1 = float(input("Ingrese la nota del primer parcial: "))
        nota_parcial2 = float(input("Ingrese la nota del segundo parcial: "))
        
        if 0 <= nota_parcial1 <= 10 and 0 <= nota_parcial2 <= 10:
            if nota_parcial1 >= 7 and nota_parcial2 >= 7:
                resultado = "Promocionó"
            elif nota_parcial1 >= 4 and nota_parcial2 >= 4:
                resultado = "Aprobó"
            else:
                resultado = "Debe recuperar"
            
            print(f"Resultado: {resultado}")
        else:
            print("Error: Las notas deben estar entre 0 y 10.")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()

    """
'''
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.

'''

while True:
    operacion = input("Ingrese la operación a realizar (+, -, *, /, F): ")
    
    if operacion == 'F' or 'f':
        print("Fin del programa.")
        break
    
    if operacion in ('+', '-', '*', '/'):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        else:  # operacion == '/'
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("No se puede dividir por cero.")
                continue  # Regresar al inicio del bucle
        print("El resultado es:", resultado)
    else:
        print("Operación inválida. Intente nuevamente.")

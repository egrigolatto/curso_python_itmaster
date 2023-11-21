"""
Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)
"""

nro1 = int(input('Ingrese el primer valor: '))
nro2 = int(input('Ingrese el segundo valor: '))

if nro1 > nro2:
    mayor = nro1
    menor = nro2
    entero = mayor%menor == 0
    if entero:
        print(f"{mayor} es divisible por {menor}")
    else:
        print(f"{mayor} NO es divisible por {menor}")
else:
    mayor = nro2
    menor = nro1
    entero = mayor%menor == 0
    if entero:
        print(f"{mayor} es divisible por {menor}")
    else:
        print(f"{mayor} NO es divisible por {menor}")


'''
def main():
    try:
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))
        
        if numero1 > numero2:
            mayor = numero1
            menor = numero2
        else:
            mayor = numero2
            menor = numero1
        
        if mayor % menor == 0:
            print(f"{mayor} es divisible por {menor}")
        else:
            print(f"{mayor} no es divisible por {menor}")
    except ValueError:
        print("Error: Ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()

'''
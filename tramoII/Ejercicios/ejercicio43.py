"""
Escibir un programa que lea numeos enteros hasta que la suma de estoss sea mayor que 100, y muestre la cantidad de numeros ingresados
"""
suma = 0
contador_numeros = 0
while suma <= 100:
    print(f"La suma es: {suma}", end='\n\n')
    numero = int(input("Numero: "))
    contador_numeros += 1
    suma += numero

print(f"La cantidad de numeros es: {contador_numeros}")
'''
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176


'''

# Inicializar variables
inicio = 42
fin = 176
suma = 0

# Calcular la suma de los números entre inicio y fin
for numero in range(inicio, fin + 1):
    print(numero)
    suma += numero

# Imprimir la suma
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

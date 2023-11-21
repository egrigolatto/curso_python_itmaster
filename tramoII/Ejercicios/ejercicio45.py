'''
Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

Ejemplo:

4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).
'''

# Leer los números naturales A y B
A = int(input("Ingrese el primer número natural (A): "))
B = int(input("Ingrese el segundo número natural (B): "))

# Inicializar el resultado
resultado = 1

# Calcular A elevado a la B mediante productos sucesivos
for i in range(B):
    resultado *= A

# Imprimir el resultado
print(f"{A}^{B} =", end=" ")
for i in range(B - 1):
    print(A, "*", end=" ")
print(A, "=", resultado)

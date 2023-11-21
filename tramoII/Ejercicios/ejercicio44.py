"""
Escribir un programa que permita leer dos numeros A y B (enteros positivos). Calcular el producto A*B por sumas sucesivas  e imprimir el resultado
Ejemplo:
4*3 = 4 + 4 + 4
3*4 = 3 + 3 + 3 + 3

"""
# Leer los números A y B
A = int(input("Ingrese el primer número (A): "))
B = int(input("Ingrese el segundo número (B): "))

# Inicializar el resultado
resultado = 0

# Calcular el producto A*B por sumas sucesivas
for _ in range(B):
    resultado += A

# Imprimir el resultado
print(f"{A}*{B} =", end=" ")
for _ in range(B - 1):
    print(A, "+", end=" ")
print(A, "=", resultado)

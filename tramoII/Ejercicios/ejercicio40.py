'''
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.

'''
# Solicitar al usuario que ingrese dos números enteros
a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))

# Inicializar variables para la suma de pares y el producto de impares
suma_pares = 0
producto_impares = 1

# Calcular la suma de pares y el producto de impares entre a y b
for numero in range(a, b + 1):
    if numero % 2 == 0:  # Verificar si el número es par
        suma_pares += numero
    else:
        producto_impares *= numero

# Mostrar los resultados
print(f"La suma de los números pares entre {a} y {b} es: {suma_pares}")
print(f"El producto de los números impares entre {a} y {b} es: {producto_impares}")



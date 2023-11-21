
"""
leer uan lista de numeros terminada en 0

lista1: 1,2,3,4,5,6,7,0
lista2: 1,2,3,5,4,0
lista3: 0

mostrar la suma
"""
# Antes (para todos los datos)
suma = 0
contar = 0
numero = int(input("Numero: "))
while numero != 0:
    # Durante (para cada dato)
    suma += numero # suma = suma + numero
    contar += 1
    print(f"Suma dentro {suma}")
    numero = int(input("Numero: "))
# Despues (totales)
print(f"Suma {suma}")
print(f"Cantidad {contar}")
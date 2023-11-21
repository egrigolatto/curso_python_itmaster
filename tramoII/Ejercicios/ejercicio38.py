"""
Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.

Ejemplo:

n = 5  

n x 1 = 5  
n x 2 = 10  
n x 3 = 15  
n x 4 = 20  
n x 5 = 25  
n x 6 = 30  
n x 7 = 35  
n x 8 = 40  
n x 9 = 45  
n x 10 = 50   

"""

# print(range(10))
# print(len(range(10)))
# # algunos objetos son imprimibles y otros no
# print(list(range(10)))
# print(list(range(1,10)))
# print(list(range(1,11)))
# print(list(range(1,10,2))) # de uno a 10 saltando de a dos

# el ultimo elemento es len - 1

import random

la_tabla_del = random.randint(1,10)
print(f"La tabla del: {la_tabla_del} seria")
for numero in range(1,11):
    print(f"{la_tabla_del} x {numero}")

print(f"Numero: {numero}")

for letra in "abcderfg":
    # para cada letra en "abcderfg"
    print(letra)
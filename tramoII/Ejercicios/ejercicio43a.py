suma = 0
cont = 0
terminar = False

while not terminar:
    numero = int(input("Numero: "))
    cont += 1
    suma += numero
    if suma >= 100:
        terminar = True
        
print("Cantidad: ", cont)
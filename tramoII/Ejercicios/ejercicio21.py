"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.


"""
nro1 = int(input("Ingrese el primer valor: "))
nro2 = int(input("Ingrese el segundo valor: "))

if nro1 > nro2:
    print(f"{nro1} es mayor que {nro2}")
if nro1 < nro2:
    print(f"{nro1} es menor que {nro2}")
if nro1 == nro2:
    print("los valores son iguales")
"""
Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.
"""

cad1 = "a"
cad2 = "A"

print(f"{cad1} == {cad2} ==> {cad1 == cad2}")
print(f"{cad1} > {cad2} ==> {cad1 > cad2}")
print(f"{cad1} >= {cad2} ==> {cad1 >= cad2}")
print(f"{cad1} < {cad2} ==> {cad1 < cad2}")
print(f"{cad1} <= {cad2} ==> {cad1 <= cad2}")
print(f"{cad1} != {cad2} ==> {cad1 != cad2}")

print("-.-"*20)

print(f"{cad1+cad2+cad1}")

if cad1 == cad2:
    print("iguales")
else:
    print("distintas")
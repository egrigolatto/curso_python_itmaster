

"""
leer dos numeros y mostrarlos luego hacer un swap y mostrarlos

a = 3
b = 7
3 <---> 7
7 <---> 3
"""

a = 5
b = 10

print(f"{a:5} <----> {b:5}")
auxiliar = a
a = b
b = auxiliar
print(f"{a:5} <----> {b:5}")

a,b = b,a
print(f"{a:5} <----> {b:5}")

a=a+b
b=a-b
a=a-b
print(f"{a:5} <----> {b:5}")













"""
Dados dos numeros mostrar el mayor
"""

a = 10
b = 5
c = 150

print(f"{a} {b} {c} El mayor es: {max(a,b,c)}")

print(f"{a} {b} {c} El mayor es: {min(a,b,c)}")

mayor = a
if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(f"{a} {b} {c} El mayor es: {mayor}")

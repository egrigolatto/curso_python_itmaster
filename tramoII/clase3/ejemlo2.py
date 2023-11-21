"""
dados a,b,c enteros mostrar

mayor
medio
menor
"""

a,b,c = 10,5,17

mayor = a
medio = b
menor = c

if b > mayor:
    mayor = b
    medio = a
    menor = c

if c > mayor:
    mayor = c
    medio = a
    menor = b

if menor > medio:
    medio,menor = menor, medio

print(f"{mayor} > {medio} > {menor}")
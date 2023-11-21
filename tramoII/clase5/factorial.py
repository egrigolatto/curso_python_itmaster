
"""
n! = n*(n-1)!
1! = 1
0! = 1

n * (n-1)!
    (n-1)*(n-2)!
"""
from os import system
system("cls")
fact = 1
numero = 5
for x in range(1,numero+1):
    fact*= x
print(f"{numero}! = {fact} Cantidad de dif. {len(str(fact))}")
system('pause')

 
"""
y = f(x)

resultado = cuadrado(2)

"""

def peps(x):
    return cuadrado(x)

def cuadrado(x):
    c = x*x
    return c


# PROGRAMA PRINCIPAL
def main():
    resultado = cuadrado(2)
    print(f"cuadrado(2) -> {resultado}")
    resultado = cuadrado(3)
    print(f"cuadrado(3) -> {resultado}")    
    pepe = 25
    resultado = cuadrado(pepe)
    print(f"cuadrado({pepe}) -> {resultado}")
    pepe = 10
    print(f"cuadrado({pepe}) -> {cuadrado(pepe)}")

    if peps(2) == cuadrado(2):
        print("iguales")


main() # <== PUNTO DE ENTRADA


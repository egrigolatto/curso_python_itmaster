'''Implementar una clase Carta, que se crea a partir de un palo y un valor.

Las cartas deben poder imprimirse de la forma <valor> de <palo>.

Las cartas deben poder compararse entre ellas.
Una carta vale menos que otra si al ser del mismo palo su valor es menor, o si al ser de distintos palos el propio es menor que el palo de la otra carta
Implementar una clase Palo, que implementa los métodos __eq__, __lt__ y __str__.'''

class Palo:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicializa el nombre del palo.

    def __eq__(self, otro_palo):
        # Sobrecarga del operador de igualdad (==) para comparar palos por nombre.
        return self.nombre == otro_palo.nombre

    def __lt__(self, otro_palo):
        # Sobrecarga del operador menor que (<) para definir un orden entre palos.
        # Se basa en un orden predefinido de palos (Espadas, Bastos, Copas, Oros).
        palos_ordenados = ["Espadas", "Bastos", "Copas", "Oros"]
        return palos_ordenados.index(self.nombre) < palos_ordenados.index(otro_palo.nombre)

    def __str__(self):
        # Sobrecarga del método str para imprimir el nombre del palo.
        return self.nombre

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor  # Inicializa el valor de la carta.
        self.palo = palo    # Inicializa el palo de la carta.

    def __str__(self):
        # Sobrecarga del método str para imprimir la carta en el formato "<valor> de <palo>".
        return f"{self.valor} de {self.palo}"

    def __eq__(self, otra_carta):
        # Sobrecarga del operador de igualdad (==) para comparar cartas por valor y palo.
        return self.valor == otra_carta.valor and self.palo == otra_carta.palo

    def __lt__(self, otra_carta):
        # Sobrecarga del operador menor que (<) para definir un orden entre cartas.
        # Compara primero por palo y, si son diferentes, compara por valor.
        if self.palo == otra_carta.palo:
            return self.valor < otra_carta.valor
        else:
            return self.palo < otra_carta.palo

# Ejemplo de uso:
palo1 = Palo("Espadas")
palo2 = Palo("Copas")
carta1 = Carta("10", palo1)
carta2 = Carta("7", palo1)
carta3 = Carta("8", palo2)

print(carta1)  # Imprime "10 de Espadas"
print(carta2)  # Imprime "7 de Espadas"
print(carta3)  # Imprime "8 de Copas"

print(carta1 == carta2)  # False
print(carta1 < carta2)   # False
print(carta1 < carta3)   # True
print(palo1 < palo2)     # True

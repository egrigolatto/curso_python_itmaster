"""
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.

Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.
"""
from random import randint

# numero = randint(1,20)

numero = int(input('Ingrese un numero entero: '))

esDeUnSoloDigito = numero > -10 and numero < 10
esImpar = numero%2 != 0
estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno = not estaEnAmbos

if estaEnAmbos:
    print(f'{numero} es de un solo digito y es impor')
if noEstaEnNinguno:
    print('No cumple')

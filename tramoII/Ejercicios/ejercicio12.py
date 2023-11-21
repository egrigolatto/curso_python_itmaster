"""
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."
"""

valor1 = float(input("Ingrese el valor del angulo 1: "))
valor2 = float(input("Ingrese el valor del angulo 2: "))

angulo_restante = float(180 - valor1 - valor2)

print(f"Valor angulo restante: {angulo_restante}°")
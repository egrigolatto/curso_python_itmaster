"""
Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.
"""
persona_1 = input("Ingrese su nombre: ")
inversion_persona1 = float(input(f"Hola {persona_1}, ingresa el valor que pensas invertir: "))
persona_2 = input("Ingrese su nombre: ")
inversion_persona2 = float(input(f"Hola {persona_2}, ingresa el valor que pensas invertir: "))
persona_3 = input("Ingrese su nombre: ")
inversion_persona3 = float(input(f"Hola {persona_3}, ingresa el valor que pensas invertir: "))


total = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2) 

print(f"{persona_1} aporto: {porcentaje_inversion_persona1}%\n{persona_2} aporto: {porcentaje_inversion_persona2}%\n{persona_3} aporto: {porcentaje_inversion_persona3}%")
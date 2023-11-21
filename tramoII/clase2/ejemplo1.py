enunciado = """
leer 3 valores y mostrar el promedio
"""
print(enunciado)
nro1 = int(input('Ingrese un numero: '))
nro2 = int(input('Ingrese un numero: '))
nro3 = int(input('Ingrese un numero: '))

promedio = (nro1 + nro2 + nro3) / 3

print("Notas: ",nro1," - ",nro2," - ",nro3,"Promedio:",promedio)
#f"" format string, para dar formato a una cadena, 
cadena_formato = f"Notas {nro1} - {nro2} - {nro3} promedio {promedio:5.2}"
#5:2 --> es para darle formato a la variable, 5 son los espacios que puede ocupar en total la variable, y 2 el espacio que tiene para decimales

print(cadena_formato)
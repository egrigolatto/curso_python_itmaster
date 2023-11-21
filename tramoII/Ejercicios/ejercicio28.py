"""
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

"""

num_mes = int(input("Ingrese un número de mes (1-12): "))

if num_mes >= 1 and num_mes <= 12:
        nombres_meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        nombre_mes = nombres_meses[num_mes - 1]
        print(f"El mes {num_mes} es {nombre_mes}.")
else:
        print("Número de mes inválido.")
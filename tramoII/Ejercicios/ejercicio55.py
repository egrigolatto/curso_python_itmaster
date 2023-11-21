'''
Escribir un programa que permita para cada cliente que va al banco "Express".

Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.
'''

primer_cliente = None
ultimo_cliente = None

while True:
    documento = input("Ingrese el número de documento del cliente (-1 para finalizar): ")

    # Verificamos si el usuario desea finalizar la atención del día.
    if documento == '-1':
        break

    # Verificamos si el número de documento tiene entre 7 y 8 dígitos.
    if len(documento) < 7 or len(documento) > 8:
        print("Número de documento no válido. Debe tener entre 7 y 8 dígitos. Intente nuevamente.")
        continue  # Volver al inicio del bucle si la entrada no es válida.

    # Convertimos el número de documento a un entero para facilitar la comparación.
    try:
        numero_documento = int(documento)
    except ValueError:
        print("Número de documento no válido. Intente nuevamente.")
        continue  # Volver al inicio del bucle si la entrada no es válida.

    # Registramos al primer cliente atendido si aún no se ha registrado.
    if primer_cliente is None:
        primer_cliente = numero_documento

    # Actualizamos el último cliente atendido en cada iteración.
    ultimo_cliente = numero_documento

if primer_cliente is not None and ultimo_cliente is not None:
    print(f"El primer cliente atendido fue el que tiene el número de documento {primer_cliente}.")
    print(f"El último cliente atendido fue el que tiene el número de documento {ultimo_cliente}.")
else:
    print("No se atendió a ningún cliente.")

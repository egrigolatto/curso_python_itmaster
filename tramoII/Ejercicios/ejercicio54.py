'''
Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"


'''
# Definimos las constantes con el nombre de usuario y contraseña correctos.
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "123456"

# Inicializamos el contador de intentos.
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("Acceso concedido.")
        break  # Salimos del bucle si las credenciales son correctas.
    else:
        print("Credenciales incorrectas. Intente nuevamente.")
        intentos += 1

# Si el usuario agotó los 3 intentos sin éxito, mostramos un mensaje de bloqueo de cuenta.
if intentos == 3:
    print("Se ha bloqueado la cuenta.")

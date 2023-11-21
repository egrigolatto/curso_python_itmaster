cadena = "La casa grande"

print(f"'{cadena}' tiene {len(cadena)} caracteres")

contador = 0
for letra in cadena: # para cada letra en la cadena
    if letra == 'a':
        contador += 1
print(f"La cantidad de letras a es {contador}")

contador = 0
index = 0
while index < len(cadena):
    letra = cadena[index]
    if letra == 'a':
        contador += 1
    index += 1

print(f"La cantidad de letras a es {contador}")


from random import randint
fecha = 19630101 # AAAAMMDD

# tambien lo podemos convertir en un string que iterarlo, porque es un numero 


# AAAA <== |MMDD ( la division entera me va a dar lo que esta a la izquierda de donde corto, y lo que quede a la derecha lo voy a reemplazar con ceros, por eso 1000)
anio = fecha//10000
# AAAAMM|==>DD (el % me va a dar lo que esta a la derecha de dond corto y la cantidad de digitos son los ceros que voy a poner)
dia = fecha%100
# AAAA|==> MM <== |DD ()
mes = (fecha//100)%100

print(f"{dia:02}/{mes:02}/{anio:4}")

otra_aaaammdd = (anio*10000) + (mes*100) + dia
print(otra_aaaammdd)

otra_ddmmaaaa = f'{dia:02}{mes:02}{anio}'
print(otra_ddmmaaaa)


anio = randint(2000,2024)
mes = randint(1,12)
if mes in (1, 3, 5, 7, 8, 10, 12):
    dia = randint(1,31)
elif mes in (4,6,9,11):
    dia = randint(1,30)
else:
    if (anio%4) ==0:
        dia = randint(1,29)
    else:
        dia = randint(1,28)

fecha = (anio*10000) + (mes*100) + dia

print(f"{dia:02}/{mes:02}/{anio:04}")

es_fecha = randint(10000000,99999999)
# AAAA <== |MMDD
anio = es_fecha//10000
# AAAAMM|==>DD
dia = es_fecha%100
# AAAA|==> MM <== |DD
mes = (es_fecha//100)%100

print(f"{dia:02}/{mes:02}/{anio:04}")

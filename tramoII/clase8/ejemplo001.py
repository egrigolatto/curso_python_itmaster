from sys import path
import random
path.append('clase7/')

import fechas_int as fi


def es_par(un_numero):
    return un_numero%2 == 0

def transformar_pares(tupla:tuple[tuple[int]],cadena:str) -> tuple[tuple[int|str]]:
    #ANTES
    tupla_salida = ()
    for elemento in tupla:
        tupla_interna = ()
        #ANTES
        for elemento_interno in elemento:
            if es_par(elemento_interno):
                tupla_interna += (cadena,)
            else:
                tupla_interna += (elemento_interno,)
        #DESPUES
        tupla_salida += (tupla_interna,)
    #DESPUES
    return tupla_salida



def main():

    tupla = (
        (1,2,3,4,5,6,7,8,9),
        (1,2,3,4,5,6,7,8,9),
        (1,2,3,4,5,6,7,8,9)
    )

    
    fecha = fi.generar_fecha(2022)
    print(fi.str_fecha(fecha))
    
    print(tupla)
    tupla = transformar_pares(tupla,'pepepeppepe@')
    print(tupla)

main()
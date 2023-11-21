"""
Este módulo contiene funciones para el manejo de enterosa como fechas.

Funciones:

- el_anio(fecha) : Retorna el año de la fecha. 
- el_mes(fecha) : Retorna el mes de la fecha. 
- el_dia(fecha) : Retorna el día de la fecha. 

"""
from random import randint


def el_anio(fecha):
    """
    Retorna el año de la fecha.

    Args:
        fecha (int): Un entero con la forma AAAAMMDD.

    Returns:
        int con el año de la fecha.
    """
    return fecha//10000

# AAAAMM|==>DD


def el_dia(fecha):
    return fecha % 100

# AAAA|==> MM <== |DD


def el_mes(fecha):
    return (fecha//100) % 100


def str_fecha(fecha):
    return f"{el_dia(fecha):02}/{el_mes(fecha):02}/{el_anio(fecha):4}"


def el_nombre_del_mes(mes):
    nombre_del_mes = ("enero", "febrero", "marzo", "abril", "mayo",
                      "junio", "julio", "agosto", "septiembre", "octubre",
                      "noviembre", "diciembre")
    return nombre_del_mes[mes-1]


def str_fecha_larga(fecha):
    return f"{el_dia(fecha):02} de {el_nombre_del_mes(el_mes(fecha))} de {el_anio(fecha):4}"


def obtener_cant_dias_mes(mes, anio):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dia = 31
    elif mes in (4, 6, 9, 11):
        dia = 30
    else:
        if(anio % 4) == 0:
            dia = 29
        else:
            dia = 28
    return dia


def fecha_mas_dias(fecha, cantidad_dias):
    dia = el_dia(fecha)
    mes = el_mes(fecha)
    anio = el_anio(fecha)

    while cantidad_dias > 0:
        cantidad_dias -= 1
        dia += 1
        if dia > obtener_cant_dias_mes(mes, anio):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

    return crear_fecha(dia, mes, anio)


def crear_fecha(dia, mes, anio):
    return (anio*10000) + (mes*100) + dia


def fecha_menos_dias(fecha, cantidad_dias):
    dia = el_dia(fecha)
    mes = el_mes(fecha)
    anio = el_anio(fecha)
    while cantidad_dias > 0:
        cantidad_dias -= 1
        dia -= 1
        if dia == 0:
            dia = obtener_cant_dias_mes(mes, anio)
            mes -= 1
            if mes == 1:
                mes = 12
                anio -= 1
    return crear_fecha(dia, mes, anio)


def generar_fecha(anio):
    mes = randint(1, 12)
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dia = randint(1, 31)
    elif mes in (4, 6, 9, 11):
        dia = randint(1, 30)
    else:
        if (anio % 4) == 0:
            dia = randint(1, 29)
        else:
            dia = randint(1, 28)

    return (anio*10000) + (mes*100) + dia


def test():
    print(f"{'-'*80}\nMódulo de fechas (Como números enteros)\n{'-'*80}")
    f = generar_fecha(2023)
    print(str_fecha_larga(f))
    for x in range(1,33):
        print(str_fecha(fecha_menos_dias(f,x)))

if __name__ == '__main__':
    test()

import sys
# Agregar al path la ruta donde se encuentran los modulos
sys.path.append("recursos/") 


from fechas_int import *


def main():
    fecha = 19180101
    print(str_fecha_larga(fecha))
    for cant_dias in range(1,366):
        print(str_fecha_larga(fecha_mas_dias(fecha,cant_dias)))

    print(str_fecha_larga(fecha_mas_dias(10000101,300000)))




main()


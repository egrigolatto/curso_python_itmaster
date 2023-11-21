"""
Este Módulo implementa funciones de uso general.

- es_entero(str_numero) 
- es_flotante(str_numero) 
- es_entero_entre(str_numero) 
- es_flotante_entre(str_numero) 

"""

def es_entero(str_numero:str) -> bool:
    try:  # INTENTO        
        int(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_flotante(str_numero:str)->bool:
    try:  # INTENTO
        float(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_numero(str_numero:str)->bool:
    return es_entero(str_numero) or es_flotante(str_numero)


def leer_numero(cartel:str="Ingrese un numero: ") -> int | float:    
    while True: 
        cadena = input(cartel)
        if es_entero(cadena):
            return int(cadena)
        elif es_flotante(cadena):            
            return float(cadena)
        else:
            print("Error: Tiene que ingresar un numero.")


def leer_entero(cartel:str="Ingrese un entero: ", desde:int=-999999999999999, hasta:int=999999999999999)->int:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero entero.")
    return numero


def leer_flotante(cartel:str="Ingrese un float: ", desde:float=-float('inf'), hasta:float=float('inf'))->float:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_flotante(cadena):
            numero = float(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero float.")
    return numero

def sumar(*datos)->int:
    suma = 0
    for elemento in datos:
        if isinstance(elemento,(float,int)):
            suma+=elemento
    return suma

def test_funciones():    
    numero = leer_entero("Dia: ",1,31)
    
    numero = leer_entero(hasta=31)
    numero = leer_entero(hasta=31,cartel="Numero: ",desde=10)
    numero = leer_entero(desde=-100,hasta=100)
    
    print(sumar(1,5,7,8,9,"8"))
    
    

if __name__ == '__main__':
    test_funciones()

'''Se pide implementar una clase CalendarioMes con los siguientes métodos:

__init__(): toma como parámetro un entero que representa el número de días del mes (entre 28 y 31). Debe lanar una excepción si no es un día válido.

agregar_evento(): toma como parámetro un día (número entero) y el nombre de un evento (cadena) y lo almacena en el calendario. Debe lanar una excepción si no es un día válido.

eliminar_evento(): toma como parámetro un día y el nombre de un evento y lo elimina del calendario.

Debe lanzar una excepción si no existe un evento con ese nombre.

obtener_eventos_dia(): toma como parámetro un día y devuelve una lista con los eventos programados para ese día, o la lista vacía si no hay eventos en ese día. Debe lanar una excepción si no es un día válido.'''

class CalendarioMes:
    def __init__(self, num_dias):
        if num_dias < 28 or num_dias > 31:
            raise ValueError("Número de días no válido. Debe estar entre 28 y 31.")
        self.num_dias = num_dias
        self.eventos = {dia: [] for dia in range(1, num_dias + 1)}

    def agregar_evento(self, dia, nombre_evento):
        if not 1 <= dia <= self.num_dias:
            raise ValueError("Día no válido.")
        self.eventos[dia].append(nombre_evento)

    def eliminar_evento(self, dia, nombre_evento):
        if not 1 <= dia <= self.num_dias:
            raise ValueError("Día no válido.")
        if nombre_evento not in self.eventos[dia]:
            raise ValueError(f"No existe un evento con el nombre '{nombre_evento}'.")
        self.eventos[dia].remove(nombre_evento)

    def obtener_eventos_dia(self, dia):
        if not 1 <= dia <= self.num_dias:
            raise ValueError("Día no válido.")
        return self.eventos[dia]

# Ejemplo de uso:
calendario = CalendarioMes(30)

calendario.agregar_evento(5, "Reunión")
calendario.agregar_evento(15, "Conferencia")
calendario.agregar_evento(5, "Entrenamiento")

print(calendario.obtener_eventos_dia(5))  # ['Reunión', 'Entrenamiento']
print(calendario.obtener_eventos_dia(15))  # ['Conferencia']

calendario.eliminar_evento(5, "Reunión")

print(calendario.obtener_eventos_dia(5))  # ['Entrenamiento']

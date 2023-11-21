'''Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponden al nombre del equipo local y el visitante (en ese orden).

Además, tiene los siguientes métodos:

cargar_resultado: Recibe dos números enteros, que corresponden a los goles convertidos por el local y el visitante (en ese orden).

obtener_ganador: Devuelve el nombre del equipo ganador, o None si hubo un empate.

obtener_perdedor: Similar a obtener_ganador, pero devuelve el perdedor o None.

Escribir la clase Liga, que tiene los siguientes métodos:

cargar_partido: Recibe un objeto de clase Partido, y guarda los datos necesarios.

obtener_campeon: Devuelve una cadena con el nombre del equipo que más puntos tiene.

Si hay varios equipos que tengan el puntaje máximo, devolver el nombre de cualquiera ellos.

Se otorgan 3 puntos por partido ganado, 1 por partido empatado y 0 por partido perdido.

Este método debe ser lo más eficiente posible.'''

class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = 0
        self.goles_visitante = 0

    def cargar_resultado(self, goles_local, goles_visitante):
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def obtener_ganador(self):
        if self.goles_local > self.goles_visitante:
            return self.equipo_local
        elif self.goles_visitante > self.goles_local:
            return self.equipo_visitante
        else:
            return None

    def obtener_perdedor(self):
        ganador = self.obtener_ganador()
        if ganador is None:
            return None
        return self.equipo_local if ganador == self.equipo_visitante else self.equipo_visitante

class Liga:
    def __init__(self):
        self.partidos = []
        self.puntos = {}

    def cargar_partido(self, partido):
        self.partidos.append(partido)
        ganador = partido.obtener_ganador()
        perdedor = partido.obtener_perdedor()

        if ganador:
            self.puntos[ganador] = self.puntos.get(ganador, 0) + 3
        else:
            self.puntos[partido.equipo_local] = self.puntos.get(partido.equipo_local, 0) + 1
            self.puntos[partido.equipo_visitante] = self.puntos.get(partido.equipo_visitante, 0) + 1

    def obtener_campeon(self):
        max_puntos = max(self.puntos.values(), default=0)
        campeones = [equipo for equipo, puntos in self.puntos.items() if puntos == max_puntos]
        return campeones[0]  # Devolvemos el primer equipo en caso de empate

# Ejemplo de uso:
partido1 = Partido("Equipo A", "Equipo B")
partido1.cargar_resultado(2, 1)

partido2 = Partido("Equipo C", "Equipo D")
partido2.cargar_resultado(1, 1)

partido3 = Partido("Equipo A", "Equipo C")
partido3.cargar_resultado(1, 0)

liga = Liga()
liga.cargar_partido(partido1)
liga.cargar_partido(partido2)
liga.cargar_partido(partido3)

print(liga.obtener_campeon())  # Imprime "Equipo A"

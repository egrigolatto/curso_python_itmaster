'''Cree una clase Habilidad con un atributo nombre. A continuación, cree una clase Persona que tenga un método aprender_habilidad que tome como argumento un objeto Habilidad y muestre un mensaje indicando que la persona ha aprendido esa habilidad.'''

class Habilidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def aprender_habilidad(self, habilidad):
        print(f"{self.nombre} ha aprendido a {habilidad.nombre}.")

# Ejemplo de uso:
habilidad = Habilidad("cocinar")
persona = Persona("Juan")
persona.aprender_habilidad(habilidad)  # Debería mostrar: "Juan ha aprendido a cocinar."

'''
Defina dos clases, Paciente y Médico. Un paciente puede tener asignado un médico, pero un médico puede tener muchos pacientes.
'''

class Médico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.medico_asignado = None

    def asignar_medico(self, médico):
        self.medico_asignado = médico

# Crear médicos
doctor1 = Médico("Dr. Smith", "Cardiología")
doctor2 = Médico("Dr. Johnson", "Dermatología")

# Crear pacientes
paciente1 = Paciente("Alice", 30)
paciente2 = Paciente("Bob", 45)

# Asignar pacientes a médicos
doctor1.agregar_paciente(paciente1)
doctor2.agregar_paciente(paciente2)

# Asignar médico a paciente
paciente1.asignar_medico(doctor1)
paciente2.asignar_medico(doctor2)

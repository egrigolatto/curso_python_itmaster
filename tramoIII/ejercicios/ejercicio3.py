'''Defina clases Empresa y Empleado. Una empresa tiene varios empleados, pero un empleado trabaja en una sola empresa.'''

class Empresa:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre  # Nombre de la empresa
        self.ubicacion = ubicacion  # Ubicación de la empresa
        self.empleados = []  # Inicialmente, la lista de empleados está vacía

    def contratar_empleado(self, nombre, salario):
        nuevo_empleado = Empleado(nombre, salario, self)
        self.empleados.append(nuevo_empleado)
        return nuevo_empleado

class Empleado:
    def __init__(self, nombre, salario, empresa):
        self.nombre = nombre  # Nombre del empleado
        self.salario = salario  # Salario del empleado
        self.empresa = empresa  # Referencia a la empresa en la que trabaja

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}, Empresa: {self.empresa.nombre}"

# Ejemplo de uso:
empresa1 = Empresa("MiEmpresa", "Ciudad X")  # Creamos una empresa
empleado1 = empresa1.contratar_empleado("Juan", 50000)  # La empresa contrata a un empleado
empleado2 = empresa1.contratar_empleado("María", 55000)  # La empresa contrata a otro empleado

print(f"{empresa1.nombre} tiene los siguientes empleados:")
for empleado in empresa1.empleados:
    print(empleado)

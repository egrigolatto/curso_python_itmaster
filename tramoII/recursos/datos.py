import random

# Constantes con nombres y apellidos
MASCULINOS = [
    "Carlos", "José", "Pedro", "Manuel", "Juan",
    "Miguel", "Alberto", "Francisco", "Diego", "Antonio",
    "Eduardo", "Sergio", "Fernando", "Javier", "Ricardo",
    "Andrés", "Oscar", "Daniel", "Alejandro", "Mario",
    "Gustavo", "Enrique", "Alfredo", "Mauricio", "Martín",
    "Luis", "Raúl", "Gabriel", "Felipe", "Samuel",
    "Vicente", "Cristian", "Hugo", "Adrián", "Ignacio",
    "Arturo", "Pablo", "Rafael", "Salvador", "Julio",
    "Isaac", "Leonardo", "Ángel", "Santiago", "Víctor",
    "Elías", "Gonzalo", "Erik", "Ramón", "Alex"
]

FEMENINOS = [
    "María", "Ana", "Sofía", "Laura", "Carmen",
    "Isabel", "Marta", "Elena", "Patricia", "Sara",
    "Rosa", "Cristina", "Susana", "Lucía", "Paula",
    "Natalia", "Clara", "Beatriz", "Andrea", "Esther",
    "Verónica", "Julieta", "Vanesa", "Marina", "Lorena",
    "Silvia", "Julia", "Cecilia", "Teresa", "Luisa",
    "Rocío", "Yolanda", "Victoria", "Mercedes", "Irene",
    "Leticia", "Raquel", "Adriana", "Mónica", "Sonia",
    "Inés", "Daniela", "Miriam", "Virginia", "Pilar",
    "Gabriela", "Alejandra", "Violeta", "Olga", "Mar"
]

APELLIDOS = [
    "González", "Rodríguez", "Pérez", "Martínez", "García",
    "López", "Hernández", "Sánchez", "Ramírez", "Torres",
    "Flores", "Vásquez", "Castillo", "Ortiz", "Gutiérrez",
    "Mendoza", "Ruiz", "Alvarez", "Cruz", "Espinoza",
    "Reyes", "Morales", "Guzmán", "Vargas", "Medina",
    "Ramos", "Romero", "Suárez", "Navarro", "Jiménez"
]

# Lista de artículos de almacén (Código, Nombre, Precio, Categoría)
ARTICULOS_ALMACEN = [
    ("2001", "Leche", 1.20, "ref"),
    ("2002", "Huevos", 2.50, "ref"),
    ("2003", "Pan", 1.00, "alm"),
    ("2004", "Mermelada", 2.00, "alm"),
    ("2005", "Aceite", 3.50, "alm"),
    ("2006", "Sal", 0.50, "alm"),
    ("2007", "Azúcar", 1.20, "alm"),
    ("2008", "Café", 4.00, "alm"),
    ("2009", "Te", 3.00, "alm"),
    ("2010", "Yogur", 1.00, "ref"),
    ("2011", "Queso", 2.50, "ref"),
    ("2012", "Arroz", 1.00, "alm"),
    ("2013", "Pasta", 1.50, "alm"),
    ("2014", "Jabón", 0.90, "lim"),
    ("2015", "Detergente", 2.00, "lim"),
    ("2016", "Shampoo", 3.50, "per"),
    ("2017", "Desodorante", 2.50, "per"),
    ("2018", "Papel Higiénico", 1.00, "lim"),
    ("2019", "Servilletas", 1.50, "lim"),
    ("2020", "Zumo de Naranja", 2.00, "ref"),    
    ("2101", "Soda", 1.50, "ref"),
    ("2102", "Agua Mineral", 0.80, "ref"),
    ("2103", "Cerveza", 1.50, "ref"),
    ("2104", "Vino", 8.00, "alm"),
    ("2105", "Lata de Atún", 1.20, "alm"),
    ("2106", "Mayonesa", 2.50, "alm"),
    ("2107", "Mostaza", 1.50, "alm"),
    ("2108", "Vinagre", 1.00, "alm"),
    ("2109", "Patatas Fritas", 2.00, "alm"),
    ("2110", "Tortillas de Maíz", 2.00, "alm"),
    ("2111", "Ajo en Polvo", 0.80, "alm"),
    ("2112", "Canela", 0.50, "alm"),
    ("2113", "Champú para Bebés", 4.50, "per"),
    ("2114", "Crema Hidratante", 5.00, "per"),
    ("2115", "Limpiador de Suelos", 3.00, "lim"),
    ("2116", "Blanqueador", 2.50, "lim"),
    ("2117", "Colonia", 10.00, "per"),
    ("2118", "Cepillo de Dientes", 1.00, "per"),
    ("2119", "Pasta de Dientes", 1.50, "per"),
    ("2120", "Enjuague Bucal", 3.00, "per")
    
]

# Lista de artículos de librería (Código, Nombre, Precio)
ATICULOS_LIBRERIA = [
    ("1001", "Cuaderno Espiral", 3.50),
    ("1002", "Lápiz HB", 0.40),
    ("1003", "Borrador", 0.25),
    ("1004", "Regla 30 cm", 1.00),
    ("1005", "Tijeras", 2.00),
    ("1006", "Cinta Adhesiva", 1.50),
    ("1007", "Lapicero Azul", 0.75),
    ("1008", "Lapicero Negro", 0.75),
    ("1009", "Lapicero Rojo", 0.75),
    ("1010", "Marcadores", 4.00),
    ("1011", "Corrector Líquido", 1.80),
    ("1012", "Calculadora", 12.00),
    ("1013", "Papel A4 (Resma)", 5.00),
    ("1014", "Clip", 0.05),
    ("1015", "Saca Grapas", 1.50),
    ("1016", "Grapadora", 6.00),
    ("1017", "Carpeta 3 Anillos", 4.00),
    ("1018", "Compás", 3.50),
    ("1019", "Separadores", 2.00),
    ("1020", "Post-its", 1.50),
    ("1021", "Papelógrafo", 15.00),
    ("1022", "Pegamento en Barra", 0.90),
    ("1023", "Cartulina", 0.50),
    ("1024", "Láminas para Carpeta", 0.10),
    ("1025", "Portaminas", 2.00),
    ("1026", "Repuesto para Portaminas", 1.00),
    ("1027", "Cutter", 2.50),
    ("1028", "Grapas", 0.50),
    ("1029", "Lápices de Colores (Caja)", 5.00),
    ("1030", "Resaltador", 1.20),
    ("1031", "Papel Milimetrado", 1.00),
    ("1032", "Cuaderno Universitario", 5.00),
    ("1033", "Portafolio", 7.00),
    ("1034", "Libreta", 1.50),
    ("1035", "Caja de Archivo", 3.00),
    ("1036", "Bolígrafo Multicolor", 2.50),
    ("1037", "Folder", 0.25),
    ("1038", "Sobres", 0.10),
    ("1039", "Recambio de Bolígrafo", 1.00),
    ("1040", "Cinta Métrica", 2.00),
    ("1041", "Escuadra", 1.50),
    ("1042", "Papel para Acuarela", 2.50),
    ("1043", "Mochila", 25.00),
    ("1044", "Rotuladores", 3.00),
    ("1045", "Plumas", 1.00),
    ("1046", "Pincel", 1.50),
    ("1047", "Témperas", 4.00),
    ("1048", "Cuaderno Dibujo", 4.50),
    ("1049", "Set Geometría", 3.00),
    ("1050", "Calculadora Científica", 20.00)
]

"""
return (2>1) ? 10 : 20
"""

def obtener_nombre_completo(sexo:str='X')->str:
    
    # Elegir la lista de nombres según el sexo
    if sexo == 'X':
        sexo = 'M' if random.randint(0,1) == 0 else 'F'
    
    nombres = MASCULINOS if sexo == 'M' else FEMENINOS
    
    # Obtener un nombre aleatorio
    nombre = random.choice(nombres)
    
    # Probabilidad de tener un nombre compuesto (50%)
    if random.random() < 0.5:
        segundo_nombre = random.choice(nombres)
        # Asegurar que el segundo nombre sea diferente al primero
        while segundo_nombre == nombre:  
            segundo_nombre = random.choice(nombres)
        nombre = f"{nombre} {segundo_nombre}"
    
    # Probabilidad de tener un tercer nombre (5%)
    if " " in nombre and random.random() < 0.05:
        tercer_nombre = random.choice(nombres)
        # Asegurar que el tercer nombre sea diferente
        while tercer_nombre in nombre.split():  
            tercer_nombre = random.choice(nombres)
        nombre = f"{nombre} {tercer_nombre}"
    
    # Obtener un apellido aleatorio
    apellido = random.choice(APELLIDOS)
    
    # Probabilidad de tener un segundo apellido (30%)
    if random.random() < 0.3:
        segundo_apellido = random.choice(APELLIDOS)
        # Asegurar que el segundo apellido sea diferente al primero
        while segundo_apellido == apellido:  
            segundo_apellido = random.choice(APELLIDOS)
        apellido = f"{apellido} {segundo_apellido}"
    
    return f"{nombre} {apellido}"

# Test de la función
if __name__ == '__main__':
    print(obtener_nombre_completo())
    print(obtener_nombre_completo(sexo='F'))
    print(obtener_nombre_completo('M'))

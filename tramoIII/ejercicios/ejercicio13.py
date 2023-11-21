'''Escribir una clase Cuenta que tenga el siguiente comportamiento:

c = Cuenta('Pérez')   
d = Cuenta('López')            
c.acreditar(100, 'Sueldo') 
c.transferir(30, d)      
c.extraer(60, 'Shopping')        
c.saldo() ==> 10
d.saldo() ==> 40 
print(c) Cuenta de Pérez (10)
c.movimientos() ==> [('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
d.movimientos() ==> [('acreditación',30,'Cuenta de Pérez')]
d.extraer(100, 'Deudas') ==> ERROR ValueError: Fondos Insuficientes
'''

class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.movimientos_realizados = []

    def acreditar(self, monto, concepto):
        self.saldo += monto
        self.movimientos_realizados.append(('acreditación', monto, concepto))

    def transferir(self, monto, otra_cuenta):
        if monto <= self.saldo:
            self.saldo -= monto
            otra_cuenta.acreditar(monto, f'Cuenta de {self.titular}')
            self.movimientos_realizados.append(('extracción', monto, f'Cuenta de {otra_cuenta.titular}'))
        else:
            raise ValueError("Fondos Insuficientes")

    def extraer(self, monto, concepto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.movimientos_realizados.append(('extracción', monto, concepto))
        else:
            raise ValueError("Fondos Insuficientes")

    def saldo(self):
        return self.saldo

    def movimientos(self):
        return self.movimientos_realizados

    def __str__(self):
        return f"Cuenta de {self.titular} ({self.saldo})"

# Ejemplo de uso:
c = Cuenta('Pérez')
d = Cuenta('López')

c.acreditar(100, 'Sueldo')
c.transferir(30, d)
c.extraer(60, 'Shopping')

print(c.saldo())  # 10
print(d.saldo())  # 40
print(c)  # Imprime "Cuenta de Pérez (10)"

print(c.movimientos())
# Imprime [('acreditación', 100, 'Sueldo'), ('extracción', 60, 'Shopping'), ('extracción', 30, 'Cuenta de López')]

print(d.movimientos())
# Imprime [('acreditación', 30, 'Cuenta de Pérez')]

try:
    d.extraer(100, 'Deudas')
except ValueError as e:
    print(f"ERROR {e}")

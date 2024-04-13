class OperacionBase:
    def imprimir_valor(self, numero):
        print("Valor actual:", numero)

class SumarDos(OperacionBase):
    def __init__(self, operacion_base):
        self.operacion_base = operacion_base
    
    def imprimir_valor(self, numero):
        self.operacion_base.imprimir_valor(numero)
        print("Después de sumar 2:", numero + 2)

class MultiplicarPorDos(OperacionBase):
    def __init__(self, operacion_base):
        self.operacion_base = operacion_base
    
    def imprimir_valor(self, numero):
        self.operacion_base.imprimir_valor(numero)
        print("Después de multiplicar por 2:", numero * 2)

class DividirPorTres(OperacionBase):
    def __init__(self, operacion_base):
        self.operacion_base = operacion_base
    
    def imprimir_valor(self, numero):
        self.operacion_base.imprimir_valor(numero)
        print("Después de dividir por 3:", numero / 3)

# Crear una instancia de la clase base
operacion = OperacionBase()

# Mostrar el valor inicial
operacion.imprimir_valor(10)

# Aplicar decoradores para realizar las operaciones
operacion = SumarDos(operacion)
operacion = MultiplicarPorDos(operacion)
operacion = DividirPorTres(operacion)

# Mostrar el resultado final
operacion.imprimir_valor(10)

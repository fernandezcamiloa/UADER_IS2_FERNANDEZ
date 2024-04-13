class Componente:
    def mostrar(self):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print(f"  - Pieza: {self.nombre}")

class Conjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)
    
    def mostrar(self):
        print(f"Conjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar()

# Crear piezas individuales
pieza1 = Pieza("Pieza 1")
pieza2 = Pieza("Pieza 2")
pieza3 = Pieza("Pieza 3")
pieza4 = Pieza("Pieza 4")

# Crear sub-conjuntos
subconjunto1 = Conjunto("Sub-conjunto 1")
subconjunto2 = Conjunto("Sub-conjunto 2")
subconjunto3 = Conjunto("Sub-conjunto 3")

# Agregar piezas a los sub-conjuntos
subconjunto1.agregar_componente(pieza1)
subconjunto1.agregar_componente(pieza2)
subconjunto1.agregar_componente(pieza3)
subconjunto1.agregar_componente(pieza4)

subconjunto2.agregar_componente(pieza1)
subconjunto2.agregar_componente(pieza2)
subconjunto2.agregar_componente(pieza3)
subconjunto2.agregar_componente(pieza4)

subconjunto3.agregar_componente(pieza1)
subconjunto3.agregar_componente(pieza2)
subconjunto3.agregar_componente(pieza3)
subconjunto3.agregar_componente(pieza4)

# Crear producto principal
producto_principal = Conjunto("Producto Principal")
producto_principal.agregar_componente(subconjunto1)
producto_principal.agregar_componente(subconjunto2)
producto_principal.agregar_componente(subconjunto3)

# Mostrar el ensamblado completo
producto_principal.mostrar()

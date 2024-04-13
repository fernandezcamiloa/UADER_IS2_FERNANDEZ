class LaminasAcero:
    def __init__(self, espesor, ancho, laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador
    
    def producir_lamina(self):
        self.laminador.producir(self.espesor, self.ancho)

class Laminador:
    def producir(self, espesor, ancho):
        pass

class Laminador5Metros(Laminador):
    def producir(self, espesor, ancho):
        print(f"Lámina de {espesor}\" de espesor y {ancho} metros de ancho producida por el laminador de 5 metros.")

class Laminador10Metros(Laminador):
    def producir(self, espesor, ancho):
        print(f"Lámina de {espesor}\" de espesor y {ancho} metros de ancho producida por el laminador de 10 metros.")

# Ejemplo de uso:
laminador_5m = Laminador5Metros()
laminador_10m = Laminador10Metros()

lamina_5m = LaminasAcero(0.5, 1.5, laminador_5m)
lamina_10m = LaminasAcero(0.5, 1.5, laminador_10m)

lamina_5m.producir_lamina()
lamina_10m.producir_lamina()

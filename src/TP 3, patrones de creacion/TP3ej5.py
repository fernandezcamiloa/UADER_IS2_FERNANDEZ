class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = None
        self.alas = None
        self.tren_aterrizaje = None

    def __str__(self):
        return f"Avión construido con: {self.body}, {self.turbinas}, {self.alas} y {self.tren_aterrizaje}"


class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self, body):
        self.avion.body = body

    def construir_turbinas(self, turbinas):
        self.avion.turbinas = turbinas

    def construir_alas(self, alas):
        self.avion.alas = alas

    def construir_tren_aterrizaje(self, tren_aterrizaje):
        self.avion.tren_aterrizaje = tren_aterrizaje

    def obtener_avion(self):
        return self.avion


# Ejemplo de uso:
builder = AvionBuilder()

# Construir un avión
builder.construir_body("Cuerpo del avión")
builder.construir_turbinas("2 turbinas")
builder.construir_alas("2 alas")
builder.construir_tren_aterrizaje("Tren de aterrizaje")

avion = builder.obtener_avion()
print(avion)

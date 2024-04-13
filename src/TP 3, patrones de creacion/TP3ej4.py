class Factura:
    def __init__(self, importe, tipo_cliente):
        self.importe = importe
        self.tipo_cliente = tipo_cliente

    def calcular_total(self):
        if self.tipo_cliente == "IVA Responsable":
            total = self.importe * 1.21  # 21% de IVA
        elif self.tipo_cliente == "IVA No Inscripto":
            total = self.importe
        elif self.tipo_cliente == "IVA Exento":
            total = self.importe * 1.0  # Sin IVA
        else:
            raise ValueError("Tipo de cliente no válido")

        return total


# Ejemplo de uso:
importe_factura = 1000  # Ejemplo de importe de la factura
tipo_cliente = "IVA Responsable"  # Ejemplo de tipo de cliente

factura = Factura(importe_factura, tipo_cliente)
total_factura = factura.calcular_total()

print(f"Importe total de la factura para un cliente {tipo_cliente}: {total_factura}")

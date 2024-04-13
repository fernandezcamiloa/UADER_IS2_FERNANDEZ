class CalculadoraImpuestos:
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012

        total_impuestos = iva + iibb + contribuciones_municipales
        return total_impuestos

# Ejemplo de uso:
calculadora = CalculadoraImpuestos()
importe_base = 1000  # Ejemplo de importe base imponible
impuestos_totales = calculadora.calcular_impuestos(importe_base)
print("Impuestos totales a pagar:", impuestos_totales)

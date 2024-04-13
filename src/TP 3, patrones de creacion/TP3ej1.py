class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.calcular_factorial(n - 1)


# Ejemplo de uso:
factorial_calculator = FactorialCalculator()

# Calculando el factorial de 5
resultado = factorial_calculator.calcular_factorial(5)
print("Factorial de 5:", resultado)

# Creando otra instancia
otra_instancia = FactorialCalculator()

# Verificando si ambas instancias son la misma
print("¿Ambas instancias son la misma?", factorial_calculator is otra_instancia)

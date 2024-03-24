
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

class Factorial:
    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        for num in range(min_num, max_num + 1):
            print("Factorial de", num, "! es", self.factorial(num))

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        rango = input(
            "Por favor ingrese un rango de números en el formato 'desde-hasta', o '-hasta' para calcular desde 1 hasta el número indicado, o 'desde-' para calcular desde el número indicado hasta 60: "
        )
        if "-" in rango:
            desde, hasta = map(int, rango.split("-"))
        elif "-hasta" in rango:
            desde = 1
            hasta = int(rango.split("-")[0])
        elif "desde-" in rango:
            desde = int(rango.split("-")[0])
            hasta = 60
    else:
        desde, hasta = map(int, sys.argv[1].split("-"))

    factorial_obj = Factorial()
    factorial_obj.run(desde, hasta)

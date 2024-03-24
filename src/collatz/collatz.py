import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def calcular_collatz_para_rango(rango):
    resultados = []
    for n in range(1, rango + 1):
        iteraciones = collatz(n)
        resultados.append((n, iteraciones))
    return resultados

def graficar_collatz(resultados):
    numeros, iteraciones = zip(*resultados)
    plt.scatter(iteraciones, numeros, s=5)
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número inicial (n)')
    plt.title('Conjetura de Collatz para números entre 1 y 10000')
    plt.grid(True)
    plt.show()

# Calcular el número de Collatz para el rango especificado
resultados = calcular_collatz_para_rango(10000)

# Graficar los resultados
graficar_collatz(resultados)

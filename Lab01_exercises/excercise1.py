import time
import matplotlib.pyplot as plt

def measure_time(func, n):
    """Mide el tiempo de ejecución de una función"""
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

def plot_times(n_values, times, title):
    """Grafica los tiempos de ejecución"""
    plt.plot(n_values, times, 'o-', label="Tiempo de ejecución") 
    plt.title(title)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.legend()
    plt.show()

def run_algorithm(algorithm_func, n_values, title):
    """Ejecuta el algoritmo y mide el tiempo de ejecución para diferentes valores de n"""
    times = []
    for n in n_values:
        time_taken = measure_time(algorithm_func, n)
        times.append(time_taken)
        print(f"n = {n}, tiempo = {time_taken:.8f} segundos")

    plot_times(n_values, times, title)


#ALGORITMO 4
def alternative_nested_loops(n):
    """Algoritmo con O(n²) pero con una lógica diferente"""
    lista = list(range(n))
    resultados = []
    for i in range(n):
        for j in range(n):
            resultados.append(lista[i] + lista[j])  
    return resultados

n_values = [10, 50, 100, 200, 500, 800, 1000]

if __name__ == "__main__":
    run_algorithm(alternative_nested_loops, n_values, "Nested Loops - O(n²)")

# 1ER EJERCICIO
import matplotlib.pyplot as plt
data= {10:0.3, 100:0.5, 1000:0.8}

plt.scatter(x=data.keys(), y=data.values(),color = "Red")
plt.title('Loops')
plt.ylabel('Time(s)')
plt.show()

# 2DO EJERCICIO
#Se debe realizar los ejercicios planteados y un grafico del tiempo de procesamiento versus los valores n.
#Calculo de tiempo de ejecicion
#Logartimic complexity - O(log n)
#Total time = O(logn)
#Calcula el tiempo de procesamiento para un condicional con un bucle simple,los valores de n seran : 1,10,100,1000,10000,100000

from timeit import default_timer as timer
def logarithms(n):
    i=1
    while i <= n:
        i= i * 2
        print(i)
        #pass

n=10**3

start= timer()
logarithms(n)
end= timer()
proc_time= end-start
print(f"Tiempo de procesamiento -> {proc_time}")



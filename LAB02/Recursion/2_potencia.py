# 2DO EXCERCISE : Potencia ( "x" a la "n")

def potencia(x, n):
    if n == 0:  # Caso base
        return 1
    return x * potencia(x, n - 1) 

if __name__ == "__main__":
    print(potencia(2, 5))  # 2^5 = 32




















#Otra forma mas PRO para numeros grandes:

def potencia_rapida(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:  # Si es par
        mitad = potencia_rapida(x, n // 2)
        return mitad * mitad
    else:  # Si es impar
        mitad = potencia_rapida(x, (n - 1) // 2)
        return x * mitad * mitad

if __name__ == "__main__":
    print(potencia_rapida(2, 5))  # 2^5 = 32

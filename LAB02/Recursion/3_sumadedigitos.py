# 3ER : Suma de digitos

def suma_digitos(n):
    if n < 10:  
        return n
    return (n % 10) + suma_digitos(n // 10)  

if __name__ == "__main__":
    print(suma_digitos(4321))  

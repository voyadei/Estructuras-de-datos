# 7MO FIBONACCI

def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    if n == 1:  # Caso base 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

if __name__ == "__main__":
    print(fibonacci(6))  # 8
    print(fibonacci(10)) # 55

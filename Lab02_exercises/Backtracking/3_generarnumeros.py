#Generar números con los valores 1, 2 y 3 de N dígitos

def generate_numbers(n, result=""):
    if len(result) == n:
        print(result)  # Imprime la combinación completa
        return
    
    generate_numbers(n, result + "1")  # Agregar '1'
    generate_numbers(n, result + "2")  # Agregar '2'
    generate_numbers(n, result + "3")  # Agregar '3'

if __name__ == "__main__":
    n = 3
    generate_numbers(n)

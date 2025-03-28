#Generar strings de dígitos binarios de longitud N

def generate_binary_strings(n,result= ''):
    #Base inicial
    if len(result) == n: #Len sirve para saber la cantidad de elementos
        print(result)
        return
    
    generate_binary_strings(n,result + '0')
    generate_binary_strings(n,result + '1')

if __name__ == "__main__":
    n= 3 #Numero de bits
    generate_binary_strings(n)
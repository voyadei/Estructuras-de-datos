# 6TO Suma de elementos en una lista

def suma_lista(lista):
    if not lista:  
        return 0
    return lista[0] + suma_lista(lista[1:])  # Tomar el primer elemento y sumar el resto

if __name__ == "__main__":
    print(suma_lista([1, 2, 3, 4, 5]))  
    print(suma_lista([10, 20, 30]))     
    print(suma_lista([-5,6]))            

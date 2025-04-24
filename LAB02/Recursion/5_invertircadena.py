# 5TO: Invertir una cadena

def invertir_cadena(cadena):
    if len(cadena) <= 1:  # Caso base: cadena vacía o de un solo carácter
        return cadena
    return invertir_cadena(cadena[1:]) + cadena[0]  

if __name__ == "__main__":
    print(invertir_cadena("hola"))      
    print(invertir_cadena("Python"))     
    print(invertir_cadena("recursivo"))  

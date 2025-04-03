# 4TO: Verfiicar si una cadena es un palindromo

def es_palindromo(cadena):
    if len(cadena) <= 1:  
        return True
    if cadena[0] != cadena[-1]:  # Si el primer y último carácter son diferentes, no es palíndromo
        return False
    return es_palindromo(cadena[1:-1])  # Llamada recursiva con la subcadena interna

if __name__ == "__main__":
    print(es_palindromo("radar"))  
    print(es_palindromo("oso"))     
    print(es_palindromo("hola"))    
    print(es_palindromo("reconocer")) 





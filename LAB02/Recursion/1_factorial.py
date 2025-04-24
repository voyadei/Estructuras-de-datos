"""
RECURSION AND BACKTRACKING.-

RECURSION: Funcion que se llama a si misma un cierto numero de veces hasta que se cumpla la condicion inicial.
BACKTRAKING: Fuerza bruta,probar con todas las formas posibles.
"""

# Pasos para hacer un commit:
# git add .
# git commit -m "Descripción de los cambios"
# git push origin main


# 1ER EXERCISE : FACTORIAL

def factorial(n): 
    if n== 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__== "__main__":
    print(factorial(4)) 

"""
Lo que ocurre por dentro:

factorial(1) = 1 * 1 = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
"""

# 
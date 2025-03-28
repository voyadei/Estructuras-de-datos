# Combinaciones de strings de T/F de longitud n
"""
                    ' '
                  /      \
                 /        \
               T          F
              /   \       /   \
             /     \     /     \
          TT        TF  FT     FF 

"""

def generate_tf_combinations(n, result=""):
    if len(result) == n:
        print(result)  # Imprime la combinación completa
        return
    
    generate_tf_combinations(n, result + "T")  # Agregar 'T' 
    generate_tf_combinations(n, result + "F")  # Agregar 'F' 

if __name__ == "__main__":
    n = 3  # Longitud de las combinaciones
    generate_tf_combinations(n)

def contar_ocurrencias(lista, objetivo, indice=0):
  
    if indice == len(lista):
        return 0
    
    if lista[indice] == objetivo:
        return 1 + contar_ocurrencias(lista, objetivo, indice + 1)
    
    return contar_ocurrencias(lista, objetivo, indice + 1)

lista_numeros = [1, 2, 3, 4, 2, 5, 2, 6]
objetivo = 2
print(f"El numero {objetivo} aparece {contar_ocurrencias(lista_numeros, objetivo)} veces en la lista.")

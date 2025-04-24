#Que es recursion?

"""
Es un proceso que se define en terminos de si mismo,es una funcion que se 
llama a si misma de manera directa o indirecta.


"""
n_paginas =[50,100,150,70,250]

total=0
for libros in n_paginas:
    total +=libros

    print(total)

print(f"La suma es: {total}")
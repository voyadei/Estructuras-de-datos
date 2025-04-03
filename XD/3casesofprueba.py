class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

        
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    

    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

# Caso 1: Crear un nodo independiente
nodo1 = Node("Primer Nodo")
print(f"Datos del nodo 1: {nodo1.get_data()}")  # Salida esperada: Primer Nodo
print(f"Próximo nodo de nodo1: {nodo1.get_next()}")  # Salida esperada: None

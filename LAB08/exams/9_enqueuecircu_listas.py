""""
🔄 enqueue() en Cola Circular con Listas Enlazadas 🔗
Implementa el método enqueue() para una cola circular basada en listas enlazadas.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        self.size = 0
    
    def enqueue(self, data): #Code
        new_node = Node(data)
        if not self.rear:
            self.rear = new_node
            self.rear.next = self.rear  # Primer nodo apunta a sí mismo
        else:
            new_node.next = self.rear.next  # Enlaza al frente
            self.rear.next = new_node       # Rear apunta al nuevo nodo
            self.rear = new_node            # Rear se actualiza al nuevo nodo
        self.size += 1
        pass
    
    def display(self):
        if not self.rear:
            return []
        
        result = []
        current = self.rear.next  # Comenzar desde el frente
        while True:
            result.append(current.data)
            current = current.next
            if current == self.rear.next:  # Vuelta completa
                break
        return result

# ✅ Test cases
clq = CircularLinkedQueue()
clq.enqueue("A")
print(clq.rear.data == "A") # 🥇 Primer elemento
print(clq.rear.next == clq.rear) # 🔄 Apunta a sí mismo
clq.enqueue("B")
print(clq.display() == ["A", "B"]) # 📊 Cola tiene A y B
clq.enqueue("C")
print(clq.display() == ["A", "B", "C"]) # 📊 Cola tiene A, B y C
print(isinstance(clq.rear, Node)) # 🔍 Tipo nodo
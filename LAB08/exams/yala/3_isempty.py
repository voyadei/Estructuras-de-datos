"""
📊 is_empty() en Cola con Listas Enlazadas 📋
Implementa el método is_empty() para una cola implementada con listas enlazadas.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
    
    def is_empty(self):
        return self.front is None #Code

# ✅ Test cases
q = LinkedQueue()
print(q.is_empty() == True) # ✅ Cola vacía inicial
q.enqueue(1)
print(q.is_empty() == False) # ❌ No está vacía
q.front = None
q.rear = None
print(q.is_empty() == True) # ✅ Vaciada manualmente
q.enqueue("test")
print(q.is_empty() == False) # ❌ Ya no está vacía
print(isinstance(q.is_empty(), bool)) # 🔍 Tipo booleano
"""
👀 peek() en Cola Simple 🔍

Implementa el método peek() para una cola que permita ver el elemento al frente sin eliminarlo.
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def peek(self):
        return self.items[0] if self.items else None #Code
        

# ✅ Test cases
q = Queue()
print(q.peek() == None) # 📭 Cola vacía
q.enqueue("primero")
print(q.peek() == "primero") # 👁️ Ver sin eliminar
q.enqueue("segundo")
print(q.peek() == "primero") # 🥇 Sigue siendo el primero
q.items = []
print(q.peek() == None) # 📭 Cola vacía de nuevo
print(isinstance(q.peek(), str) or q.peek() == None) # 📝 Tipo correcto
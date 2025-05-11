"""
🔁 dequeue() en Cola Simple 🔄
Implementa el método dequeue() para una cola básica que elimine y retorne el elemento al frente.
"""
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None

# ✅ Test cases
q = Queue()
print(q.dequeue() == None) # 📭 Cola vacía
q.enqueue(1)
q.enqueue(2)
print(q.dequeue() == 1) # 🥇 Primer elemento
print(q.dequeue() == 2) # 🥈 Segundo elemento
print(q.dequeue() == None) # 📭 Cola vacía de nuevo
q.enqueue(3)
print(isinstance(q.dequeue(), int)) # 🔢 Tipo correcto

""""
En una sola linea sera
def dequeue(self):
    return self.items.pop(0) if self.items else None
"""
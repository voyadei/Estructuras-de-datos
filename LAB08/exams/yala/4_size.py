"""
🔢 size() en Cola Circular ⭕
Implementa el método size() para una cola circular que retorne la cantidad de elementos.
"""
class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def enqueue(self, item):
        if self.count < self.capacity:
            if self.rear == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.count += 1
            return True
        return False
    
    def size(self):
        return self.count #Code
        

# ✅ Test cases
cq = CircularQueue(3)
print(cq.size() == 0) # 📭 Cola vacía
cq.enqueue("A")
print(cq.size() == 1) # 🥇 Un elemento
cq.enqueue("B")
cq.enqueue("C")
print(cq.size() == 3) # 🧮 Tres elementos
cq.count = 0
print(cq.size() == 0) # 📭 Contador en cero
print(isinstance(cq.size(), int)) # 🔢 Tipo numérico
"""
🔄 dequeue() en Cola Circular Simple ⭕
Implementa el método dequeue() para una cola circular que extraiga elementos del frente.
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
    
    def dequeue(self): #Aqui tu codigo
        if self.count == 0:
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        if self.count == 0:
            self.front = self.rear = -1
        return item
        pass

# ✅ Test cases
cq = CircularQueue(3)
print(cq.dequeue() == None) # 📭 Cola vacía
cq.enqueue("A")
cq.enqueue("B")
print(cq.dequeue() == "A") # 🥇 Primer elemento
print(cq.dequeue() == "B") # 🥈 Segundo elemento
print(cq.dequeue() == None) # 📭 Cola vacía de nuevo
cq.enqueue("C")
print(isinstance(cq.dequeue(), str)) # 📝 Tipo correcto
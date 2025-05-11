"""
⭕ enqueue() en Cola Circular 🔄
Implementa el método enqueue() para una cola circular que añada elementos circulando cuando llega al final.
"""

class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item): #Code
        next_pos = (self.rear + 1) % self.capacity
        if next_pos == self.front:
            return False  # Cola llena
        if self.front == -1:  # Cola vacía
            self.front = self.rear = 0
        else:
            self.rear = next_pos
        self.queue[self.rear] = item
        return True
        pass

# ✅ Test cases
cq = CircularQueue(2)
print(cq.enqueue("A") == True) # ✅ Primer elemento
print(cq.front == 0 and cq.rear == 0) # 🎯 Posiciones correctas
print(cq.enqueue("B") == True) # ✅ Segundo elemento
print(cq.enqueue("C") == False) # ❌ Tercer elemento
print(isinstance(cq.enqueue("X"), bool)) # 🔍 Tipo booleano
"""
📋 add_front() en Cola Doble (Deque) 📝
Implementa el método add_front() para una cola doble (deque) que permita añadir elementos al frente.
"""
class Deque:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item) #Code
    
    def add_rear(self, item):
        self.items.append(item)

# ✅ Test cases
dq = Deque()
dq.add_front(1)
print(dq.items == [1]) # 🥇 Un elemento
dq.add_front(2)
print(dq.items == [2, 1]) # 🔄 Orden correcto
dq.add_rear(3)
print(dq.items == [2, 1, 3]) # 📊 Tres elementos en orden
dq.add_front(4)
print(dq.items == [4, 2, 1, 3]) # 🎯 Insertado al frente
print(isinstance(dq.items, list)) # 📋 Tipo lista


"""
🔄 remove_rear() en Cola Doble (Deque) 📤
Implementa el método remove_rear() para una cola doble que elimine y retorne el elemento al final.
"""
class Deque:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        if not self.items:
            return None
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop() if self.items else None #Code

# ✅ Test cases
dq = Deque()
print(dq.remove_rear() == None) # 📭 Deque vacío
dq.add_rear(1)
print(dq.remove_rear() == 1) # 🥇 Un elemento
dq.add_rear(2)
dq.add_rear(3)
print(dq.remove_rear() == 3) # 🔄 Último elemento
dq.add_front(4)
print(dq.remove_rear() == 2) # 📊 Elemento al final
print(isinstance(dq.remove_rear(), int) or dq.remove_rear() == None) # 📝 Tipo correcto
class Node:
    """Node in a linked list, stores data and reference to the next node."""

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


nodo1= Node(10)
nodo2= Node(20)
nodo3= Node(30)
nodo4=Node(40)

nodo1.set_next(nodo2)
nodo2.set_next(nodo3)
nodo3.set_next(nodo4)

# Empezamos desde el nodo inicial
actual = nodo1

# Recorremos hasta llegar a None
while actual is not None:
    print(actual.get_data())
    actual = actual.get_next()


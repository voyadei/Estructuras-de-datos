"""
insert_left() en Nodo de Árbol 
Implementa el método insert_left() para insertar un nodo como hijo izquierdo en un árbol binario.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value): #Code
        new_node = TreeNode(value)
        if self.left:
            new_node.left = self.left
        self.left = new_node
        return new_node

# ✅ Test cases
root = TreeNode(1)
left = root.insert_left(2)
print(root.left.value == 2) # 🌿 Hijo izquierdo creado
print(left.value == 2) # 🎯 Retorna el nuevo nodo
left_child = left.insert_left(3)
print(root.left.left.value == 3) # 🌳 Estructura correcta
old_left = TreeNode(4)
root.left = old_left
new_left = root.insert_left(5)
print(new_left.left.value == 4) # 🔄 Nodo anterior como hijo
print(isinstance(new_left, TreeNode)) # 🔍 Tipo TreeNode
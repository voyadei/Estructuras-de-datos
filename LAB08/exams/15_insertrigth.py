"""
🌿 insert_right() en Nodo de Árbol 🌲
Implementa el método insert_right() para insertar un nodo como hijo derecho en un árbol binario.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_right(self, value): #Code
        new_node = TreeNode(value)
        if self.right is None:
            self.right = new_node
        else:
            new_node.right = self.right
            self.right = new_node
        return new_node

# ✅ Test cases
root = TreeNode(1)
right = root.insert_right(2)
print(root.right.value == 2) # 🌲 Hijo derecho creado
print(right.value == 2) # 🎯 Retorna el nuevo nodo
right_child = right.insert_right(3)
print(root.right.right.value == 3) # 🌳 Estructura correcta
old_right = TreeNode(4)
root.right = old_right
new_right = root.insert_right(5)
print(new_right.right.value == 4) # 🔄 Nodo anterior como hijo
print(isinstance(new_right, TreeNode)) # 🔍 Tipo TreeNode
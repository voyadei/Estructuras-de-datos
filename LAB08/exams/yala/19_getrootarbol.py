"""
🌲 get_root() en Árbol Binario 🌱

Implementa el método get_root() para obtener el valor de la raíz del árbol binario.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def get_root(self):
        return self.root.value if self.root else None #Code

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.get_root() == None) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.get_root() == 42) # 🌱 Árbol de un solo nodo

# Árbol:      1
#           /   \
#          2     3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
tree = BinaryTree(root)
print(tree.get_root() == 1) # 🌲 Raíz es 1

# Cambiar la raíz
tree.root = TreeNode(10)
print(tree.get_root() == 10) # 🔄 Raíz cambiada

print(isinstance(tree.get_root(), int) or tree.get_root() == None) # 🔢 Tipo correcto
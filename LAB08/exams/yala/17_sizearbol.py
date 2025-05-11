"""
🍂 size() en Árbol Binario 📏
Implementa el método size() que calcule el número total de nodos en un árbol binario.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def size(self, node=None): #Code
        if node is None:
            node = self.root
            if node is None:
                return 0  # Árbol vacío

        left_size = self.size(node.left) if node.left else 0
        right_size = self.size(node.right) if node.right else 0

        return 1 + left_size + right_size

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.size() == 0) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.size() == 1) # 🌱 Árbol de un solo nodo

# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.size() == 6) # 📊 Árbol con 6 nodos

tree.root = TreeNode(10)
tree.root.left = TreeNode(20)
print(tree.size() == 2) # 🎯 Árbol con 2 nodos

print(isinstance(tree.size(), int)) # 🔢 Tipo numérico
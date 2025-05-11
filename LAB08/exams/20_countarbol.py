"""
count_leaves() en Árbol Binario 🍂
Implementa el método count_leaves() para contar el número de nodos hoja (sin hijos) en un árbol binario.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def count_leaves(self, node=None): #Code
        if node is None:
            if self.root is None:
                return 0
            node = self.root
        if node.left is None and node.right is None:
            return 1
        left_leaves = self.count_leaves(node.left) if node.left else 0
        right_leaves = self.count_leaves(node.right) if node.right else 0

        return left_leaves + right_leaves

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.count_leaves() == 0) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(1))
print(single_node_tree.count_leaves() == 1) # 🌱 Un solo nodo es hoja

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
print(tree.count_leaves() == 3) # 🍃 Hojas: 4, 5, 6

balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_tree = BinaryTree(balanced_root)
print(balanced_tree.count_leaves() == 2) # 🍂 Hojas: 2, 3

print(isinstance(tree.count_leaves(), int)) # 🔢 Tipo numérico



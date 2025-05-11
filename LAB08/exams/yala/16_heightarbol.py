"""
📏 height() en Árbol Binario 📐
Implementa el método height() que calcule la altura de un árbol binario (la longitud del camino más largo desde la raíz hasta una hoja).
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def height(self, node=None): #Code
        if node is None:
            node = self.root
            if node is None:
                return -1  

        if node.left is None and node.right is None:
            return 0  

        left_height = self.height(node.left) if node.left else -1
        right_height = self.height(node.right) if node.right else -1

        return 1 + max(left_height, right_height)


# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.height() == -1) # 📭 Árbol vacío
single_node_tree = BinaryTree(TreeNode(1))
print(single_node_tree.height() == 0) # 🌱 Árbol de un solo nodo

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
tree = BinaryTree(root)
print(tree.height() == 2) # 📏 Altura 2

deep_root = TreeNode(1)
deep_root.left = TreeNode(2)
deep_root.left.left = TreeNode(3)
deep_root.left.left.left = TreeNode(4)
deep_tree = BinaryTree(deep_root)
print(deep_tree.height() == 3) # 📐 Altura 3

print(isinstance(deep_tree.height(), int)) # 🔢 Tipo numérico
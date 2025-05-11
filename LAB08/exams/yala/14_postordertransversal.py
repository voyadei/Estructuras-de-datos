"""
postorder_traversal() en Árbol Binario 🌴
Implementa el método postorder_traversal() para realizar un recorrido postorden (izquierda-derecha-raíz) en un árbol binario.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def postorder_traversal(self, node=None, result=None): #Code
        if result is None:
            result = []
        if node is None:
            if self.root is None:
                return result  # Evita recursión infinita si el árbol está vacío
            node = self.root
        if node.left:
            self.postorder_traversal(node.left, result)
        if node.right:
            self.postorder_traversal(node.right, result)
        result.append(node.value)
        return result

# ✅ Test cases
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
print(tree.postorder_traversal() == [4, 5, 2, 6, 3, 1]) # 🔍 Recorrido postorden correcto
single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.postorder_traversal() == [42]) # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
print(empty_tree.postorder_traversal() == []) # 📭 Árbol vacío
tree.root = TreeNode(10)
print(tree.postorder_traversal() == [10]) # 🎯 Otro árbol simple
print(isinstance(tree.postorder_traversal(), list)) # 📋 Tipo lista
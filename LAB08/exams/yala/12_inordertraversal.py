"""
inorder_traversal() en Árbol Binario 🔍
Implementa el método inorder_traversal() para realizar un recorrido inorden (izquierda-raíz-derecha) en un árbol binario.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def inorder_traversal(self, node=None, result=None): #Code
        if result is None:
            result = []
        if node is None:
            if self.root is None:
                return result  # Árbol vacío, retornar lista vacía
            node = self.root
        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.value)
        if node.right:
            self.inorder_traversal(node.right, result)
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
print(tree.inorder_traversal() == [4, 2, 5, 1, 3, 6]) # 🔍 Recorrido inorden correcto
single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.inorder_traversal() == [42]) # 🌱 Árbol de un solo nodo
empty_tree = BinaryTree()
print(empty_tree.inorder_traversal() == []) # 📭 Árbol vacío
tree.root = TreeNode(10)
print(tree.inorder_traversal() == [10]) # 🎯 Otro árbol simple
print(isinstance(tree.inorder_traversal(), list)) # 📋 Tipo lista
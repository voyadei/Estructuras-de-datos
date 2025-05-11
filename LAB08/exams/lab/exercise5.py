from modulo import TreeNode, BinaryTree

def prune_tree(root, target):
    if not root:
        return None

    root.left = prune_tree(root.left, target)
    root.right = prune_tree(root.right, target)

    # Si el nodo actual no es el target y ambos hijos han sido eliminados, podar este nodo también
    if root.value != target and not root.left and not root.right:
        return None

    return root

def print_tree_preorder(node):
    """Helper para imprimir árbol en preorden (solo para debug)."""
    if not node:
        return []
    return [node.value] + print_tree_preorder(node.left) + print_tree_preorder(node.right)

def test_prune_tree():
    print("\nTest Case 1:")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    pruned1 = prune_tree(tree1.root, 1)
    print(print_tree_preorder(pruned1))  # Esperado: [1]

    print("\nTest Case 2:")
    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(1)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.right = TreeNode(1)
    pruned2 = prune_tree(tree2.root, 1)
    print(print_tree_preorder(pruned2))  # Esperado: [1, 2, 1, 3, 1]

    print("\nTest Case 3:")
    tree3 = BinaryTree()
    pruned3 = prune_tree(tree3.root, 7)
    print(print_tree_preorder(pruned3))  # Esperado: []

    print("\nTest Case 4:")
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    pruned4 = prune_tree(tree4.root, 4)
    print(print_tree_preorder(pruned4))  # Esperado: []

    print("\nTest Case 5:")
    tree5 = BinaryTree()
    tree5.root = TreeNode(5)
    tree5.root.left = TreeNode(5)
    tree5.root.right = TreeNode(5)
    pruned5 = prune_tree(tree5.root, 5)
    print(print_tree_preorder(pruned5))  # Esperado: [5, 5, 5]


if __name__ == "__main__":
    test_prune_tree()


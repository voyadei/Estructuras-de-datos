from modulo import TreeNode, BinaryTree

def lowest_common_ancestor(root, p, q):
    """
    Retorna el nodo LCA que contiene a p y q en su subárbol.
    """
    if not root:
        return None

    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root  # Este es el punto donde se separan los caminos hacia p y q

    return left if left else right

def test_lowest_common_ancestor():
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    lca1 = lowest_common_ancestor(tree1.root, 4, 6)
    print("Test Case 1 (LCA of 4 and 6):", lca1.value if lca1 else "Not found")

    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    lca2 = lowest_common_ancestor(tree2.root, 2, 4)
    print("Test Case 2 (LCA of 2 and 4):", lca2.value if lca2 else "Not found")

    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    lca3 = lowest_common_ancestor(tree3.root, 2, 3)
    print("Test Case 3 (LCA of 2 and 3):", lca3.value if lca3 else "Not found")

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    lca4 = lowest_common_ancestor(tree4.root, 1, 3)
    print("Test Case 4 (LCA of 1 and 3):", lca4.value if lca4 else "Not found")

    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3])
    lca5 = lowest_common_ancestor(tree5.root, 8, 3)
    print("Test Case 5 (LCA of 8 and 3):", lca5.value if lca5 else "Not found")  # No existe uno de los nodos

# Ejecutar pruebas
test_lowest_common_ancestor()

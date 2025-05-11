from collections import defaultdict, deque
from modulo import TreeNode, BinaryTree

def vertical_order_traversal(root):
    if not root:
        return []

    col_table = defaultdict(list)  # Mapa: hd → lista de nodos
    queue = deque([(root, 0)])  # (nodo, distancia horizontal)

    while queue:
        node, hd = queue.popleft()
        col_table[hd].append(node.value)

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Ordenar las claves (horizontal distances) de menor a mayor
    return [col_table[x] for x in sorted(col_table)]

def test_vertical_order_traversal():
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    result1 = vertical_order_traversal(tree1.root)
    print("Test Case 1:", result1)  # [[4], [2], [1, 5], [3], [6]]

    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    result2 = vertical_order_traversal(tree2.root)
    print("Test Case 2:", result2)  # [[3], [2], [1]]

    tree3 = BinaryTree()
    result3 = vertical_order_traversal(tree3.root)
    print("Test Case 3:", result3)  # []

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1])
    result4 = vertical_order_traversal(tree4.root)
    print("Test Case 4:", result4)  # [[1]]

    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    result5 = vertical_order_traversal(tree5.root)
    print("Test Case 5:", result5)  # [[4], [2], [1, 5, 6], [3], [7]]

# Ejecutar pruebas
test_vertical_order_traversal()

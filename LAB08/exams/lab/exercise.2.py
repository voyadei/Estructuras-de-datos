from collections import deque
from modulo import TreeNode, BinaryTree

def build_tree_from_list(self, values):
        """Construye un árbol a partir de una lista nivel por nivel (None = nodo nulo)."""
        if not values or values[0] is None:
            self.root = None
            return

        iter_values = iter(values)
        self.root = TreeNode(next(iter_values))
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            try:
                left_val = next(iter_values)
                if left_val is not None:
                    node.left = TreeNode(left_val)
                    queue.append(node.left)

                right_val = next(iter_values)
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    queue.append(node.right)
            except StopIteration:
                break

def serialize(root):
    """Convierte un árbol binario en una cadena usando BFS."""
    if not root:
        return ""

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("#")  # Marcador para nulo

    return ",".join(result)

def deserialize(data):
    """Reconstruye el árbol desde su representación en cadena."""
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue:
        node = queue.popleft()
        if values[i] != "#":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if values[i] != "#":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root
def test_serialize_deserialize():
    def inorder_traversal(root):
        if not root:
            return []
        return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

    trees = [
        ([1, 2, 3, 4, 5, None, 6], "Test Case 1: Normal tree"),
        ([], "Test Case 2: Empty tree"),
        ([42], "Test Case 3: Single node"),
        ([1, 2, None, 3, None, None, None, 4], "Test Case 4: Left-skewed"),
        ([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4], "Test Case 5: Right-skewed")
    ]

    for vals, label in trees:
        tree = BinaryTree()
        tree.build_tree_from_list(vals)
        serialized = serialize(tree.root)
        deserialized_root = deserialize(serialized)
        print(label)
        print("Serialized:", serialized)
        print("Inorder after deserialization:", inorder_traversal(deserialized_root))
        print("---")

# Run tests
test_serialize_deserialize()

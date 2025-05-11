from modulo import TreeNode, BinaryTree

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        """Insert a value into the BST."""
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        if not self.root:
            self.root = TreeNode(value)
        else:
            _insert(self.root, value)
    def inorder(self):
        """Return the inorder traversal as a list."""
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)

def balance_bst(bst):
    """Convert an unbalanced BST into a balanced BST using inorder traversal."""
    def build_balanced_bst(sorted_values):
        if not sorted_values:
            return None
        mid = len(sorted_values) // 2
        node = TreeNode(sorted_values[mid])
        node.left = build_balanced_bst(sorted_values[:mid])
        node.right = build_balanced_bst(sorted_values[mid + 1:])
        return node

    sorted_values = bst.inorder()
    balanced_bst = BinarySearchTree()
    balanced_bst.root = build_balanced_bst(sorted_values)
    return balanced_bst

# Test cases
def test_balance_bst():
    def print_inorder(bst):
        return bst.inorder()

    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)

    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)

    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)

    bst4 = BinarySearchTree()

    bst5 = BinarySearchTree()
    bst5.insert(42)

    balanced1 = balance_bst(bst1)
    balanced2 = balance_bst(bst2)
    balanced3 = balance_bst(bst3)
    balanced4 = balance_bst(bst4)
    balanced5 = balance_bst(bst5)

    print("Test Case 1:", print_inorder(balanced1))
    print("Test Case 2:", print_inorder(balanced2))
    print("Test Case 3:", print_inorder(balanced3))
    print("Test Case 4:", print_inorder(balanced4))
    print("Test Case 5:", print_inorder(balanced5))

# Run tests
test_balance_bst()

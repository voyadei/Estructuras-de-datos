from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

if __name__ == "__main__":
    # Create a binary tree
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print("Level Order Traversal:", level_order_traversal(root))

# Test Case 1: Tree with one node
single_node = TreeNode(42)
assert level_order_traversal(single_node) == [42]

# Test Case 2: Tree with only left children
left_chain = TreeNode(1, TreeNode(2, TreeNode(3)))
assert level_order_traversal(left_chain) == [1, 2, 3]

# Test Case 3: Tree with only right children
right_chain = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
assert level_order_traversal(right_chain) == [1, 2, 3]

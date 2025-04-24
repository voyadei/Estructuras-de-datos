class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def length(self):
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.next)
        return count_nodes(self.head)

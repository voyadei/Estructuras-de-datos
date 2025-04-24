class Node:
    """Represents a node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Deletes the first node with the given key."""
        current = self.head

        # If the node to delete is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # Key not found
            return

        prev.next = current.next
        current = None

    def display(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

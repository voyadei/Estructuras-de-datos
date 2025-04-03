class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def contains(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

# Example usage:
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

target_value = 11
print(f"La lista contiene {target_value}? {llist.contains(target_value)}")

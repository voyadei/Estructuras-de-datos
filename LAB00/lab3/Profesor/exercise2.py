class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""

        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()

        return result + "None"

    def list_length(self):
        """Count and return the number of nodes in the list."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next()

        return count
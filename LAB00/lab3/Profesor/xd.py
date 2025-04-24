class Stack:
    """Stack implementation using a linked list (LIFO data structure)."""
    
    def __init__(self):
        self.linked_list = LinkedList()
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.linked_list.head is None
    
    def push(self, data):
        """Add an element to the top of the stack."""
        self.linked_list.insert_at_beginning(data)
    
    def pop(self):
        """Remove and return the element at the top of the stack."""
        return self.linked_list.delete_from_beginning()
    
    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()
    
    def size(self):
        """Return the number of elements in the stack."""
        return self.linked_list.length
    
    def display(self):
        """Display the elements in the stack."""
        return self.linked_list.display()
    
    
def test_stack():
    stack = Stack()
    print("Created a new stack")
    print(f"Stack: {stack.display()}")
    
    print("\nPushing elements:")
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}, Stack: {stack.display()}")
    
    print(f"\nTop element (peek): {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    
    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Stack: {stack.display()}")

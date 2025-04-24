class QueueWithTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

if __name__ == "__main__":
    q = QueueWithTwoStacks()
    print("Enqueue 1, 2, 3")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Peek:", q.peek())       # Output: 1
    print("Dequeue:", q.dequeue()) # Output: 1
    print("Peek:", q.peek())       # Output: 2
    print("Size:", q.size())       # Output: 2
    print("Is Empty:", q.is_empty()) # Output: False

    q.dequeue()
    q.dequeue()

    print("Is Empty after removing all:", q.is_empty()) # Output: True


# Test Case 1: Enqueue and dequeue single element
q = QueueWithTwoStacks()
q.enqueue(10)
assert q.dequeue() == 10

# Test Case 2: Interleaved operations
q.enqueue(1)
q.enqueue(2)
assert q.peek() == 1
q.enqueue(3)
assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.dequeue() == 3

# Test Case 3: Size and isEmpty check
assert q.is_empty() == True
q.enqueue(7)
q.enqueue(8)
assert q.size() == 2


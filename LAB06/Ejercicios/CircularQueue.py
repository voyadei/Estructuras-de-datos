class CircularQueue:
    """Queue implementation using a circular array."""

    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Queue is full! 💥")

        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"
    

def test_circular_queue():
    """Test the circular queue implementation."""
    queue = CircularQueue(5)
    
    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.is_full() == False, "New queue should not be full"
    
    # Test 2: Basic operations
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.size() == 2, "Queue should have 2 items"
    assert queue.peek() == "A", "Front item should be 'A'"
    
    # Test 3: Circular behavior
    queue.enqueue("C")
    queue.enqueue("D")
    queue.enqueue("E")
    assert queue.is_full() == True, "Queue should be full"
    
    # Test 4: Dequeuing and re-enqueueing (circular behavior)
    assert queue.dequeue() == "A", "Should dequeue 'A'"
    assert queue.dequeue() == "B", "Should dequeue 'B'"
    queue.enqueue("F")
    queue.enqueue("G")
    assert queue.is_full() == True, "Queue should be full again"
    
    # Test 5: Verify FIFO order after wraparound
    assert queue.dequeue() == "C", "Should dequeue 'C'"
    assert queue.dequeue() == "D", "Should dequeue 'D'"
    assert queue.dequeue() == "E", "Should dequeue 'E'"
    assert queue.dequeue() == "F", "Should dequeue 'F'"
    assert queue.dequeue() == "G", "Should dequeue 'G'"
    assert queue.is_empty() == True, "Queue should be empty after all dequeues"
    
    print("All circular queue tests passed! ✅")

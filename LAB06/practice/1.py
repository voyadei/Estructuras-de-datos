class CircularQueue:
    def __init__(self,capacity=5):
    self.capacity=capacity
    self.queue=[None]*capacity
    self.front=-1
    self.rear=-1
    self.size_count=0
    
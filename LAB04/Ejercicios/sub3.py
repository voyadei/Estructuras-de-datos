class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
    









    

s = MinStack()
s.push(3)
s.push(5)
s.push(2)
s.push(1)
s.pop()
print(s.top())
print(s.getMin())

s = MinStack()
s.push(3)
s.push(5)
print(s.getMin())       # Output: 3

s.push(2)
s.push(1)
print(s.getMin())       # Output: 1

s.pop()
print(s.top())          # Output: 2
print(s.getMin())       # Output: 2


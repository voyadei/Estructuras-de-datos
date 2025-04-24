from modulo import LinkedList, Node

class ExtendedLinkedList(LinkedList):
    def remove_nth_from_end(self, n):
        self.found = False

        def recurse(node):
            if node is None:
                return 0, node
            i, node.next = recurse(node.next)
            if i + 1 == n:
                self.found = True
                return i + 1, node.next
            return i + 1, node

        _, self.head = recurse(self.head)
        return (self.found, self.to_list())

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Test
ll = ExtendedLinkedList()
for i in range(1, 6):
    ll.append(i)

print(ll.remove_nth_from_end(2) == (True, [1, 2, 3, 5]))

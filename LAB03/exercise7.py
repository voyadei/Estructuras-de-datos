from modulo import LinkedList,Node
class ExtendedLinkedList(LinkedList):
    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = second = dummy

        for _ in range(n + 1):
            if first is None:
                return  
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        self.head = dummy.next  

    def display(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = ExtendedLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.display()

ll.remove_nth_from_end(4)

print("After Removing 2nd Node from End:")
ll.display()

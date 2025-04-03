from modulo import LinkedList, Node
class ExtendedLinkedList(LinkedList):  
    def remove_middle(self):  
        """Removes the middle node of the linked list."""  
        if self.head is None or self.head.next is None:  
            self.head = None  
            return  

        slow = self.head  
        fast = self.head  
        prev = None  

        # Fast moves twice as fast as slow
        while fast and fast.next:  
            prev = slow  
            slow = slow.next  
            fast = fast.next.next  

        # Remove middle node
        prev.next = slow.next  

    def display(self):   
        current = self.head  
        while current:  
            print(current.data, end=" -> ")  
            current = current.next  
        print("None")  

# Example Usage:
ll = ExtendedLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Lista original:")
ll.display()
ll.remove_middle()
print("Despues de remover el nodo del medio:")
ll.display()

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ? new node
        self.storage = DoublyLinkedList()

    def push(self, value):
        #pass
        # Adds item onto the stack // Add to head
        self.storage.add_to_head(value)
        self.size +=1
    def pop(self):
        #pass
        #removes most recently pushed item from stack // remove from head
        #What happens if nothing is in the stack?
        if self.size == 0:
            return
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return value
    def len(self):
        return self.size

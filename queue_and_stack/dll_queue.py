import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #We do not know how many items will be in the Queue
        # self.storage = ? -- our new node
        self.storage = DoublyLinkedList()
    def enqueue(self, value):
        #Add an item to the back of the queue // adding to the tail
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        #pass
        
        #Check to see if there is something to remove
        if self.size == 0:
            return
        #remove and return an item from the front of the queue// remove from head
        value = self.storage.head.value
        self.storage.remove_from_head()

        self.size -= 1
        return value
    def len(self):
        return self.size

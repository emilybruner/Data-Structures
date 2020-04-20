import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList




class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #adding item to the back of the queue 
        self.size += 1
        self.storage.add_to_head(value)
        

    def dequeue(self):
        #remove and return an item from the front of the queue
            #if size is 0 return none
            if self.size is 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_from_tail()
            

    def len(self):
        return self.size

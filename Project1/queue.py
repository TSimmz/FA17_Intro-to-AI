#***************************************************************************
#***************************************************************************
# Class: Queue
# Function: Implements a queue data structure in Python
#***************************************************************************
#***************************************************************************
class Queue:
    # Queue constructor
    def __init__(self):
        self.items = []
    
    # Checks to see if queue is empty
    def isEmpty(self):
        return self.items == []

    # Adds item to the end of the list
    def enqueue(self, item):
        self.items.insert(0,item)

    # Removes item from front of list
    def dequeue(self):
        return self.items.pop()

    # Returns the size of the queue
    def size(self):
        return len(self.items)

    # Returns the list itself for comparison
    def getList(self):
        return self.items
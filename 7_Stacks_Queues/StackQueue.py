#Stack
class Stack:
    def __int__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def is_empty(self):
        return self.items == []        
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

#queue    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
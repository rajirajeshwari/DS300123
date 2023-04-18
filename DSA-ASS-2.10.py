class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise Exception("Queue is empty")
        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def is_empty(self):
        return not self.stack1 and not self.stack2
    def size(self):
        return len(self.stack1) + len(self.stack2)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  

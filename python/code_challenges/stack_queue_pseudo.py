from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        # To enqueue a value, simply push it onto stack1.
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            # Both stacks are empty, the queue is empty.
            return None

        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2 to reverse the order.
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the element from stack2, which simulates dequeuing from the queue.
        return self.stack2.pop()
    

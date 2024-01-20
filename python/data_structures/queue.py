from data_structures.linked_list import Node

class InvalidOperationError(Exception):
    """Custom exception for invalid operations on the queue."""
    pass



class Queue:
    """
       A Queue implemented using a linked list.

    This Queue class allows you to enqueue elements at the back and dequeue elements
    from the front. It maintains the order of elements in a first-in, first-out (FIFO)
    manner.

    Attributes:
        front: The front of the queue.
        back: The back of the queue (also known as rear).
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """

        self.front = None
        self.back = None  # could be called .rear

    def enqueue(self, value):
        """
        Adds a new node to the end of the queue, with the provided value.
        """
        new_node = Node(value)

        # if the Queue is empty
        if self.back is None:
            self.front = new_node
            self.back = new_node

        # Queue isn't empty
        else:
            self.back.next = new_node
            # point the queue's self.back to our new node. Update the pointer!
            self.back = new_node

    def peek(self):
        """
        Returns the value of the front element of the queue without removing it.
        Returns:
            The value of the front element.
        """
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        return self.front.value

    def dequeue(self):
        """
        Removes the front node from the queue and returns its value.
        """
        # if the Queue is empty
        if self.front is None:
            # TODO: raise an error
            return None

        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next

        # the Queue has become empty
        if self.front is None:
            # also need to update self.back
            self.back = None

        return dequeue_value
    
    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        
        return self.front is None
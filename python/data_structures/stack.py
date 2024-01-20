from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """

        return self.top is None


    def push(self, value):
        """
        Pushes a new value onto the top of the stack.
        """
        # create a new node
        new_node = Node(value)

        # point the new node to the current top
        new_node.next = self.top

        # reassign the self.top in the stack
        self.top = new_node

    def pop(self):
        """
        Pops the top value from the stack and returns it.
        """
        # popping from an empty list
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        

        # get the return value
        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        self.top = self.top.next

        return pop_value
    
    def peek(self):
        """
        look for the first node on top
    
        """
        if self.top is None:

            raise InvalidOperationError("Method not allowed on empty collection")
        
        # get the return value
        peek_value = self.top.value


        self.top = peek_value

        return peek_value
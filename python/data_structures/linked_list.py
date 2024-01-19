class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = None
        self.next = next_

class LinkedList:
    """A LinkedList class with an appropriate string representation."""
    def __init__(self):
        self.head = None

    def insert(self, value):
        
        self.head = Node(value, self.head)

    def __iter__(self):
        """Iterator to allow traversal of the list."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert_before(self, target_value, new_value):
        new_node = Node(new_value)

        if not self.head:
            raise TargetError(f"Target value '{target_value}' not found in the list.")


        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next


        # If the loop completes and the target value is not found
        raise TargetError(f"Target value '{target_value}' not found in the list.")

    def insert_after(self, target_value, new_value):
        new_node = Node(new_value)
    
        if not self.head:
            raise TargetError(f"Target value '{target_value}' not found in the list.")

        current_node = self.head
        while current_node:
            if current_node.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

        # If the loop completes and the target value is not found
        raise TargetError(f"Target value '{target_value}' not found in the list.")

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k should be a non-negative integer.")

        slow_pointer = fast_pointer = self.head

        # Move the fast pointer k nodes ahead
        for _ in range(k):
            if fast_pointer is None:
                raise TargetError(f"The list does not have {k+1} elements.")
            fast_pointer = fast_pointer.next

        # Move both pointers until the fast pointer reaches the end
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        if fast_pointer is None:
            raise TargetError(f"The list does not have {k+1} elements.")

        return slow_pointer.value



    def __str__(self):
        
        elements = ""

        current_node = self.head
        
        while current_node:
            formateed_current_value = f"{{ {current_node.value} }} -> " 
            elements += formateed_current_value
            current_node=current_node.next

        elements += "NULL"

        return elements


class TargetError(BaseException):
    pass

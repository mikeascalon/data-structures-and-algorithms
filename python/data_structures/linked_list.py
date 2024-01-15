class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        
        elements = ""

        current_node = self.head
        
        while current_node:
            formateed_current_value = f"{{ {current_node.value} }} -> " 
            elements += formateed_current_value
            current_node=current_node.next

        elements += "NULL"

        return elements


class TargetError:
    pass

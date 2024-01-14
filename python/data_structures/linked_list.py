class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, position=0):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                raise ValueError("Position out of bounds")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def included(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        if not self.head:
            return "NULL"
        
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return " -> ".join(elements) + " -> None"


class TargetError:
    pass

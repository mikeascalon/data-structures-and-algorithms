from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import Node,KaryTree


def fizz_buzz_tree(kary_tree):
    if kary_tree.root is None:  # Assuming the KaryTree object has a 'root' attribute
        return None

    def fizz_buzz(value):
        if value % 15 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def clone_tree(node):
        if node is None:
            return None
        new_node = Node(fizz_buzz(node.value))
        new_node.children = [clone_tree(child) for child in node.children]
        return new_node

    new_tree = KaryTree()
    new_tree.root = clone_tree(kary_tree.root)
    return new_tree
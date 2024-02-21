from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    hashtable = Hashtable()
    result_set = set()
    
    # Helper function to traverse the first tree and insert its values into the hashtable
    def traverse_and_insert(node):
        if node:
            traverse_and_insert(node.left)
            # Use the value as both the key and the value for simplicity
            hashtable.set(node.value, node.value)
            traverse_and_insert(node.right)
    
    # Helper function to traverse the second tree and check for intersections
    def traverse_and_check(node):
        if node:
            traverse_and_check(node.left)
            if hashtable.has(node.value):
                result_set.add(node.value)
            traverse_and_check(node.right)
    
    traverse_and_insert(tree1.root)
    traverse_and_check(tree2.root)
    
    return result_set
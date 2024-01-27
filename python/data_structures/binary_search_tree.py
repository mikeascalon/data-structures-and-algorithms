from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
       A binary search tree (BST) is a binary tree data structure where each node has at most two children,
    referred to as the left child and the right child. In a BST, for each node:
    
    - All nodes in its left subtree have values less than the node's value.
    - All nodes in its right subtree have values greater than the node's value.

    This class extends BinaryTree to provide methods for adding elements to the BST and checking for
    the presence of elements in the BST.
    """

    def add(self,value):

        """
        Add a new node with the given 'value' to the binary search tree (BST).

        Args:
            value: The value to be added to the BST.
        """
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        def walk(node,node_to_add):

            if node is None:
                return

            if node_to_add.value < node.value:
                if node.left is None:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            elif node_to_add.value > node.value:
                if node.right is None:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)

        walk(self.root, new_node) 

    def contains(self, value):

        """
        Check if the BST contains a node with the given 'value'.

        Args:
            value: The value to be checked for in the BST.

        Returns:
            bool: True if a node with the given value is found in the BST, False otherwise.
        """

        def search (node, target_value):
            if node is None:
                return False

            if target_value == node.value:
                return True
            elif target_value < node.value:
                return search(node.left, target_value)
            else:
                return search(node.right, target_value)
        return search(self.root, value)    
            
        
            

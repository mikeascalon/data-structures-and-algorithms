class BinaryTree:
    """
      Binary Tree is a hierarchical data structure where each node has at most two children,
    referred to as the left child and the right child.

    This class provides methods for traversing the binary tree using three different orders:
    - Pre-order: Root, Left, Right
    - In-order: Left, Root, Right
    - Post-order: Left, Right, Root
    """

    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def pre_order(self):

        """
        Perform a pre-order traversal of the binary tree.
        Task is 
        return root result  + left node result + right node result
        """
    
        def walk(node):
            if node is None:
                return []

            my_result = [node.value]    
            left_result = walk(node.left)
            right_result = walk(node.right)
            return my_result + left_result + right_result
        

        return walk(self.root)
    

    def in_order(self):

        """
         Perform an in-order traversal of the binary tree.
        Task is 
        return left result  + root  result + right node result
        """
    
        def walk(node):
            if node is None:
                return []

            left_result = walk(node.left)
            my_result = [node.value]    
            right_result = walk(node.right)
            return  left_result + my_result  + right_result
        

        return walk(self.root)
    
    def post_order(self):

        """
        Task is 
        return left result   + right node result + root  result
        """
    
        def walk(node):
            if node is None:
                return []

            left_result = walk(node.left)
            right_result = walk(node.right)
            my_result = [node.value]    
            return  left_result + right_result+ my_result
        

        return walk(self.root)

    def find_maximum_value(self):
        """
        Find the maximum value in the binary tree.
        """
        def find_max(node):
            if node is None:
                return float('-inf')  # Initialize with negative infinity

            left_max = find_max(node.left)
            right_max = find_max(node.right)
            return max(node.value, left_max, right_max)

        if self.root is None:
            return None  # Handle the case when the tree is empty
        else:
            return find_max(self.root)

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

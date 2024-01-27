class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        
        self.root = None

    def pre_order(self):

        """
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



class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

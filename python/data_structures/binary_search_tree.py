from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self,value):
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
            
        
            

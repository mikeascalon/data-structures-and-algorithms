from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    if not tree.root:
        return []
    

    queue = []  # Queue for breadth-first traversal
    values = []  # List to store node values
    queue.append(tree.root)

    while queue:
        current = queue.pop(0)  # Dequeue the first node in the queue

        # Add the value of current node to the values list
        values.append(current.value)

        # Enqueue child nodes of the current node
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values
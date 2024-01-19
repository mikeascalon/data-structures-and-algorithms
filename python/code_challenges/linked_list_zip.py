from data_structures.linked_list import LinkedList, Node

def zip_lists(list_a, list_b):
    current_a = list_a.head
    current_b = list_b.head

    # Create a new LinkedList for the result
    zipped_list = LinkedList()
    tail = None

    while current_a or current_b:
        if current_a:
            if not tail:
                zipped_list.head = Node(current_a.value)
                tail = zipped_list.head
            else:
                tail.next = Node(current_a.value)
                tail = tail.next
            current_a = current_a.next

        if current_b:
            if not tail:
                zipped_list.head = Node(current_b.value)
                tail = zipped_list.head
            else:
                tail.next = Node(current_b.value)
                tail = tail.next
            current_b = current_b.next

    return zipped_list
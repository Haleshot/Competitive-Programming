class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertNode(head, position, value):
    new_node = Node(value)
    if position == 1:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    current = head
    count = 1

    while count < position - 1 and current.next:
        current = current.next
        count += 1

    new_node.next = current.next
    if current.next:
        current.next.prev = new_node

    current.next = new_node
    new_node.prev = current

    return head

def deleteNode(head, position):
    if not head:
        return None

    if position == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    current = head
    count = 1

    while count < position and current.next:
        current = current.next
        count += 1

    prev_node = current.prev
    prev_node.next = current.next

    if current.next:
        current.next.prev = prev_node

    return head

    
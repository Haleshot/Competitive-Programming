class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head:
        return None

    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    k = k % length

    if k == 0:
        return head

    current = head
    for _ in range(length - k - 1):
        current = current.next

    new_head = current.next
    current.next = None
    current = new_head
    while current.next:
        current = current.next
    current.next = head

    return new_head

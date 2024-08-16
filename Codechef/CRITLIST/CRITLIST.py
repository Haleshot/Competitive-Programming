def solve(head):
    count = 0
    if head.next is None:
        return 0
    current = head.next
    old_val = head.val
    while not current.next is None:
        if (old_val < current.val and current.next.val < current.val) or (
            old_val > current.val and current.next.val > current.val
        ):
            count += 1
        old_val = current.val
        current = current.next
    return count

def getMiddleElement(head):
    count = 0
    current = head
    while current:
        current = current.next
        count += 1 
    count = count // 2
    current = head
    while count > 0:
        current = current.next
        count -= 1 
    return current.data
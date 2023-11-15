"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def reverseSegment(head, L, R):
    if L==R:
        return head
    dummy = Node(0)
    
    dummy.next = head
    prev = dummy
    i = 1 
    while i<L:
        prev=prev.next
        i+=1 
    cur = prev.next
    nx = cur.next
    while(i<R):
        tmp = nx.next
        nx.next=cur
        cur=nx
        nx = tmp
        i+=1 
    prev.next.next=nx 
    prev.next=cur
    return dummy.next
    

    
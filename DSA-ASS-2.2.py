class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_groups(head: Node, k: int) -> Node:
    prev = None
    curr = head
    nxt = None
    count = 0
    
    # Reverse first k nodes of the linked list
    while curr is not None and count < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count += 1
    
    # Recursively call for the rest of the list
    if nxt is not None:
        head.next = reverse_groups(nxt, k)
    
    # Return new head of the reversed list
    return prev
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
k = 3
new_head = reverse_groups(head, k)
while new_head is not None:
    print(new_head.val, end=' -> ')
    new_head = new_head.next


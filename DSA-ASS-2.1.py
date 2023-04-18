class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_zero_sum(head):
    dummy = Node(0)
    dummy.next = head
    sums = {0: dummy}
    total = 0
    
    while head:
        total += head.val
        sums[total] = head
        head = head.next
    
    total = 0
    head = dummy
    while head:
        total += head.val
        head.next = sums[total].next
        head = head.next
    
    return dummy.next

head = Node(2)
head.next = Node(-3)
head.next.next = Node(1)
head.next.next.next = Node(4)
head.next.next.next.next = Node(-1)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(-2)

current = head
while current:
    print(current.val, end=' -> ')
    current = current.next
print('None')

head = delete_zero_sum(head)

current = head
while current:
    print(current.val, end=' -> ')
    current = current.next
print('None')

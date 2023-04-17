class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(head1: Node, head2: Node) -> Node:
    curr1 = head1
    curr2 = head2
    
    while curr1 is not None and curr2 is not None:
        # Save next pointers
        next1 = curr1.next
        next2 = curr2.next
        
        # Link curr2 after curr1
        curr1.next = curr2
        curr2.next = next1
        
        # Update current pointers
        curr1 = next1
        curr2 = next2
    
    # Return the updated head of the first list
    return head1
head1 = Node(1, Node(3, Node(5, Node(7, Node(9)))))
head2 = Node(2, Node(4, Node(6, Node(8, Node(10)))))

new_head = merge_lists(head1, head2)
while new_head is not None:
    print(new_head.val, end=' -> ')
    new_head = new_head.next

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_at_level(root, level):
    if not root:
        return 0

    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, current_level = queue.popleft()

        if current_level == level:
            count += 1
        elif current_level > level:
            break

        if node.left:
            queue.append((node.left, current_level + 1))
        if node.right:
            queue.append((node.right, current_level + 1))

    return count

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

level = 2
count = count_nodes_at_level(root, level)
print("Number of nodes at level", level, ":", count)

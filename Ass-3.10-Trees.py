class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_odd_levels(root):
    if root is None:
        return

    queue = [root]
    level = 1

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)

            if level % 2 != 0:
                print(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level += 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Nodes at odd levels:")
print_odd_levels(root) 

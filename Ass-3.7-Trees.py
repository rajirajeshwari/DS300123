class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    if not root:
        return 0

    stack = [(root, False)]
    sum_left_leaves = 0

    while stack:
        node, is_left = stack.pop()

        if is_left and not node.left and not node.right:
            sum_left_leaves += node.val

        if node.left:
            stack.append((node.left, True))

        if node.right:
            stack.append((node.right, False))

    return sum_left_leaves

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sum_of_left_leaves(root))  


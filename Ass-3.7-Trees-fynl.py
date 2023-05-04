class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_all_nodes(root):
    if root is None:
        return 0
    return root.val + sum_all_nodes(root.left) + sum_all_nodes(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)

sum_of_nodes = sum_all_nodes(root)
print("Sum of all nodes in the tree:", sum_of_nodes)  

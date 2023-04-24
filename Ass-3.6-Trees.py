class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0
    
    def isLeaf(node):
        return node and not node.left and not node.right
    
    def traverse(node):
        if not node:
            return 0
        if isLeaf(node.left):
            return node.left.val + traverse(node.right)
        return traverse(node.left) + traverse(node.right)
    
    return traverse(root)
# Create a binary tree
#     3
#    / \
#   9  20
#     /  \
#    15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sum_left_leaves = sumOfLeftLeaves(root)
print(sum_left_leaves)  

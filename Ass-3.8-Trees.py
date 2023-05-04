class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum_x(root, x):
    if root is None:
        return 0

    count = 1 if root.val == x else 0

    count += count_subtrees_with_sum_x(root.left, x - root.val)
    count += count_subtrees_with_sum_x(root.right, x - root.val)
    return count

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

count = count_subtrees_with_sum_x(root, 22)
print("Number of subtrees that sum up to 22 in the tree:", count)  
  

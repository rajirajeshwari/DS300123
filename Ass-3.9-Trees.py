class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_level_sum(root):
    if root is None:
        return 0

    queue = [root]
    max_sum = float("-inf")
    level = 0

    while queue:
        level_sum = 0
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        level += 1

    return max_level

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

max_sum_level = max_level_sum(root)
print("Maximum level sum:", max_sum_level) 

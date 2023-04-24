class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new_node
                return
            elif node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def print_leaves(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.val, end=" ")
        self.print_leaves(node.left)
        self.print_leaves(node.right)
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print("Leaf nodes:")
tree.print_leaves(tree.root)

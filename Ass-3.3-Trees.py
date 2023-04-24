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

    def preorder_traversal(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.val, end=" ")
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.val, end=" ")
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print("Pre-order traversal:")
tree.preorder_traversal(tree.root)
print("\nIn-order traversal:")
tree.inorder_traversal(tree.root)
print("\nPost-order traversal:")
tree.postorder_traversal(tree.root)

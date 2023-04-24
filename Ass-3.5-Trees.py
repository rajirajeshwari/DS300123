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

    def bfs(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def dfs_preorder(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)

    def dfs_inorder(self, node):
        if node is None:
            return
        self.dfs_inorder(node.left)
        print(node.val, end=" ")
        self.dfs_inorder(node.right)

    def dfs_postorder(self, node):
        if node is None:
            return
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node.val, end=" ")
# Create a binary tree and insert some nodes
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

# BFS traversal
print("BFS traversal:")
tree.bfs()  

# Pre-order DFS traversal
print("\nPre-order DFS traversal:")
tree.dfs_preorder(tree.root)  

# In-order DFS traversal
print("\nIn-order DFS traversal:")
tree.dfs_inorder(tree.root)  

# Post-order DFS traversal
print("\nPost-order DFS traversal:")
tree.dfs_postorder(tree.root)  

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def get_height(self,node):
        if not node:
            return -1

        left_height=self.get_height(node.left)
        right_height=self.get_height(node.right)

        return 1 + max(left_height,right_height)


t1=BinaryTree(1)
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
t1.root.right.left.left=Node(8)
print(t1.get_height(t1.root))

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start):
        if start:
            print(start.value)
            self.preorder(start.left)
            self.preorder(start.right)

    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.value)
            self.inorder(start.right)

    def postorder(self,start):
        if start:
            self.postorder(start.left)
            self.postorder(start.right)
            print(start.value)


t1=BinaryTree(1)
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
# t1.preorder(t1.root)
# t1.inorder(t1.root)
t1.postorder(t1.root)

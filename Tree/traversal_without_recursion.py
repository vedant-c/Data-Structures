class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def inorder(self,root):
        current=root
        stack=[]
        while True:
             if current:
                 stack.append(current)
                 current=current.left
             elif stack:
                current=stack.pop()
                print(current.value)
                current=current.right
             else:
                break

    def preorder(self,root):
        current=root
        stack=[]
        stack.append(root)
        while stack:
            current=stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


    def postorder(self,root):
        current=root
        s1=[]
        s2=[]
        s1.append(root)
        while s1:
            current=s1.pop()
            s2.append(current)
            if current.left:
                s1.append(current.left)
            if current.right:
                s1.append(current.right)
        while s2:
            print(s2.pop().value)

t1=BinaryTree(1)
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
# t1.inorder(t1.root)
t1.postorder(t1.root)

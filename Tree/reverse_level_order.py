class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def reverse_level_order(self,start):
        queue=[start]
        stack=[]
        while queue:
            cur=queue.pop(0)
            stack.insert(0,cur)

            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        while stack:
            print(stack.pop(0).value)


t1=BinaryTree(1)
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
t1.reverse_level_order(t1.root)

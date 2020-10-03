class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def size(self):
        # if not self.root:
        #     print(1)
        #     return
        stack=[self.root]
        size=1
        while stack:
            cur=stack.pop(0)
            if cur.left:
                stack.append(cur.left)
                size+=1
            if cur.right:
                stack.append(cur.left)
                size+=1

        print(size)

    def size_recursive(self,node):
        if node is None:
            return 0

        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


t1=BinaryTree(1)
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
t1.size()
print(t1.size_recursive(t1.root))

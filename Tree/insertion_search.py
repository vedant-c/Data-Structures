class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BST:
    def __init__(self,):
        self.root=None

    def insert(self,data):
        #ezpz
        new_node=Node(data)

        if not self.root:
            self.root=new_node
            return

        cur=self.root
        while cur:
            if data<cur.value:
                if cur.left is None:
                    cur.left=new_node
                    return
                cur=cur.left
            else:
                if cur.right is None:
                    cur.right=new_node
                    return
                cur=cur.right

    def find(self,data):
        cur=self.root
        while cur:
            if data<cur.value and cur.left:
                cur=cur.left
                if cur.value==data:
                    print("True")
                    return
            elif data>cur.value and cur.right:
                cur=cur.right
                if cur.value==data:
                    print("False")
                    return
            else:
                cur=None
                print("False")
        return None




t1=BST()
t1.insert(10)
t1.insert(8)
t1.insert(6)
t1.insert(3)
t1.insert(14)
t1.insert(12)
print(t1.root.left.value)
print(t1.root.right.value)
print(t1.root.left.left.value)
print(t1.root.right.left.value)
t1.find(6)
t1.find(12)
t1.find(11)

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
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

    def level_order(self):
        queue=[self.root]
        while queue:
            cur=queue.pop(0)
            print(cur.value)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def delete(self,data):

        current=self.root
        parent=None

        while current.value!=data:
            parent=current
            if data<current.value:
                current=current.left
            else:
                current=current.right


        if  current.left and current.right:
            del_node=current.right
            del_parent=current
            while del_node.left:
                del_parent=del_node
                del_node=del_node.left

            current.value=del_node.value
            if del_node.right:
                if del_parent.value>del_node.value:
                    del_parent.left=del_node.right
                else:
                    del_parent.right=del_node.right
            else:
                if del_parent.value>del_node.value:
                    del_parent.left=None
                else:
                    del_parent.right=None
            return

        if current.left or current.right:
            if data<parent.value:
                if current==parent.left:
                    parent.left=current.left
                else:
                    parent.right=current.left
                return
            else:
                if current==parent.left:
                    parent.left=current.right
                else:
                    parent.right=current.right
                    return


        elif current==parent.left:
            parent.left=None
        else:
            parent.right=None


    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.value)
            self.inorder(start.right)


t1=BinaryTree()
t1.insert(10)
t1.insert(5)
t1.insert(14)
t1.insert(3)
t1.insert(8)
t1.insert(12)
t1.insert(18)
t1.insert(6)
t1.insert(9)
t1.delete(8)
t1.inorder(t1.root)

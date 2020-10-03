class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        last_node=self.head
        while last_node.next:
            last_node=last_node.next

        last_node.next=new_node

    def nth_last(self,n):
        p=self.head
        q=self.head

        count=0
        while q and count<n:
            q=q.next
            count+=1
        if q is None:
            print( str(n) + "is greater than number of nodes")
            return

        while p and q:
            p=p.next
            q=q.next

        print(p.data)


llist=Linkedlist()
llist.append("a")
llist.append("b")
llist.append("c")
llist.append("d")
llist.append("e")
llist.nth_last(3)
# llist.print_list()

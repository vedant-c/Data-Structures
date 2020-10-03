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

    def delete(self,data):

        curr=self.head
        if curr and curr.data==data:
            self.head=curr.next
            curr=None
            return

        prev=None
        while curr and curr.data!=data:
            prev=curr
            curr=curr.next

        if curr is None:
            return

        prev.next=curr.next
        curr=None

    def rem_dup(self):
        values={}
        cur=self.head
        prev=None

        while cur:
            if cur.data in values:
                prev.next=cur.next
            else:
                values[cur.data]=1
                prev=cur
            cur=cur.next




l1=Linkedlist()
l1.append(1)
l1.append(6)
l1.append(1)
l1.append(4)
l1.append(2)
l1.append(2)
l1.append(4)
l1.rem_dup()
l1.print_list()

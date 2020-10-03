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

    def rotate(self,val):
        p=self.head
        q=self.head

        while q:
            if q.data==val:
                break
            q=q.next
        self.head=q.next
        q.next=None
        q=self.head

        while q.next:
            q=q.next
        q.next=p



l1=Linkedlist()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.rotate(4)
l1.print_list()

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

    def tail_to_head(self):
        p=self.head
        prev=None

        while p.next:
            prev=p
            p=p.next
        prev.next=None
        p.next=self.head
        self.head=p
    

l1=Linkedlist()
l1.append("a")
l1.append("b")
l1.append("c")
l1.append("d")
l1.append("e")
l1.tail_to_head()
l1.print_list()

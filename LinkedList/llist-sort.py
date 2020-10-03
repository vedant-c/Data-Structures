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

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def sort(self,l2):

        p1=self.head
        p2=l2.head
        s=None

        if p1 and p2:
            if p1.data<=p2.data:
                s=p1
                p1=s.next
            else:
                s=p2
                p2=s.next
            newhead=s

        while p1 and p2:
            if p1.data<=p2.data:
                s.next=p1
                s=p1
                p1=s.next
            else:
                s.next=p2
                s=p2
                p2=s.next

        if not p1:
            s.next=p2
        if not p2:
            s.next=p1

        self.head=newhead



l1=Linkedlist()
l1.append(1)
l1.append(5)
l1.append(7)
l1.append(9)
l1.append(10)

l2=Linkedlist()
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(6)
l2.append(8)


l1.sort(l2)
l1.print_list()

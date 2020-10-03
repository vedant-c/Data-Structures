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

    def sum_two_lists(self,l2):
        l3=Linkedlist()

        p1=self.head
        p2=l2.head

        while p1 or p2:
            p=p1.data
            q=p2.data
            s=p+q
            if s>=10:
                l3.append(s%10)
                if p1.next:
                    p1.next.data+= (s//10)
                else:
                    l3.append(s//10)
            else:
                l3.append(p1.data+p2.data)
            p1=p1.next
            p2=p2.next

        l3.print_list()

l1=Linkedlist()
l1.append(5)
l1.append(6)
l1.append(3)

l2=Linkedlist()
l2.append(8)
l2.append(4)
l2.append(7)

l1.sum_two_lists(l2)

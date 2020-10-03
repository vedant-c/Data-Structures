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

    def prepend(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        curr=self.head
        self.head=new_node
        new_node.next=curr

    def insert(self,data,prev):
        new_node=Node(data)
        curr=self.head

        if not prev:
            print("Previos node not in the list")
            return

        new_node.next=prev.next
        prev.next=new_node

    def insert1(self,data,pos):
        new_node=Node(data)
        curr=self.head

        i=1
        while i<pos-1:
            curr=curr.next
            i+=1

        new_node.next=curr.next
        curr.next=new_node

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

    def delete_pos(self,pos):

        curr=self.head
        if pos==0:
            self.head=curr.next
            curr=None
            return

        prev=None
        count=0
        while curr and count!=pos:
            prev=curr
            curr=curr.next
            count+=1

        if curr is None:
            return

        prev.next=curr.next
        curr=None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


    def swap_node(self,n1,n2):
        if n1==n2:
            return

        cur1=self.head
        prev1=None
        cur2=self.head
        prev2=None

        while cur1 and cur1.data!=n1:
            prev1=cur1
            cur1=cur1.next
        while cur2 and cur2.data!=n2:
            prev2=cur2
            cur2=cur2.next

        if prev1:
            prev1.next=cur2
        else:
            self.head=cur2

        if prev2:
            prev2.next=cur1
        else:
            self.head=cur1
        cur1.next,cur2.next=cur2.next,cur1.next

    def reverse_iterative(self):
        prev=None
        cur=self.head

        while cur:
            t= cur.next
            cur.next=prev
            prev=cur
            cur=t

        self.head=prev

    def reverse_recursive(self):

        def _reverse_recursive(cur,prev):
            if not cur:
                return prev

            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
            return _reverse_recursive(cur, prev)

        self.head=_reverse_recursive(cur=self.head, prev=None)


    def sort(self,l2):
        l3=Linkedlist()
        l3.append(min(llist.head.data,l2.head.data))
        l3.append(max(llist.head.data,l2.head.data))

        l3.print_list()





llist=Linkedlist()
llist.append("a")
llist.append("b")
llist.append("c")
llist.append("d")
llist.append("e")
# llist.delete1(2)
# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))
# llist.swap_node("a","d")
llist.reverse_recursive()
llist.sort()
# llist.print_list()

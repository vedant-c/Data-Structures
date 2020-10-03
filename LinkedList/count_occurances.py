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

    def count_occurances_iterative(self,val):

        occ={}
        cur=self.head
        while cur:
            occ[cur.data]=occ.get(cur.data,0)+1
            cur=cur.next

        print(occ[val])

    def count_occurances_recursive(self,node,val):
        if not node:
            return 0
        if node.data==val:
            return 1 + self.count_occurances_recursive(node.next,val)
        else:
            return self.count_occurances_recursive( node.next, val)


llist=Linkedlist()
llist.append(1)
llist.append(2)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(1)
llist.append(4)
llist.append(1)
llist.count_occurances_iterative(1)
print(llist.count_occurances_recursive(llist.head,1))

# llist.print_list()

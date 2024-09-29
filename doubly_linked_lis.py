class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class linked_list:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head is  None:
            print("linked list is empty")
        else:
            n=self.head
            while(n is not None):
                print(n.data,end="-->")
                n=n.nref
    def printLL_reverse(self):
        if self.head is  None:
            print("linked list is empty")
        else:
            n=self.head
            while(n.nref is not None):
                
                n=n.nref
            while n is not None:
                print(n.data,end="-->")
    def insert_at_empty(self,data):
        if self.head is not None:
            print("linked list is not empty")
        else:
            newnode=Node(data)
            self.head=newnode
    def add_begin(self,data):
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
        else:
            self.head.pref=newnode
            newnode.nref=self.head
            self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=newnode
            newnode.pref=n
    def add_after(self,data,x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("the node is not present in Linked List")
            else:
                newnode=Node(data)
                newnode.nref=n.nref
                newnode.pref=n
                if n.nref is not None:
                    n.nref.pref=newnode
                n.nref=newnode
    def add_before(self,data,x):
        if(self.head is None):
            print("linkedlist is empty")
            return
        if self.head.data==x:
            newnode=Node(data)
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
            return
        n=self.head
        while n.nref is not None:
            if n.data == x:
                break
            n=n.nref
        newnode=Node(data)
        newnode.nref=n
        newnode.pref=n.pref
        n.pref.nref=newnode
        n.pref=newnode
    def del_begin(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        if self.head.nref is None:
            self.head=None
            print("after deleting the linked list is empty")
        else:
            self.head=self.head.nref
    def del_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.nref is None:
            self.head=None
            print("after deleting the node")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def del_by_val(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("x is not present in linked list")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
LL=linked_list()
LL.add_begin(39)
LL.add_end(400)
LL.add_begin(30)
LL.add_before(50,30)
LL.del_begin()
LL.del_end()
LL.printLL()

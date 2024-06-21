class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,x):
        t=self.head
        if t==None:
            self.head=node(x)
            return
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addfront(self,x):
        t=self.head
        if t==None:
            self.head=node(x)
            return
        node.next=self.head
        self.head=node(x)
    def add1(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
    def linear_search(self,x):
        t=self.head
        while t:
            if t.data==x:
                print("Found")
                return
            t=t.next
        print("Not Found")
    def middle(self):
        fast=self.head
        slow=self.head
        while(fast!=None and fast.next!=None): #keep fast!=None should be first as if reversed the none of next is not possible so if false and and is the function we cannot do it
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    def length_ll(self):
        fast=self.head
        slow=self.head
        while(fast!=None and fast.next!=None): #keep fast!=None should be first as if reversed the none of next is not possible so if false and and is the function we cannot do it
            slow=slow.next
            fast=fast.next.next
        if(fast==None):
           print("Even")
        else:
            print("Odd")
obj1 = sll()
obj1.addback(10)
obj1.addback(20)
obj1.addback(30)
obj1.addback(40)
obj1.addback(50)
obj1.addback(60)
obj1.display()
print()
obj1.add1()
print()
obj1.linear_search(30)
print()
obj1.middle()
obj1.length_ll()
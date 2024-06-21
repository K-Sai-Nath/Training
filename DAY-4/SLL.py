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
    def add1(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
obj1 = sll()
obj1.addback(10)
obj1.addback(20)
obj1.addback(30)
obj1.addback(40)
obj1.addback(50)
obj1.display()
print()
obj1.add1()
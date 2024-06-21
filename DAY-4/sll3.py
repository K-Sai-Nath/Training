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
        while(fast!=None and fast.next!=None): 
            slow=slow.next
            fast=fast.next.next
        if(fast==None):
           print("Even")
        else:
            print("Odd")
    def max_consecutive(self):
        t=self.head
        count=1
        max1=1
        while (t.next!=None):
            if(t.data==t.next.data-1):  #1 2 3 4 5 11 12 13 max=5
                count+=1
            else:
                if(count>max1):
                    max1=count
                count=1
            t=t.next
        if(count>max1):
            max1=count
        print(max1)
    '''def all_possible_pair(self):
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next'''
    def bubble_sort(self):
        t=self.head
        while(t.next!=None):
            t1=self.head
            flag=0
            while(t1.next!=None):
                if t1.data>t1.next.data:
                    flag=1
                    t1.data,t1.next.data=t1.next.data,t1.data
                t1=t1.next
            if flag==0:
                break
            t=t.next
obj1 = sll()
obj1.addback(6)
obj1.addback(7)
obj1.addback(4)
obj1.addback(8)
obj1.addback(5)
obj1.addback(1)
obj1.display()
print()
obj1.add1()
print()
obj1.linear_search(30)
print()
obj1.middle()
obj1.length_ll()
print()
obj1.max_consecutive()
print()
#obj1.all_possible_pair()
obj1.bubble_sort()
obj1.display()
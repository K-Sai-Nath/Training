class node():
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
class dll():
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            '''self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next'''
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
        print()
    def reverse_display(self):
        temp=self.tail
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.prev
        print()
    def linear_search(self,x):
        '''t=self.head
        while(t!=None):
            if(t.data==x):
                print("Found")
                return
            t=t.next
        print("Not Found")'''
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t.next):
            if(t.data==x or t1.data==x):
                return 1
            t=t.next
            t1=t1.prev
        if(t.data==x):
            return 1
        else:
            return 0
    def evenorodd(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            print("Odd")
        else:
            print("Even")
    def palindrome(self):
        t=self.head
        t1=self.tail
        flag=1
        while t!=t1 and t!=t1.next:
            if t.data!=t1.data:
                flag=0
                break
            t=t.next
            t1=t1.prev
        if flag==0:
            print("Not Palindrome")
        else:
            print("Palindrome")
    def transfer(self):
        '''t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        temp=self.head                  3 5 7 8 9 10 12 15
        while(t!=None):                 9 10 12 15 3 5 7 8
            temp.data,t.data=t.data,temp.data
            t=t.next
            temp=temp.next'''
        t=self.head
        t1=self.tail
        fast=self.head
        slow=self.head
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        slow.t.next=slow.next
        slow.head.prev=slow.t
        t1=slow.prev
        t1.next=None
        slow.prev=None
        slow.head=slow
        slow.t=t1
    def swap_links(self):
        t1 = self.head
        t2 = self.head.next
        temp = self.head
        self.head = self.head.next
        pre = None
        while temp!=None:
            temp = t2.next
            t2.next = t1
            t1.prev = t2
            t2.prev = pre
            if pre:
                pre.next = t2
            pre = t1
            if temp:
                t1 = temp 
                t2 = temp.next
        self.tail = pre
        self.tail.next = None
obj = dll()
obj.addfront(10)
obj.addfront(20)
obj.addfront(30)
obj.addfront(20)
obj.addfront(10)
#obj.addfront(80)
obj.display()
#obj.reverse_display()
#obj.linear_search(10)
obj.evenorodd()
obj.palindrome()
#obj.transfer()
#obj.display()
obj.swap_links()
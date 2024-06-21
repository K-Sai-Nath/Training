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
            
            
class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif root.data>x:
           root.left= self.create(root.left,x)
        else:
            root.right= self.create(root.right,x)
        return root
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
    def add_allnodes(self,root):
        if(root==None):
            return 0 
        return root.data+self.add_allnodes(root.left)+self.add_allnodes(root.right)
    def even_sum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.even_sum(root.left)+self.even_sum(root.right)
        else:
            return self.even_sum(root.left)+self.even_sum(root.right)   #check left and right but dont add root
    def odd_sum(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
            return root.data+self.odd_sum(root.left)+self.odd_sum(root.right)
        else:
            return self.odd_sum(root.left)+self.odd_sum(root.right)
    def abs_evod(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
           return root.data+(self.abs_evod(root.left)+self.abs_evod(root.right))
        return (self.abs_evod(root.left)+self.abs_evod(root.right))-root.data
    def height(self,root):
        if(root==None):
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balanced(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def count_leafnode(self,root):
        if(root == None):
            return 0
        if(root.left is None and root.right is None):
            return 1
        return self.count_leafnode(root.left)+self.count_leafnode(root.right)
    def leafnodesum(self,root):
        if(root==None):
            return 0
        if(root.right==None and root.left==None):
            return root.data
        return self.leafnodesum(root.right)+self.leafnodesum(root.left)
    def search(self,root,key):
        if(root==None):
            return  0
        if(root.data==key):
            return 1
        if(root.data>key):
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    def depth(self,root,y,c):
        if(root==None):
            return -1
        if(root.data==y):
            return c
        if(root.data>y):
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
    def leftview(self,root,c,l):
        if(root==None):
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
    def rightview(self,root,c,l):
        if(root==None):
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
    def topview(self,root,di,que):
        if(root==None):
            return []
        while(que):
            r,level=que.pop(0)
            if level not in di:
                di[level]=r.data
            if r.left:
                que.append((r.left,level-1))
            if r.right:
                que.append((r.right,level+1))
        l=[]
        for i in sorted(di.keys()):
            l.append(di[i])
        return l
    def bottomview(self,root,di,que):
        if(root==None):
            return []
        while(que):
            r,level=que.pop(0) 
            di[level]=r.data
            if r.left:
                que.append((r.left,level-1))
            if r.right:
                que.append((r.right,level+1))
        l=[]
        for i in sorted(di.keys()):
            l.append(di[i])
        return l
    # def verticalview()
t1=tree()
t1.root=node(10)    #t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,3)
t1.create(t1.root,7)
t1.create(t1.root,2)
# t1.inorder(t1.root)
# print()
# t1.preorder(t1.root)
# print()
# t1.postorder(t1.root)
# print()
# print(t1.add_allnodes(t1.root))
# print("Left Subtree sum:")
# print(t1.add_allnodes(t1.root.left))
# print("Right subtree sum:")
# print(t1.add_allnodes(t1.root.right))
# print("absolute difference of left,right:")
# print(abs(t1.add_allnodes(t1.root.left)-t1.add_allnodes(t1.root.right)))
# print("Sum of even nodes:")
# print(t1.even_sum(t1.root))
# print("ODD Sum:")
# print(t1.odd_sum(t1.root))
# print("Absolute Difference:")
# print(abs(t1.abs_evod(t1.root)))
# print("Height of Tree:")
# print(t1.height(t1.root))
# if(t1.balanced(t1.root)):
#     print("Balanced Tree")
# else:
#     print("Not Balanced Binary Search Tree")
# print(t1.count_leafnode(t1.root))
# print(t1.leafnodesum(t1.root))
# if(t1.search(t1.root,15)==1):
#     print("Found")
# else:
#     print("Not Found")
# print("Depth of node is:",t1.depth(t1.root,15,0))
# t1.leftview(t1.root,0,[])
# print()
# t1.rightview(t1.root,0,[])
print()
print(t1.topview(t1.root,{},[(t1.root,0)]))
print(t1.bottomview(t1.root,{},[(t1.root,0)]))
'''top,left right'''
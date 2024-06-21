class Node:
    def __init__(self):
        self.d={}
        self.flag=0  
class Tries:
    def __init__(self):
        self.root=Node()
    def insert(self,st):
        t=self.root
        for i in st:
            if i not in t.d:
                t.d[i]=Node()
            else:
                t=t.d[i]
        t.flag=1
    def searchWord(self,st):
        t=self.root
        for i in st:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False
    def searchPrefix(self,st):
        t=self.root
        for i in st:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def PrintAllPrefix(self,st):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in st:
            if(i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return 
        fun(t)
t1=Tries()
n=int(input())
for i in range(n):
    q,s=input().split()
    if (q=='1'):
        t1.insert(s)
    if (q=='2'):
        print(t1.searchWord(s))
    if (q=='3'):
        print(t1.searchPrefix(s))

'''
word
world
wood
words
apple
apricot
[b,ba,wo,ap]
print the prefix from the given list who has longest string in the Trie
lexicographically longest
erasing
'''
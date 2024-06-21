'''class TrieNode():
    def __init__(self):
        self.dict={}
        self.flag=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                node.dict[i]=TrieNode()
            node=node.dict[i]
        node.flag=True
    def display(self):
        node=self.root
        res=[]
        def dfs(node,word):
            if node.flag==1:
                res.append(word[:])
            for i in node.dict.keys():
                dfs(node.dict[i],word+i)
        dfs(node,"")
        print(res)
    def search_word(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        if node.flag==1:
            return True
        return False
    def prefix(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        return True
                
t1=Trie()
t1.insert("word")
t1.insert("apple")
t1.insert("words")
t1.display()
print(t1.search_word("words"))
print(t1.search_word("world"))
print(t1.prefix("app"))
'''
'''from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.dict={}
        self.flag=False
        self.count=defaultdict(int)
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                node.dict[i]=TrieNode()
            node.count[i]+=1
            node=node.dict[i]
        node.flag=True
    def display(self):
        node=self.root
        res=[]
        def dfs(node,word):
            if node.flag==1:
                res.append(word[:])
            for i in node.dict.keys():
                dfs(node.dict[i],word+i)
        dfs(node,"")
        print(res)
    def search_word(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        if node.flag==1:
            return True
        return False
    def prefix(self,word):
        node=self.root
        flag=0
        res=float('inf')
        for i in word:
            res=min(res,node.count[i])
            if i not in node.dict.keys():
                break
            node=node.dict[i]
        return res
    def prefix_word(self,word):
        node=self.root
        res=[]
        def dfs(node,idx,word1):
            if idx==len(word):
                if node.flag==1:
                    res.append(word1)
                for i in node.dict.keys():
                    dfs(node.dict[i],idx,word1+i)
                    return
            for i in node.dict.keys():
                if i!=word[idx]:
                    continue
                else:
                    dfs(node.dict[i],idx+1,word1+word[idx])
        dfs(node,0,"")
        lng=-1
        out=""
        print(res)
        for i in res:
            if len(i)>lng:
                lng=len(i)
                out=i
        return out
t1=Trie()
t1.insert("worlds")
t1.insert("word")
t1.insert("apple")
t1.insert("words")
t1.insert("world")
t1.insert("wood")
t1.insert("apricot")
t1.insert("wo")
t1.display()
print(t1.search_word("wards"))
print(t1.search_word("world"))
print(t1.prefix("wo"))
t1.prefix_word("wo")
l=['b','ba','wo','ap']
lng=-1
res=""
for i in l:
    out=t1.prefix_word(i)
    if len(out)>lng:
        lng=len(out)
        res=out
    elif len(out)==lng:
        lng=len(out)
        res=min(res,out)
print(res)'''
from collections import defaultdict
class TrieNode():
    def _init_(self):
        self.dict={}
        self.flag=False
        self.count=defaultdict(int)
class Trie:
    def _init_(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                node.dict[i]=TrieNode()
            node.count[i]+=1
            node=node.dict[i]
        node.flag=True
    def display(self):
        node=self.root
        res=[]
        def dfs(node,word):
            if node.flag==1:
                res.append(word[:])
            for i in node.dict.keys():
                dfs(node.dict[i],word+i)
        dfs(node,"")
        print(res)
    def search_word(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        if node.flag==1:
            return True
        return False
    def prefix(self,word):
        node=self.root
        flag=0
        res=float('inf')
        for i in word:
            res=min(res,node.count[i])
            if i not in node.dict.keys():
                break
            node=node.dict[i]
        return res
    def prefix_word(self,word):
        node=self.root
        res=[]
        def dfs(node,idx,word1):
            if idx==len(word):
                if node.flag==1:
                    res.append(word1)
                for i in node.dict.keys():
                    dfs(node.dict[i],idx,word1+i)
                return
            for i in node.dict.keys():
                if i!=word[idx]:
                    continue
                else:
                    dfs(node.dict[i],idx+1,word1+word[idx])
        dfs(node,0,"")
        lng=-1
        out=""
        print(res)
        for i in res:
            if len(i)>lng:
                lng=len(i)
                out=i
        return out
                
t1=Trie()
t1.insert("word")
t1.insert("worlds")
t1.insert("wood")
t1.insert("apple")
t1.insert("apricot")
t1.insert("words")
t1.insert("wo")
t1.display()
print(t1.search_word("words"))
print(t1.search_word("world"))
print(t1.prefix("wo"))
t1.prefix_word("wo")
l=['b','ba','wo','ap']
lng=-1
res=""
for i in l:
    out=t1.prefix_word(i)
    if len(out)>lng:
        lng=len(out)
        res=out
    elif len(out)==lng:
        lng=len(out)
        res=min(res,out)
print(res)
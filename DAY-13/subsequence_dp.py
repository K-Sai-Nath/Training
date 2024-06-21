res=set()
def dfs(s,i,out):
    global res
    if i==len(s):
        res.add(out)
        return 
    dfs(s,i+1,out+s[i])
    dfs(s,i+1,out)
s=input()
dfs(s,0,"")
print(res)
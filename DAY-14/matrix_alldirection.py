'''#using recursion
m=4
n=3
res=0
def fun(i,j,m,n,visited):
    global res
    if i<0 or j<0 or i==m or j==n:
        return
    if(i,j) in visited:
        return
    if i==m-1 and j==n-1:
        res+=1 
        return
    visited.add((i,j))
    fun(i-1,j,m,n,visited)
    fun(i,j-1,m,n,visited)
    fun(i+1,j,m,n,visited)
    fun(i,j+1,m,n,visited)
    visited.remove((i,j))
fun(0,0,m,n,set())
print(res)
'''
def fun():
    if(i>0 or i>=n or j<0 or j>=m or (i==k and j==l)):
        return
    if (i==m-1 and j==n-1):
         c+=1 
         return c 
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
    
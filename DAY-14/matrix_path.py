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
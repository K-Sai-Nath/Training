'''def solve(i,j,mat):
    if i<0 or j<0 or i>=n or j>=n or mat[i][j]==0:
        return
    if mat[i][j]==1:
        mat[i][j]=0
    solve(i-1,j,mat)
    solve(i,j+1,mat)
    solve(i,j-1,mat)
    solve(i+1,j,mat)
n=5
c=0
mat=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in range(n):
    for j in range(n):
        if(mat[i][j]==1):
            c=c+1
            solve(i,j,mat)
print(c)'''
'''ip=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
res=-float('inf')
def dfs(ip,i,j):
    if i>=len(ip) or j>=len(ip) or i<0 or j<0 or ip[i][j]==0:
        return 0
    ip[i][j]=0
    out=1
    out+=dfs(ip,i+1,j)
    out+=dfs(ip,i,j+1)
    out+=dfs(ip,i-1,j)
    out+=dfs(ip,i,j-1)
    return out
for i in range(len(ip)):
    for j in range(len(ip)):
        if ip[i][j]==1:
            res=max(res,dfs(ip,i,j))
print(res)'''

def solve(i,j,mat,c):
    if i<0 or j<0 or i>=n or j>=n or mat[i][j]==0:
        return c
    if mat[i][j]==1:
        mat[i][j]=0
    solve(i-1,j,mat,c)
    solve(i,j+1,mat,c)
    solve(i,j-1,mat,c)
    solve(i+1,j,mat,c)
n=5
co=0
m=0
mat=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in range(n):
    for j in range(n):
        if(mat[i][j]==1):
            co=co+1
            k=solve(i,j,mat,0)
            if(k>m):
                m=k
print(c,m)

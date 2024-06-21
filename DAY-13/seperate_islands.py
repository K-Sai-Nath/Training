def solve(i,j,mat):
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
print(c)
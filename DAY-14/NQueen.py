n=4
board=[['.' for i in range(n)] for j in range(n)]
cnt=0
out=[]
def isValid(row,col,board,n):
    for j in range(n):
        if board[j][col]=='Q':
            return False
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    i=row
    j=col
    while i>=0 and j<n:
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
    return True
def nqueen(row,board,n):
    global cnt
    if row==n:
        cnt+=1
        return
    for col in range(n):
        if isValid(row,col,board,n):
            board[row][col]='Q'
            nqueen(row+1,board,n)
            board[row][col]='.'
nqueen(0,board,n)
print(cnt)
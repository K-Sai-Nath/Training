'''
[(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)]

[5,6,5,4,11,2]

17
'''
times=[(1,3,5),(2,5,6),(4,6,5),(6,7,4),(5,8,11),(7,9,2)]
times.sort()
def search(i):
    for j in range(i+1,len(times)):
        if times[i][1]<=times[j][0]:
            return j 
    return -1
def dfs(i):
    if i==len(times):
        return 0
    next1=search(i)
    if next1!=-1:
        take=times[i][2]+dfs(next1)
    else:
        take=times[i][2]
    nottake=dfs(i+1)
    return max(take,nottake)
print(dfs(0))
'''
times=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
wages=[5,6,5,4,11,2]
b=wages.copy()
for i in range(1,len(wages)):
    for j in range(0,i):
        if(j[1]<=i[0]):
            if(b[j]+wages[i]>b[i]):
                b[i]=b[j]+wages[i]
print(max(b))

        '''
    
'''def sortthree(l):
    res=[]
    for i in range(len(l)-2):
        new=[l[i],l[i+1],l[i+2]]
        print(new)
        new.sort()
        l[i:i+3] = new[0:]
        res.append(new[0])
    res.append(l[len(l)-2])
    res.append(l[len(l)-1])
    print(res)'''
l=list(map(int,input().split()))
# sortthree(l)
n=len(l)
for i in range(n-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
print(l)
'''
9 8 1
a[0]=min(9,8,1) 1
a[2]=max(9,8,1) 9
a[1]=sum-a[0]-a[2]
18-9-1=8
1 8 9'''
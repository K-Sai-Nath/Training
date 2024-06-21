l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
res=[]
s=0
def add(l1,l2,i,j):
    global res,s
    if(i==len(l1)):
        return 
    if(j==len(l2)):
        add(l1,l2,i+1,0)
        s=0
        return
    if(l1[i]%2)==0:
        if(l2[j]%2!=0):
            s+=(l1[i]+l2[j])
        add(l1,l2,i,j+1)
    else:
        res.append(s)
        s=0
        add(l1,l2,i+1,j)
add(l1,l2,0,0)
print(res)
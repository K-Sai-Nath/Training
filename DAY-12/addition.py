l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
res=[]
def add(l1,l2,i,j):
    if(i==len(l1)):
        return 
    if(j==len(l2)):
        add(l1,l2,i+1,0)
        return
    if(l1[i]%2)==0:
        if(l2[j]%2!=0):
            res.append(l1[i]+l2[j])
        add(l1,l2,i,j+1)
    else:
        add(l1,l2,i+1,j)
add(l1,l2,0,0)
print(res)
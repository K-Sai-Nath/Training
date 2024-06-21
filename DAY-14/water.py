w=[2,5,2,3,6,7,1,0,5,7]
'''l1=[0]*len(l)
l2=[0]*len(l)
max_left=l[0]
max_right=l[-1]
l1.append(max_left)
for i in range(len(l)-1):
    if l[i+1]>max_left:
        max_left=l[i+1]
        l1.append(max_left)
for i in range(len(l),0,-1):
    if l[i-1]>max_right:
        max_right=l[i-1]
        l1.append(max_right)'''
l=[0]*len(w)
r=[0]*len(w)
m=0
m1=0
for i in range(len(w)):
    if w[i]>m:
        m=w[i]
    l[i]=m
for i in range(len(w)-1,-1,-1):
    if w[i]>m1:
        m1=w[i]
    r[i]=m1
s=0
for i in range(len(w)):
    s=s+abs(min(l[i],r[i])-w[i])
print(s)
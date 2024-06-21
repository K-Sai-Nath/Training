w=[2,5,2,3,6,7,1,0,5,7]
'''# my logic after sir's explanation
l1=[0]*len(l)
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

'''#Sir explanation
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
'''
''' #Sai Nath's Logic
ip=[2,5,2,3,6,7,1,0,5,7]
n=len(ip)
gl=[0]*len(ip)
gr=[0]*len(ip)
gl[0]=ip[0]
gr[-1]=ip[-1]
for i in range(1,len(ip)):
    gl[i]=max(gl[i-1],ip[i])
print(gl)
for i in range(len(ip)-2,-1,-1):
    gr[i]=max(gr[i+1],ip[i])
print(gr)
res=0
for i in range(len(ip)):
    res+=min(gl[i],gr[i])-ip[i]
print(res)
ip=[4,3,4,5,6,1,0,6,7]'''
'''
#Sai Nath's Two pointer Logic
#First sir said it won't work but then works
ip=[6,4,5,8,2,4]
i=0
j=len(ip)-1
max_left=ip[0]
max_right=ip[-1]
res=0
while i<j:
    if max_right>max_left:
        i+=1
        if ip[i]>max_left:
            max_left=ip[i]
        res+=max_left-ip[i]
    else:
        j-=1
        if ip[j]>max_right:
            max_right=ip[j]
        res+=max_right-ip[j]
print(res)
'''

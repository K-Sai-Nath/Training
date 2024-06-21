#Question - Number and its kth largest factor 12- 1,2,3,4,6,12
'''n=int(input())
k=int(input())
temp=n
while(temp>=1):
    if(n%temp==0):
        k-=1
        if k==0:
            print(temp)
            break
    temp-=1
#Find co-prime numbers:
n1=int(input())
n2=int(input())
flag=0
while True:
    if n2%n1==0:
        if(n1==1):
            print("Co Prime")
            flag=1
        break
    n1=n1%n2
    n2=n1
if flag==0:
    print("Not Co-Prime")'''
    
'''"
op_c=0
cl_c=op_c
for i in s:
    if i in opn:
        op_c+=1
    else:
        cl_c+=1
    cl_c-=1
'''
s="(([{}]))"
opn=['(','{','[']
clo=[')','}',']']
st=[]
b=0
for i in s:
    if i in opn:
        st.append(i)
    if i in clo and i not in st:
        b=s.index(i)
print(b)
'''      
s=input()
st=[]
f=0
for i in s:
    if (i in '{[('):
        st.append(i)
    elif (not st):  #if stack is not empty
        if (i==''}' and st[-1]=='{' or i=='[' and st[-1]==']' or i=='(' and st[-1]==')'):
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
if f==0:
    
    '''
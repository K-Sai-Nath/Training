def isprime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
l=list(map(int,input().split()))
s=0
for i in range(len(l)-1):
    index1=l[i]
    index2=l[i+1]
    for j in range(index2,index1,-1):
        if isprime(j):
            print(j,end=" ")
            s+=j
            break
print(s)

'''[4,8,14,22,36,68]
max prime number between each number
4-8 -->7
8-14 -->13
14-22 -->19
22-36 -->31
36-68 -->67
    sum = 137
    
    PACKAGE : 4LPA

hidden test case:
no prime number in between return 0 
[14,16,20,22]
0+19+0 
19'''
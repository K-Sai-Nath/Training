'''s=input()
n=int(input())
res=""
for i in range(n):
    l=input()
    m=int(input())
    if l=='L':
        res+=s[m]
    else:
        length=len(s)
        res+=s[length-m]
print(res)
for i in range(len(s)-n):
    if sorted(res)==sorted(s[i:n+i]):
        print("TRUE")
        break
else:
    print("FALSE")'''
s=input()
n=int(input())
str1=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str1+=s[int(b[2])]
    else:
        str1+=s[-int(b[2])]
    print(str1)
str1=list(str1)
str1.sort()
print(str1)
b=[]
for i in range(len(s)-n+1):
    temp=list(s[i:n+i])
    temp.sort()
    b.append(temp)
    print(temp)
for i in b:
    if(i==str1):
        print("Yes")
        break
else:
    print("No")
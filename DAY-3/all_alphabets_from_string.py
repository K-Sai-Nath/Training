n=int(input())
mat=[]
for i in range(n):
    mat.append(input())
s=input()
flag=0
for i in range(len(s)):
    if (s[i] in mat):
        continue
    else:
        flag=1
        break
if flag==1:
    print("No")
else:
    print("Yes")

n=int(input())
mat=[]
for i in range(n):
    mat.append(list(input()))   #need to convert to list so to use replace keyword or remove keyword for duplicate characters
s=input()
flag=0
for i in range(len(s)):
    if (s[i] in mat):
        mat[i].remove(s[i])
        continue
    else:
        flag=1
        break
if flag==1:
    print("No")
else:
    print("Yes")

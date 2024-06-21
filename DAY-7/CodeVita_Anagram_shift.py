s=input()
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
    print("FALSE")
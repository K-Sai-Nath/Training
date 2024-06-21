s=input()
max1=1
c=1
for i in range(1,len(s)):
    if ord(s[i])==ord(s[i-1])+1:
        c+=1
    else:
        max1=max(max1,c)
        c=1
max1=max(max1,c) #sliding window so keep else part also out
print(max1)

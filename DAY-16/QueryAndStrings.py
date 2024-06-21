n=int(input())
l=[]
res=[]
for i in range(n):
    val=int(input())
    st=input()
    if val==1:
        l.append(st)
    elif val==2:
        if st in l:
            res.append("True")
        else:
            res.append("False")
    else:
        for i in st:
            if(st[0:len(st)]==st):
                res.append("True")
                break
        else:
            res.append("False")
print(res)
for i in res:
    print(i)
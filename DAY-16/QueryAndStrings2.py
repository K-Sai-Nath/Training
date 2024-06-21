n=int(input())
l=set()
res=[]
for i in range(n):
    val=int(input())
    st=input()
    if val==1:
        l.add(st)
    elif val==2:
        if st in l:
            res.append("True")
        else:
            res.append("False")
    elif val==3:
        count=0
        for i in l:
            if(st[0:len(st)]==st):
                count+=1
        res.append(count)
    else:
        if st in l:
            l.remove(st)
        
print(res)
for i in res:
    print(i)
'''
5
1 word
1 word
3 wo 
4 word
2 word
1- insert
3 - count
4 - remove element
'''
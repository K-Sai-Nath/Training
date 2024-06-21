def sunshadow(l):
    max1=l[0]
    c=1
    for i in range(1,len(l)):
        if max1<l[i]:
            c=c+1
            max1=l[i]
    print(c)
    max1=l[-1]
    c1=1
    for i in range(len(l)-2,-1,-1):
        if max1<l[i]:
            c1=c1+1
            max1=l[i]
    print(c1)
l=[3,5,2,0,8,1]
sunshadow(l)
'''shadwo morning - 3,5,8
shadow evening - 1,8'''
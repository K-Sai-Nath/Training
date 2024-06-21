'''res=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            res.append([l[i],l[j],l[k]])
print(res,end="\n")'''
'''
def generate_pairs(lst, pair=[], index=0,k):
    if len(pair) == k:
        print(pair)
        return

    for i in range(index, len(lst)):
        generate_pairs(lst, pair + [lst[i]], i + 1)

lst = list(map(int,input().split())) # [3, 2, 5, 4, 1, 6, 8]
k=int(input())
generate_pairs(lst)'''
def combination(l,k):
    def fun(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start, len(l)):
            fun(curr + [l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
combination(a,k)
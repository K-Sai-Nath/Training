l=list(map(int,input().split()))
def robber(idx,l,res):
    if idx>=len(l):
        return 0
    return max(l[idx]+robber(idx+2,l,res),robber(idx+1,l,res))
print(robber(0,l,0))
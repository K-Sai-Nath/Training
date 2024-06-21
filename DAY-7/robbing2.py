l=list(map(int,input().split()))

'''
def robber(idx,l,res):
    if idx>=len(l):
        return 0
    return max(l[idx]+robber(idx+2,l,res),robber(idx+1,l,res)) 
print(robber(0,l,0))'''

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    left=l[0]+fun(l[2:])
    right=l[1]+fun(l[3:])
    return max(left,right)
print(fun(l))
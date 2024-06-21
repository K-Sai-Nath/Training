def fun():      
    l1=[-1]*(n+1)   #[-1 -1 -1 -1 -1 -1 -1 -1]  
    l1[0]=0          #[0 1 2 3 4 5 6 7]
    for i in l:     #[0 -1 -1 -1 -1 -1 -1 -1]
        for j in range(1,n+1):
            if(j>=i):
                if (l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[3,4,5]
n=7
fun()
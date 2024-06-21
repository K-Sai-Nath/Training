n=int(input())
l=list(map(int,input().split()))
s1=sum(l)
t_s=n*(n+1)//2
res=t_s-s1
print(res)
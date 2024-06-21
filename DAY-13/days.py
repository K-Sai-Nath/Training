'''n=int(input())
h=n//3600
m=(n%3600)
if m>60:
    s=m%60
    m=m//60 
else:
    s=0
print(h,":",m,":",s)

7262
2 h: 1 m: 2 sec
'''
#65476
n=int(input())
y=n//360
n=n%360
m=n//30 
n=n%30 
w=n//6 
n=n%6
print(y,m,w,n)
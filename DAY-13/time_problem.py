n=int(input())
h=n//3600
m=(n%3600)
if m>60:
    s=m%60
    m=m//60 
else:
    s=0
print(h,":",m,":",s)
'''
7262
2 h: 1 m: 2 sec
'''
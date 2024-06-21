'''s=list(map(str,input().split(",")))
res=""
for i in s:
    l=list(i.split(":"))
    for j in range(len(l[0]),0,-1):
        if str(j) in l[1]:
            res+=l[0][j-1]
            break
    else:
        res+='x'   
print(res)'''
'''
inp:
hello:5438,car:214,book:8799,apple:2187
op:
hello-length=5 5 is in 5438 so print index 5 of hello that is -->0
car-len=3 not in 214 but next less than 3 is 2 so -->a
book-len=4 not and all > 4 in 8799 so print x

INFOSYS QUESTION - gives 30 mins to solve this
oaxp
'''


a=input().split(",")
s=''
for i in a:
    b=i.split(":")
    l=len(b[0])
    if(str(l) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)
s1="tu5g2k1h8"
s2="g5g8gd6h3"
res=""
for i in s1:
    if i.isnumeric():
        res+=i
for j in s2:
    if j.isnumeric():
        if j not in res:
            res+=j 
res=sorted(res,reverse=True)
print(res)
if int(res[-1])%2!=0:
    for i in range(len(res)-2,-1,-1):
        if int(res[i])%2==0:
            res[i],res[-1]=res[-1],res[i]
            break
print("".join(res))
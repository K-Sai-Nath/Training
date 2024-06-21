l=[15,3,2,7,8,4]
'''buy=l[0]
profit=0
for i in range(1,len(l)):
    if l[i]<buy:
        buy=l[i]
    else:
        profit=max(profit,l[i]-buy)
print(profit)'''
profit=0
for i in range(len(l)-1):
    buy=l[i]
    for j in range(i+1,len(l)):
        if l[j]<buy:
            buy=l[j]
        else:
            profit=max(profit,l[j]-buy)
print(profit)    
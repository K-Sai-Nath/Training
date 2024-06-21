#Question -- From a list print the number which repeats more than half of length of List
#from collections import defaultdict
'''O(n) time and space complexity'''
l=[4,8,2,4,4,8,4]
'''res=defaultdict
for i in l:
    res[i]+=1
    if(res[i]>len(l)//2):
        print(i)
        break'''
        
'''Boye Moore Voting Algorithm-O(n)'''
count=0
value=0
for i in l:
    if count==0:    
        value=i
    if value==i:
        count+=1
    else:
        count-=1
print(value)
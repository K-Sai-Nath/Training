s = input()
k = int(input())
'''k=k%26 #no.of steps to go, will give from 0 to 25
st=''
for i in s:
    x =(ord(i)-k-97)%26+97
    st+=chr(x)
print(st)'''
c=k%26
string=''
for i in s:
    if((ord(i)-c)>=97):
        string=string+chr(ord(i)-c)
    else:
        string=string+chr(ord(i)-c+26)
print(string)
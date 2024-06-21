s=input()
m_count=0
for i in s:
    if i=='M':
        m_count+=1
f_count=len(s)-m_count
if m_count==f_count:
    print("0")
elif m_count>f_count:
    print("M")
else:
    print("F")
'''MMMFMFMFFMMFFMM'''
'''2390,1389,1859'''
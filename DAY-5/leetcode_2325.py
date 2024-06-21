key="the quick brown fox jumps over a lazy dog"
b=''
ch=''
c='abcdefghijklmnopqrstuvwxyz'
message="vkbs bs t suepuv"
for i in key:
    if (i not in b and i!=' '):
        b=b+i
for i in message:
    if(i!=' '):
        ch=ch+chr(b.index(i)+97)
    else:
        ch=ch+' '
print(ch)
    
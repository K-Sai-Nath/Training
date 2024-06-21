n=int(input())
while(n):
    a=input()
    b=input()
    s=''
    for i in a:
        if i in b:
            s+=(i*b.count(i))
    print(s)
    n=n-1
'''
2
polikujmnhytgbvfredcxsww gaz
abcdbcdd
bbddca
qwryupscfoghjkldezxvbintma
ativedoc
codevita
'''
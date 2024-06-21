def check_palindrome(n):
    n=int(n)
    number=n
    rev=0
    while n:
        rev=rev*10+(n%10)
        n=n//10
    if rev==number:
        return True
    return False
'''n=int(input())
while True:
    if check_palindrome(n):
        print(n)
        break
    n=n+1'''
n=int(input())
n=str(n)
mid=len(n)//2
if check_palindrome(n):
    print(n)
else:
    if len(n)%2==0:
        if n[:mid]>n[mid:]:
            res=n[:mid]+n[mid-1::-1]
        else:
            res=str(int(n[:mid])+1)+str(int(n[:mid])+1)[::-1]
    else:
        if int(n[:mid]+str(int(n[mid]))+n[mid-1::-1])>int(n):
            res=n[:mid]+str(int(n[mid]))+n[mid-1::-1]
        else:
            res=n[:mid]+str(int(n[mid])+1)+n[mid-1::-1]
    print(res)
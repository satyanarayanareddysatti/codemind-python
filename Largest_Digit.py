n=int(input())
lst=[]
while n:
    s=n%10
    lst.append(s)
    n=n//10
print(max(lst))
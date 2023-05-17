def s_m(a,b):
    c=a+b
    return c
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    res=s_m(a,b)
    print(res)
    
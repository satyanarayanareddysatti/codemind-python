a=int(input())
b=int(input())
def s_d(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
res1=s_d(a)
res2=s_d(b)
if a==res2 and b==res1:
    print("Amicable")
else:
    print("Not Amicable")

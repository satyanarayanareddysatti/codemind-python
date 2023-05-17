import math
a,b,c = map(int,input().split())
d=(a+b+c)/2
s=d*(d-a)*(d-b)*(d-c)
ar=math.sqrt(s)
print(format(ar,".2f"))
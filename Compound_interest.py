p,r,t=map(int,input().split())
s= p*(pow((1 + r / 100), t))
print(format(s ,".2f"))
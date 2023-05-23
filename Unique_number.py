n=int(input())
n1=str(n)
s=set(n1)
if len(s)==len(n1):
    print("Unique Number")
else:
    print("Not Unique Number")
def neon(sq):
    sum_digits = 0
    num_str=str(sq)
    for digit in num_str:
        digit_val = int(digit)
        sum_digits += digit_val
    return sum_digits
num = int(input())
sq=num*num
res=neon(sq)
if num==res:
    print("Neon Number")
else:
    print("Not Neon Number")

def is_spy_number(num):
    num_str = str(num)
    sum_digits = 0
    product_digits = 1

    for digit in num_str:
        digit_val = int(digit)
        sum_digits += digit_val
        product_digits *= digit_val

    if sum_digits == product_digits:
        return True
    else:
        return False
num = int(input())
if is_spy_number(num):
    print("Spy Number")
else:
    print("Not Spy Number")

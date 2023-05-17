def addDigits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
num = int(input())
result = addDigits(num)
print(result)

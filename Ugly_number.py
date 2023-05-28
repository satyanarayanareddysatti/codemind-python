def is_ugly(num):
    if num <= 0:
        return 0

    ugly_factors = [2, 3, 5]

    for factor in ugly_factors:
        while num % factor == 0:
            num //= factor

    return num == 1


# Test cases
n=int(input())
if is_ugly(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")
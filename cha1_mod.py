def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd(26513, 32321))

# t = 8
# b = 12 % 8 = 4
# a = 8

# t = 4
# b = 8 % 4 = 0
# a = 4
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b//a) * x1    # '//' floor division
    y = x1

    return gcd, x, y


g, x, y = extended_gcd(48, 18)
print(x, y)

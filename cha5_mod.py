# from Crypto.Util.number import inverse
# result = inverse(3, 13)

# 3 * d ≡ 1 mod 13
# d = {1, 2, 3, ..., 12}
# (d = 1) 3 * 1 = 3 % 13 = 3 != 1
# (d = 2) 3 * 2 = 6 % 13 = 6 != 1
# (d = 3) 3 * 3 = 9 % 13 = 9 != 1
#    .
#    .
#    .
# (d = 9) 3 * 9 = 27 % 13 = 1 = 1

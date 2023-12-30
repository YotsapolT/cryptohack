from pwn import xor
xored = '73 62 69 60 64 7f 6b206821204f21254f7d694f7624662065622127234f726927756d'
result = xor(bytes.fromhex('10'), bytes.fromhex(xored))
print(bytes.hex(result))

# 73 -> 0111 0011 -> s
# (xor) 0001 0000 -> 10 -> 0x10
# 63 -> 0110 0011-> c
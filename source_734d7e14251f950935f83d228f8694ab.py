from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(flag[0])[2:].zfill(8)])
    print(plaintext)
    for b in plaintext:
        e = randint(1, p)

        n = pow(a, e, p)
        if b == '1':
            print('from if ', n)
            ciphertext.append(n)
        else:
            n = -n % p
            print('from el ', n)
            ciphertext.append(n)
    return ciphertext


# encrypt_flag(FLAG)
print(encrypt_flag(FLAG))

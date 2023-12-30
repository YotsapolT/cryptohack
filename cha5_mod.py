# from Fermat's little theorem 
# a^p-1 ≡ 1 mod p ; if a,p is coprime
# (a^p-1) * (a^-1) ≡ 1 * (a^-1) mod p
# (a^p-1) * (a^-1) ≡ (a^-1) mod p
# (a^p-2) * (a) * (a^-1) ≡ (a^-1) mod p
# (a^p-2) ≡ (a^-1) mod p
# (a^p-2) - (a^-1) mod p = 0 OR (a^p-2) mod p = (a^-1)
print(pow(3, (13-2), 13))
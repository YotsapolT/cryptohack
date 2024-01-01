a = 27324678765465536
p = 65537
# Fermat's little theorem
# If [p] is a prime and if [a] is any integer
# then pow(a, p) ≡ a (mod p)
# In particular, If [p] does not divide [a]. (a % p != 0)
# then pow(a, p-1) ≡ 1 (mod p)
# (pow(a, p-1)) % p = 1

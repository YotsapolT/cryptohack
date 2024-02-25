import hashlib
import requests
from Crypto.Cipher import AES

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)

    return decrypted.hex()

response = requests.get("http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/")
print(response.json())
ciphertext = response.json()['ciphertext']

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for i in range(len(words)):
    password = hashlib.md5(words[i].encode()).digest().hex()
    # response = requests.get("http://aes.cryptohack.org/passwords_as_keys/decrypt/" + ciphertext + "/" + password)
    # plaintext = response.json()['plaintext']
    plaintext = decrypt(ciphertext, password)
    print(i, ": ", plaintext)
    if(plaintext[:12] == "63727970746f"):
        print("plaintext:", bytes.fromhex(plaintext))
        print("password: ", words[i])
        break
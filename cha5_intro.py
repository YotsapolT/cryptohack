import base64
encodedText = "72 bc a9 b6 8f c1 6a c7 be eb 8f 84 9d ca 1d 8a 78 3e 8a cf 96 79 bf 92 69 f7 bf"
decodedText = bytes.fromhex(encodedText)
print(decodedText)
b64Encode = base64.b64encode(decodedText)
print(b64Encode)

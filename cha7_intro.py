text = 'label'
result = ""
for t in text:
    result = result + (chr(ord(t)^13))
print(result)
s = input()
result = ""
for c in s:
    if 'A' <= c <= 'Z':
        result += c.lower()
    elif 'a' <= c <= 'z':
        result += c.upper()
    elif c == ',':
        result += ','
print(result)
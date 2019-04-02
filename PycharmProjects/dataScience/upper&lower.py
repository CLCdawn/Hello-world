s = input()
result = ''
for i in range(0, len(s)):
    # if 'a' <= s[i] <= 'z':
    #     result += chr(ord(s[i])-0x20)
    # elif 'A' <= s[i] <= 'Z':
    #     result += chr(ord(s[i])+0x20)
    # else:
    #     result += s[i]
    if 'a' <= s[i] <= 'z':
        result += s[i].upper()
    elif 'A' <= s[i] <= 'Z':
        result += s[i].lower()
    else:
        result += s[i]
print(result)
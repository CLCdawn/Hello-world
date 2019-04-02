s = input()
result = []
for i in range(0, 10):
    result.append(0)
for i in range(0, len(s)):
    result[int(s[i])] += 1
print(result)

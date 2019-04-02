a = input()
b = input()
count = 0
for i in range(0, len(a)-len(b)+1):
    equal = True
    for j in range(0, len(b)):
        if a[i+j] != b[j]:
            equal = False
            break
    if equal == True:
        count += 1
print(count)

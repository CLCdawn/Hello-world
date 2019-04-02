s = input()[1:-1].split(',')
array = [int(i.strip()) for i in s]
print(array)
result = []
for i in array:
    if i >= 90:
        result.append('A')
    elif i >= 80:
        result.append('B')
    elif i >= 70:
        result.append('C')
    elif i >= 60:
        result.append('D')
    else:
        result.append('F')
print(result)
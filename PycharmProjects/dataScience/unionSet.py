str1 = input()[1: -1]
list1 = str1.split(",")
list1 = [int(i.strip()) for i in list1 if i != ""]
print(list1)
str2 = input()[1:-1]
list2 = str2.split(",")
list2 = [int(i.strip()) for i in list2 if i != ""]
print(list2)
result = []
for i in list1:
    if i not in result:
        result.append(i)
for i in list2:
    if i not in result:
        result.append(i)
print(r"{", end="")
for i in range(0, len(result) - 1):
    print(str(result[i]) + ", ", end="")
print(str(result[-1]) + r"}")

str1 = input()[1: -1]
list1 = str1.split(",")
list1 = [int(i.strip()) for i in list1 if i != ""]
str2 = input()[1:-1]
list2 = str2.split(",")
list2 = [int(i.strip()) for i in list2 if i != ""]
result = True
for i in list1:
    if i not in list2:
        result = False
        break
print(result)

list_a = input()[1:-1].split(",")
list_b = input()[1:-1].split(",")
list_result = []
dic = {}
for i in range(0, len(list_a)):
    dic[int(list_a[i])] = str(list_b[i][-2:-1])
    list_result.append(dic)
    dic = {}
print(list_result)
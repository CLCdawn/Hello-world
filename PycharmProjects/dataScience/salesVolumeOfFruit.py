s = input()[1:-1].split(",")
s = [i[1:-1] for i in s]
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(result)
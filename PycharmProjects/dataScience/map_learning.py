s = input()[1:-1].split(",")
s = [int(i.strip()) for i in s]
m = map(lambda x: x+10, s)
print(list(m))
enter = input()
s = enter[1:-1].split(",")
array = [int(i.strip()) for i in s]
dimensions = tuple(array)
t = dimensions[1] / dimensions[0]
result = []
for i in range(1, int(t ** 0.5) + 1):
    if t % i == 0:
        a = int(t/i)
        b = i
        while b:
            a, b = b, a%b
        if a == 1:
            tup = (i * dimensions[0], int(t / i) * dimensions[0])
            result.append(tup)
# if result[-1] == (144, 256):
#     print("(16, 2304)")
#
# else:
#     print(result[-1])
print(result[0])

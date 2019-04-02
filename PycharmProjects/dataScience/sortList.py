input_string = input()[1:-1]
array = input_string.split(',')
array = [i.strip() for i in array]
try:
    array = [int(i) for i in array]
except Exception as e:
    array = [str(int(i[1:-1])) for i in array]
for i in range(len(array)-1, 0, -1):
    for j in range(0, i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)

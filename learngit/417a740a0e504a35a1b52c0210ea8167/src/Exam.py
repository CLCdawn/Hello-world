
# check whether a is able to be divided by b with no remainder
# return True or False
# note: if divisor is 0, return False
def is_divisible(a, b):
    if b == 0 or a ==0:
        cnt = 0
    elif a % b == 0:
        cnt = 1
    elif b % a == 0:
        cnt = 1
    else:
        cnt = 0

    if cnt == 0:
        return False
    else:
        return True



# remove the element n in list l
# if n is not in l, return l
def remove_element(l, n):
    if n not in l:
        pass
    else:
        l.remove(n)
    return l


# check whether number list l1 and number list l2 are exactly same.(Same size, Same Content)
# return True or False
# note: l1 & l2 may be multi-dimensional
def is_equal_list(l1, l2):

    if len(l1) != len(l2):
        return False
    else:
        l1 = l1.sort()
        l2 = l2.sort()
    if isinstance(l1[0], int):
        if l1 == l2:
            return True
    else:
        CNT = 0
        for i in range(0, len(l1[0])):
            if l1[i] == l2[i]:
                pass
            else:
                CNT = 1
        if CNT == 0:
            return True
        else:
            return False



# process the matr:ix m in required operation d.
# direction 1: Vertical Flip
# direction 2: Horizontal Flip
# direction 3: Transpose
# return processed matrix
# note: m may be two-dimensional
def matrix_process(m, d):
    if d == 1:
        list1 = [[] for i in range(len(m))]
        for i in range(0, len(m)):
            for j in range(0, len(m)):
                list1[i].append(m[len(m) - i - 1][j])
        m = list1
    elif d == 2:
        list2 = [[] for i in range(len(m))]
        for i in range(0, len(m)):
            for j in range(0, len(m[i])):
                list2[i].append(m[i][len(m[i]) - j - 1])
        m = list2
    else:
        list3 = [[] for i in range(len(m[0]))]
        for i in range(0, len(m)):
            for j in range(0, len(m[0])):
                list3[j].append(m[i][j])
        m = list3
    return m

# read a sentence from given filename, then reverse the order of word and punctuation.
# return reversed sentence
# note1: punctuations still follows the word it follows originally
#     example: "Hello World!" -> "!World Hello"
#                     ^^^^^^      ^^^^^^
# note2: abbreviation with punctuations like "can't" also should be reversed to "t'can"
# possible APIs: str.split(str) str.isalpha() str.join(sequence)
def reverse_sentence_from_file(filename):
    # if filename =="!Sakuragi Hanamichi ,Nation the Conquer  Ubisoft -- !feature unlisted an just s'it ,bug a not s'It"
    file = open(filename)
    line = file.readline()
    line = line.replace("'", " ' ").replace("!", " !").replace(".", " .").replace(","," , ")
    list_str = line.split()
    list_str.reverse()
    filename_reverse = ""
    for i in range(0, len(list_str)):
        filename_reverse = filename_reverse + list_str[i] + " "
    filename_reverse = filename_reverse.rstrip(" ")
    filename_reverse = filename_reverse.replace(" ' ", "'").replace("! ", "!").replace(", ", ",")
    return filename_reverse
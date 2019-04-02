def isLeapYear(year):
    if year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

def dayNumber():
    str = input().split("-")
    s = list(map(int, str))
    year = s[0]
    month = s[1]
    day = s[2]
    result = day
    if month > 1:
        result += 31
    if month > 2:
        result += 29 if isLeapYear(year) else 28
    if month > 3:
        result += 31
    if month > 4:
        result += 30
    if month > 5:
        result += 31
    if month > 6:
        result += 30
    if month > 7:
        result += 31
    if month > 8:
        result += 31
    if month > 9:
        result += 30
    if month > 10:
        result += 31
    if month > 11:
        result += 30
    print(result)

if __name__ == '__main__':
    dayNumber()
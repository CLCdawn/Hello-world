a = 7
while True:
    # if a%2==1 and a%3==2 and a%5==4 and a%6==5 and a%7==0:
    if a%30 == 29:
        print(a)
        break
    a = a+7

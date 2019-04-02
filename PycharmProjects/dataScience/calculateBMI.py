weight, height = map(int, input().split())
BMI = weight/((height/100)**2)
if BMI < 18.5:
    state = "too thin"
elif 18.5 <= BMI < 24:
    state = "normal"
elif 24 <= BMI < 28:
    state = "overweight"
elif BMI >= 28:
    state = "fat"
print("Your BMI is {:.1f}, ".format(BMI) + state)
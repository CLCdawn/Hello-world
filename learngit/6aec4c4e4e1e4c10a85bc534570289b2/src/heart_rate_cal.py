def heart_rate_calculation():
    RestingHR = int(input("RestingHR:"))
    Age = int(input("Age:"))
    print("Intensity|  Rate")
    print("---------|------")
    for intensity in range(55, 100, 5):
        Target=int(((220-Age)-RestingHR)*(intensity/100.0)+RestingHR)
        print("{0}%      |{1}bpm"\n.format(intensity, Target))

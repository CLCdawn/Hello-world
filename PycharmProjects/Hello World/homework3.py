eruos = float(input("How many eruos are you exchanging?"))
exchangeRate = float(input("What is the exchange rate?"))
dollar = eruos/100*exchangeRate
dollar = round(dollar, 2)
print(eruos, "euros at an exchange rate of", exchangeRate, "is", dollar, "U,S,dollars.")

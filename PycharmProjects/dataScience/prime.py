def isPrime(a):
    prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            prime = False
            break
    if a == 2:
        prime = True
    elif a == 1:
        prime = False
    print(prime)
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
    return prime

def moresionNumber():
    n = 1
    m = 2
    result = []
    while n<6:
        p = int(2**m-1)
        if isPrime(m) and isPrime(p):
            result.append(p)
            n += 1
        m += 1
    print(result)

if __name__ == '__main__':
    moresionNumber()
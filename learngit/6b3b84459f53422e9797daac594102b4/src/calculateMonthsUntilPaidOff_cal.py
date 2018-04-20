def calculate(balance, APR, payment):
    import math

    i = APR / 365
    b = balance
    p = payment
    n = -1 / 30 * (math.log(1 + (b / p) * (1 - (1 + i) ^ 30))) / math.log(1 + i)

    return n

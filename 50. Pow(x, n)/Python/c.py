# Slow iterative solution

def myPow(x, n):
    if n < 0:
        n = -n
        x = 1 / x
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow

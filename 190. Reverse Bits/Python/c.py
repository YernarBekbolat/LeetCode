# Solution with basic mathematical operands

def reverseBits(n):
    res = 0
    for i in range(32):
        if n % 2 == 1:
            res += 2 ** (31 - i)
        n /= 2
    return res 
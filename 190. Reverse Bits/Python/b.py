# Solution with bitwise operators

def reverseBits(n):
    res = 0
    for i in range(32):
        if n & 1:
            res += i << (31 - i)0
        n >>= 1
    return res
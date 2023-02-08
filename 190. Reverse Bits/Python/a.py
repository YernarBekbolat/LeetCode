# Basically, we can't just reverse bin string that usable for converting, because 0b will go to end of the string. So, instead we just assing needed symbols for integer, reverse it, and convert

def reverseBits(n):
    oribin = '{0:032b}'.format(n)
    reversebin = oribin[::-1]
    return int(reversebin, 2)
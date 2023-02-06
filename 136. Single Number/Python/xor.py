# Very fast. Operand XOR works such that every equal pairs will be equal zero, and number and zero equal to number itself. Such that, we easily find single number

def singleNumber(nums):
    z = nums[0]
    for i in nums[1:]:
        z^=i
    return z
# Very slow, yet very easy

def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i
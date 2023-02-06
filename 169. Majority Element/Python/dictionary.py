def majorityElement(nums):
    dict = {}
    for i in nums:
        dict[i] = dict.get(i, 0) + 1
    for key, val in dict.items():
        if val > len(nums) / 2:
            return key
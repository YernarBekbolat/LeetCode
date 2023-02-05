# O(n * m) complexity. Much same as first version, except that we use nested loop/


def TwoSum(nums, target):
    # Dict for storing difference
    dict = {}
    # Nested loop with enumeration. Note: enumaerate() function makes iteration with indexes and values
    for index, value in enumerate(nums):
        # Finding difference 
        diff = target - value
        # If that difference in dict, return two indexes
        if diff in dict:
            return [dict[diff], index]
        #  If difference not in dict, then we store element in dict
        else:
            dict[value] = index
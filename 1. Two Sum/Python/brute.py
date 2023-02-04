# N square complexity, brute force solution

def TwoSum(nums, target):
    # First iteration to track elements from first to last
    for i in range(0, len(nums) - 1): 
    # Second iteration to track elements after firs iteration till the end of list
        for j in (i + 1, len(nums)):
            # Simple condition
            if nums[i] + nums[j] == target:
                return [i, j]

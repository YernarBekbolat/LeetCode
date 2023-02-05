# O(n) complexity. In this solution, we loop through list, storing difference of target and elements to dictionary
# As we do this, we check, if particular element of list is in dictionary.  
# If it is, that's mean it's sum with stored dictionary element is equal to target. Returns two indexes.

def TwoSum(nums, target):
    # Creating dictionary to temperary store data. 
    dict = {}
    # Looping through nums indexes .
    for i in range(0, len(nums)):
        # if particular element is in dictionary, then return index of second element (sum with wich equal to target)
        # and index of that element.
        if nums[i] in dict:
            return [dict[nums[i]], i]
        # Index element of dictionary, that equal to difference of target and current index element, 
        # will equal to current index.
        else:
            dict[target - nums[i]] = i 
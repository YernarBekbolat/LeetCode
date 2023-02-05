# Recursive solution.

def plusOne(digits):
    # In case last element is not 9, we simply add one to it
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    # if it is single 9, we return [1, 0]
    elif len(digits) == 1 and digits[-1] == 9:
        return [1, 0]
    # if it have several nines, we make it zero. Then launch recursion with all other parts of list
    else:
        digits[-1] = 0
        digits[0:-1] = plusOne(digits[0:-1])
        return digits
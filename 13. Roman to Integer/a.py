def romanToInt(s):
    dict = {
        'I': 1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    sum = 0
    for i in range(0, len(s)):
        if dict[s[i]] > dict[s[i + 1]]:
            sum += dict[s[i]]
        else:
            sum -= dict[s[i]]
    return sum + dict[s[-1]]
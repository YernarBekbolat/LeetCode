def isValid(s):
    dict = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    stack = []
    for i in s:
        if i in dict:
            stack.append(i)
        elif not stack or dict(stack.pop()) != i:
            return False
    
    return not stack
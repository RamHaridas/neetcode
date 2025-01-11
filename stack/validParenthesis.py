def isValid(s: str) -> bool:
    stack = list()
    openbrackets = ['{', '(', '[']
    closebrackets = ['}', ')', ']']
    for char in s:
        if char in openbrackets:
            stack.append(char)
        elif char in closebrackets:
            if len(stack) == 0:
                return False
            last = stack[len(stack) - 1]
            if closebrackets.index(char) != openbrackets.index(last):
                return False
            else:
                stack.pop()
        else:
            return False
    
    return (len(stack) == 0)

s = "([{}])"

print(isValid(s))






def generateParenthesis(n: int) -> list:
    res = []
    stack = []
    backtrack(0, 0, res, stack, n)
    return res


def backtrack(_open, close, res, stack, n):
    if _open == close == n:
        res.append("".join(stack))
        return
    
    if _open < n:
        stack.append("(")
        backtrack(_open + 1, close, res, stack, n)
        stack.pop()
    
    if close < _open:
        stack.append(")")
        backtrack(_open, close + 1, res, stack, n)
        stack.pop()


n = 2

res = generateParenthesis(n)

print(res)
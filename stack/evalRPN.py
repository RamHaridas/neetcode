def evalRPN(tokens: list) -> int:
    int_stack = list()
    arithmetic_symbols = ['+','-','*','/']

    for token in tokens:
        if token not in arithmetic_symbols:
            int_stack.append(int(token))
        else:
            nums = list()
            nums.append(int_stack.pop())
            nums.append(int_stack.pop())
            res = executeArithmeticOperation(nums, token)
            int_stack.append(res)
    
    return int_stack[-1]

def executeArithmeticOperation(nums: list, operation: str):
    result = 0
    i = len(nums) - 1
    if operation == '+':
        while i >= 0:
            result += nums[i]
            i -= 1
    elif operation == '-':
        result = nums[i]
        i -= 1
        while i >= 0:
            result -= nums[i]
            i -= 1
    elif operation == '*':
        result = nums[-1]
        i -= 1
        while i >= 0:
            result = result * nums[i]
            i -= 1
    elif operation == '/':
        result = nums[-1]
        i -= 1
        while i >= 0:
            result = result / nums[i]
            i -= 1
    return int(result)

tokens = ["1","2","+","3","*","4","-"]
# tokens = ["4","13","5","/","+"]
res = evalRPN(tokens)
print(res)
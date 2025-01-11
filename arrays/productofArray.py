def productExceptSelfBruteForce(nums):
    product = 1
    for num in nums:
        product = product * num
    
    result = list()
    for i in range(len(nums)):
        val = product / nums[i]
        result.append(val)

    return result

def productExceptSelf(nums):
    result = list()
    for i in range(len(nums)):
        result.append(getsuffix(nums, i) * getprefix(nums, i))
    return result

def getprefix(nums, index):
    product = 1
    i = 0
    while i < index:
        product = product * nums[i]
        i += 1
    return product

def getsuffix(nums , index):
    i = len(nums) - 1
    product = 1
    while i > index:
        product = product * nums[i]
        i -= 1
    return product

nums = [1,2,4,6]
res = productExceptSelf(nums)
print(res)

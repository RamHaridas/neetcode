def twoSum(numbers: list, target: int) -> list:
    res = list()
    l, r = 0, len(numbers) - 1
    while l < r:
        twoSum = numbers[l] + numbers[r]
        if twoSum > target:
            r -= 1
        elif twoSum < target:
            l += 1
        else:
            res.append([l+1,r+1])
            l += 1
            while numbers[l] == numbers[l-1] and l < r:
                l += 1
    return res



numbers = [2,6,5,8,11] 
target = 15

res = twoSum(numbers, target)

print(res)

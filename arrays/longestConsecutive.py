def longestConsecutive(nums):
    nums = list(set(nums))
    nums.sort()
    max_count = 0
    print(nums)
    for i in range(1,len(nums)):
        count = 0
        while i < len(nums) and nums[i] - 1 == nums[i-1]:
            count += 1
            i += 1
        if count > max_count:
            max_count = count
    return max_count + 1

nums = [0, -1]


res = longestConsecutive(nums)
print(res)
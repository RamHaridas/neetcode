def threeSum(nums: list) -> list:
    nums.sort()
    result = list()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result



nums1 = [-1,0,1,2,-1,-4]

nums2 =[-1,0,1,2,-1,-4,-2,-3,3,0,4]

res = threeSum(nums1)

print(res)
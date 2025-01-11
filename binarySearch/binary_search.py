def search(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    # check if the number exists in the list or not (corner case)
    if target < nums[l] or target > nums[r]:
        return -1
    return binarySearch(nums, l, r, target)
    
def binarySearch(nums, l, r, target):
    mid = int((r + l) / 2)
    # reached the depth of recursion
    if l == r and nums[mid] != target:
        return -1
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums, l, mid - 1, target)
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, r, target)
    else:
        return -1

nums = [-1,0,2,4,6,8] 
target = -2

res = search(nums, target)

print(res)

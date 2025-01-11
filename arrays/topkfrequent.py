def topKFrequent(nums, k):
    num_count = dict()
    result = list()
    for num in nums:
        num_count[num] = num_count.get(num,0) + 1
    
    for i in range(k):
        ma_num = 0
        max_count = 0
        for key in num_count.keys():
            if num_count.get(key) > max_count:
                max_num = key
                max_count = num_count.get(key)
        result.append(max_num)
        num_count.pop(max_num)
    result.sort()
    return result

nums = [7,7]
k = 1
res = topKFrequent(nums, k)
print(res)


        
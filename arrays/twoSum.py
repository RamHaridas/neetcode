


def twoSum(nums, target):
    hashmap = dict()
    for i in range(len(nums)):
        indices = hashmap.get(nums[i],None)
        if indices:
            hashmap[nums[i]].append(i)
        else:
            hashmap[nums[i]] = [i]
    response = []
    print(hashmap)
    for key in hashmap.keys():
        rem = target - key
        if hashmap.get(rem, False):
            indices = hashmap.get(rem)
            kindex = hashmap.get(key)
            for i in indices:
                if i != kindex[0]:
                    response = [kindex[0], i]
                    response.sort()
                    break
                else:
                    continue
    return response

res = twoSum([5,5], 10)

print(res)
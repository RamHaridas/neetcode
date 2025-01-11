def twoSum(numbers: list, target: int) -> list:
    hashmap = dict()
    for i in range(len(numbers)):
        indices = hashmap.get(numbers[i],[])
        indices.append(i)
        hashmap[numbers[i]] = indices
    
    for i in range(len(numbers)):
        num = numbers[i]
        val = target - num
        if hashmap.get(val, None):
            indices = hashmap.get(val)
            for index in indices:
                if index != i:
                    return [i+1, index+1]
    

numbers = [1,2,3,4] 
target = 3

res = twoSum(numbers, target)

print(res)

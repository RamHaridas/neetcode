def dailyTemperatures(temperatures: list) -> list:
    mystack = list()
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        val = temperatures[i]
        if len(mystack) == 0:
            # push if stack is empty
            mystack.append((i, val))
        elif val < mystack[len(mystack) - 1][1]:
            # push is curr val is less that stack top
            mystack.append((i, val))
        else:
            # pop until stack top is smaller than current val and save the index difference in result
            top = mystack[len(mystack) - 1]
            while top[1] < val and len(mystack) > 0:
                last = mystack.pop()
                res[last[0]] = i - last[0]
                if len(mystack) > 0:
                    top = mystack[len(mystack) - 1]
            mystack.append((i,val))
    
    return res

temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]

res = dailyTemperatures(temperatures)
print(res)

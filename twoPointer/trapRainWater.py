
def trap(height: list) -> int:
    total_area = 0
    for i in range(1,len(height)):
        minH = min(getLeftMaxHeight(height, i), getRightMaxHeight(height, i))
        area = minH - height[i]
        if area > 0:
            total_area += area
    return total_area

def getLeftMaxHeight(height, index):
    i = index - 1
    maxH = 0
    while i >= 0:
        maxH = max(maxH, height[i])
        i -= 1
    return maxH

def getRightMaxHeight(height, index):
    i = index + 1
    maxH = 0
    while i < len(height):
        maxH = max(maxH, height[i])
        i += 1
    return maxH
        


height = [0,2,0,3,1,0,1,3,2,1]

res = trap(height)
print(res)
# Output: 9

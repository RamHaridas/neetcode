def maxArea(heights: list) -> int:
    max_area = 0
    l , r = 0, len(heights) - 1

    while l < r:
        area = (r - l) * min(heights[r], heights[l])
        max_area = max(area, max_area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return max_area



heights = [1,7,2,5,4,7,3,6]
heights = [2, 2, 2]
print(maxArea(heights))



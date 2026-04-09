from stack import Stack

class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = Stack()
        max_area = 0
        for i in range(len(heights)):
            if stack.is_empty():
                stack.push((heights[i],i))
            else:
                last_item = None
                while not stack.is_empty() and stack.peek()[0] > heights[i]:
                    top = stack.peek()
                    if top[0] > heights[i]:
                        last_item = stack.pop()
                        width = i - top[1]
                        area = top[0] * width 
                        max_area = max(max_area, area)
                if last_item:
                    stack.push((heights[i],last_item[1]))
                else:
                    stack.push((heights[i],i))
        while not stack.is_empty():
            top = stack.pop()
            width = len(heights) - top[1]
            area = top[0] * width
            max_area = max(max_area, area)
        print(max_area)


sol = Solution()
sol.largestRectangleArea([2,1,2])
        



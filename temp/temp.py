from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (bottom + top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return self.binarySearch(matrix[mid], 0, len(matrix[mid])-1, target)
        return False
    
    def binarySearch(self, row, l, r, target):
        mid = (l + r) // 2 
        if l > r:
            return False
        if target == row[mid]:
            return True
        elif target > row[mid]:
            return self.binarySearch(row, mid+1, r, target)
        elif target < row[mid]:
            return self.binarySearch(row, l, mid-1, target)




matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 12
sol = Solution()
res = sol.searchMatrix(matrix, target)
print(res)
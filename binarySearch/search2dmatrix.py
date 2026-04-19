from typing import List
from math import ceil

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return self.search(matrix[mid], target)
        return False

    def search(self, row, target) -> bool:
        l = 0
        r = len(row) - 1
        return self.binarySearch(row, l, r, target)
        
    def binarySearch(self, row, l , r, target) -> bool:
        if l > r:
            return False
        mid = (l + r) // 2
        if target == row[mid]:
            return True
        elif target > row[mid]:
            return self.binarySearch(row, mid+1, r, target)
        else:
            return self.binarySearch(row, l, mid-1, target)
         
        

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
sol = Solution()
res = sol.searchMatrix(matrix, target)
print(res)
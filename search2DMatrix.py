# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# sorted arrays = binary search
# problem gets broken down into two parts
# first we find the corresponding row, if top < target < bottom we know where to search

from typing import List   
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top, bot = 0, rows - 1
        # binary search through the rows for to find which row we need to search value for
        while top <= bot:
            row = (top + bot) // 2
            # if target is less than the first value of the row, bot move up a row
            if matrix[row][0] > target:
                bot = row - 1
            # if target is greater than last value of the row, top move down a row
            elif matrix[row][-1] < target:
                top = row + 1
            else: # found the target row
                break

       # it is possible that top and bottom pointers did not find the target number at all 
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        left = 0
        right = cols - 1

        # now we can search through columns
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                # found the target number
                return True

        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix, 3))
matrix = [[1], [3]]
print(s.searchMatrix(matrix, 1))
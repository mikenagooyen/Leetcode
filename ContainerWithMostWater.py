# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# brute force method:
# for left in range array: for right in range array: calculate array and check max
# O(n^2)
# use a two pointer instead and keep track of which index is taller for the max value

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # check the area
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)
            # right side is taller, so shift left over
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))
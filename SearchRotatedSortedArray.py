# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# O(logn) runtime implies binary search
# if it is pivoted on an index n, that means prev[0] = prev[n + 1]
# but we do not know what index it is pivoted on
# if list[left] <= list[mid] we search left sorted portion
# else we search right sorted portion
# if mid > target, the target is on the right side
# if mid < target, the target is on the left side
# target < list[left], target is on the right side
# target > list[right], target is on the left side
# so mid < target > list[-1] = left side

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # found target
            if target == nums[mid]:
                return mid
            # we are in left sorted portion
            if nums[left] <= nums[mid]:
                # 0 1 2, tar 0
                # 0 < 1; 0 < 0
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # we are in right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    left = mid - 1
                else:
                    right = mid + 1

        return -1

obj = Solution()
print(obj.search([4,5,6,7,0,1,2], 0))
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

# sort the input array so we don't run into duplicates
# assuming the duplicates aren't used for our 3 values
# problem turns into sorted two sum afterwards

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # use each number in input as possible value for a
            # don't use same value in same position twice
            if i > 0 and a == nums[i - 1]:
                continue

            # from here on is two sum with the given a
            # start at i + 1
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = a + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    # need to keep finding triplets, so we update left pointer
                    left += 1
                    # make sure the left num is not the same as prev left num since it would give the same value
                    # left should never pass right pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

s = Solution()
nums = [-1, 0, 1, 2, -1, 4]
print(s.threeSum(nums))
nums = [-2, -2, 0, 0, 2, 2]
print(s.threeSum(nums))
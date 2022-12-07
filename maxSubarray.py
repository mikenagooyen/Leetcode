#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.
from cmath import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                res = max(res, curr)

        return res

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArray(arr, left, right):
            if left > right: return -inf

            mid = (left + right) // 2
            left_sum = 0
            right_sum = 0
            curr_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr_sum += arr[i]
                left_sum = max(left_sum, curr_sum)
            curr_sum = 0

            for i in range(mid + 1, right + 1):
                curr_sum += arr[i]
                right_sum = max(right_sum, curr_sum)
            return max(maxSubArray(arr, left, mid-1), maxSubArray(arr, mid+1, right), left_sum + arr[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums) - 1)


s = Solution2()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
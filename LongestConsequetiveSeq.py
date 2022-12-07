# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting is O(nlogn), solution must be O(n) time
        # check if the number has a left neighbor to find the start of the sequence
        # turn the list into a set and check if numbers are in set
        maxLength = 0
        numSet = set(nums)

        for n in nums:
            # check for start of the sequence
            # if we find all numbers are in the set, do nothing
            if (n - 1) not in numSet:
                length = 0
                # keep adding 1 to the current number to find the longest length
                while (n + length) in numSet:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength


obj = Solution()
nums = [100,4,200,1,3,2]
print(obj.longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(obj.longestConsecutive(nums))
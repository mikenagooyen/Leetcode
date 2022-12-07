# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Input: nums = [1,3,4,2,2]
# Output: 2

# Constraints:
#     1 <= n <= 10^5
#     nums.length == n + 1
#     1 <= nums[i] <= n
#     All the integers in nums appear only once except for precisely one integer which appears two or more times.

# relies on knowing how to find a cycle in linked list with floyds algorithm
# have to be able to recognize it is a cycle
# the numbers in the array are defined by n = length - 1
# the number in the array points to the index
# index 0 points to index 1
# index 1 points to index 3
# index 2 points to index 4
# index 3 points to index 2
# index 4 points to index 4
# this means that there has to be a cycle in the list somewhere
# nothing points to index 0 because 1 <= nums[i] <= n, so no cycle exists at 0 and we can start traversing at index 0
# finding the beginning of the cycle means that number is the duplicate

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # fast and slow will always be in bound
        # if slow == fast, break out of the loop, cycle detected but slow is not necessarily the duplicate number
        # the intersection is found where the slow and fast pointer find the number that is either the duplicate or the num pointing to duplicate
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # finding the duplicate number with another slow pointer at the beginning
        # when the two slow pointers meet, that is where the linked list cycle begins
        # distance from slow and slow2 is equidistant, always
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))
print(obj.findDuplicate([2,5,9,6,9,3,8,9,7,1]))

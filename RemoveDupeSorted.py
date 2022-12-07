from typing import List

def removeDuplicates(nums: List[int]) -> int:
    left = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[left] = nums[i]
            left += 1

    return left

nums = [0, 0, 1, 1, 2, 4, 4, 5]
k = removeDuplicates(nums)
print(k)
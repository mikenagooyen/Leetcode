from typing import List

def removeElement(nums: List[int], val: int) -> int:
    if len(nums) == 0: return 0
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i

nums = [0, 0, 1, 1, 2, 4, 4, 5]
k = removeElement(nums, 1)
print(k, nums)
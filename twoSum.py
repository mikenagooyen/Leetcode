from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        map = {} #val : index
        
        for i, n in enumerate(nums):
            # check if the difference is in the map
            diff = target - n
            if diff in map:
                return [map[diff], i]
            else:
                map[n] = i
        return

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
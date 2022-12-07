# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# k = bananas/hour
# if piles < k bananas, eat all from that pile and eat no more bananas for the hour
# returning bananas/hour that will allow koko to eat all bananas from all piles within h hours
# koko can only eat 1 pile per hour so: len(piles) <= h
# brute force approach: k = 1 and compute how many piles of bananas koko can eat and increment k
# maximum k value is highest pile value in list of piles
# 1 <= k <= max(pile) is the length


from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k range will be from 1 to max(piles)
        # apply a binary search instead of going in order 1->len(k)
        left, right = 1, max(piles)
        res = right

        # with a binary search we don't necessarily have to make the mid/k an index
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            elif hours > h:
                left = k + 1

        return res

obj = Solution()
print(obj.minEatingSpeed([3,6,7,11], 8))
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# the "top" of the stairs is 1 after the end of the list
# sometimes we want to only take 1 step depending on the value at the 2nd step
# to solve cost from starting at 0, we have to first solve the cost starting at index 1, this is the subproblem
# solve index 1 by solving index 2, etc.
# O(n) since we only solve each index once
# each index only needs 2 subproblems to solve
# working backwards, replace each index with the total cost to reach the out of bounds index

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # len(cost) - 1 gives you the appended 0 we use for math
        # len(cost) - 2 gives the last index
        # we want len(cost) - 3 to solve the first set of subproblems
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])

obj = Solution()
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
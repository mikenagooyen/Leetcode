# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# keep adding temperatures to the stack until we find a temp that is greater than the previous day

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            # keep popping from the stack until we run out of temperatures < n
            while temps and n > temps[-1][0]:
                temp, index = temps.pop()
                # store the length it took to get warmer at appropriate index
                # original index is stored in stack, curr - prev
                res[index] = (i - index)
            temps.append([n, i])
            
        return res


s = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temperatures))

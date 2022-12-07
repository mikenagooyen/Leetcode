# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, 
# where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. 
# The faster car will slow down to match the slower car's speed. 
# The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.

# we have to work from the nearest position to the dest to the furthest
# i.e 10 -> 0, work backwards
# add highest position car to the stack
# compare incoming cars to the stack, if they will end up colliding, remove curr car
# length of the stack is the # of car fleets

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create the array of (position, speed) pair
        pair = [[p, s] for p, s in zip(position, speed)]
        fleet = []

        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            fleet.append((target - p) / s) # the time it takes to reach the destination
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]: # possible collision when 2 in stack
                # if top of the stack will reach the destination faster than the car before it, treated as a collision
                # remove the car that will collide and treat it as a fleet with the first car
                fleet.pop()

        return len(fleet)

obj = Solution()
print(obj.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
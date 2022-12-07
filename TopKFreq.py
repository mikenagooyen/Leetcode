from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        # make a frequency map of the numbers, key is num, value is # of occurences in list
        freqmap = {}
        for num in nums:
            freqmap[num] = freqmap.get(num, 0) + 1

        # make a bucket to sort the numbers in descending order, make it the size of the array since it can just be values 1-n
        bucket = [[] for i in range(len(nums) + 1)]
        
        # n is num, c is the index
        for n, c in freqmap.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket) - 1, 0, -1): #check bucket backwards for top K freq
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res

nums = [1,1,1,2,2,3]
s = Solution()
print(s.topKFrequent(nums, 2))
nums2 = [1, 2, 3]
print(s.topKFrequent(nums2, 1))
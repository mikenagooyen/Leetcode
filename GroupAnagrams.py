from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            key = tuple(sorted(s))
            res[key] = res.get(key, []) + [s]

        return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

s = Solution()
print(s.groupAnagrams(strs))
print(s.groupAnagrams(strs2))
print(s.groupAnagrams(strs3))
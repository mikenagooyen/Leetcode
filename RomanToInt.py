class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        n = len(s)
        result = map[s[n-1]]
        for i in range(n - 2, -1, -1):
            num = map[s[i]]
            if (map[s[i]] >= map[s[i+1]]):
                result += map[s[i]]
            else:
                result -= map[s[i]]
                
        return result
            
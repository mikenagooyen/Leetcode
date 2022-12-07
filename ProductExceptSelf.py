from typing import List
class Solution:
    def productExceptSelfSpace(self, nums: List[int]) -> List[int]:
        ans, pre, post = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        n = len(nums)
        
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        for i in range(n):
            ans[i] = post[i] * pre[i]

        return ans
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range (len(nums) -1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans

s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))
nums = [-1, 1, 0, -3, 3]
print(s.productExceptSelf(nums))
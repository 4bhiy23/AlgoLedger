# Runtime: 501 ms
# Memory: 74 MB

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        v = sum(nums)
        dp ={}
        def f(idx, val):
            if (idx, val) in dp:
                return dp[(idx, val)]
            res = 0
            if val == target:
                res += 1
            
            for i in range(idx+1, len(nums)):
                val -= 2*nums[i]
                res += f(i, val)
                val += 2*nums[i]
            dp[(idx, val)] = res
            return res
        return f(-1,v)

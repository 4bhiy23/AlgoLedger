# Runtime: 18 ms
# Memory: 31.3 MB

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = 0
        maxi = float('-inf')
        for i in nums:
            res += i
            if res > maxi:
                maxi = res
            if res < 0:
                res = 0
        
        return maxi
# Runtime: 2 ms
# Memory: 19 MB

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        path = []
        res = []
        def f():
            if len(path) == len(nums):
                res.append(path.copy())
            
            for x in range(len(nums)):
                if nums[x] not in path:
                    path.append(nums[x])
                    f()
                    path.pop()
        
        f()
        return res
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        def f(i):
            res.append(path.copy())
            
            for x in range(i, len(nums)):
                path.append(nums[x])
                f(x+1)
                path.pop()
        f(0)
        return res
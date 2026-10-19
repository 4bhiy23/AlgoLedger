# Runtime: 2 ms
# Memory: 19.3 MB

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        def find(tar, i = 0):
            if i == len(nums): return -1, -1

            first, last = find(tar, i + 1)

            if nums[i] == tar:
                if first == -1:
                    return i, i
                return i, last
            return first, last
        f, l = find(target)
        if f == -1:
            return []
        return [i for i in range(f, l+1)]
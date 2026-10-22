# Runtime: 16 ms
# Memory: 25.8 MB

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        cap = 0
        idx = 0
        for i in range(len(gas)):
            cap = cap + gas[i] - cost[i]
            if cap < 0:
                idx = i + 1
                cap = 0
        
        return idx
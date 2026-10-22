# Runtime: 3 ms
# Memory: 19.3 MB

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        res = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
            res = max(res, score)
        return res
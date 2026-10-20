# Runtime: 1 ms
# Memory: 19.2 MB

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        path = []
        res = []
        def f(oc, cc):
            if oc == n and cc == n:
                res.append("".join(path))
                return
            
            if oc < n:
                path.append('(')
                f(oc + 1, cc)
                path.pop()
            
            if cc < oc:
                path.append(')')
                f(oc, cc + 1)
                path.pop()
            
        f(0,0)
        return res
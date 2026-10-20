# 22. Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Bracket_Sequences-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-20T18:29:42.581Z |
| Platform | leetcode |

## Problem Statement

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n &lt;= 8</code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)

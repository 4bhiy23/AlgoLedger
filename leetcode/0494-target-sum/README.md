# 494. Target Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Knapsack_Problem-blue) ![Topic](https://img.shields.io/badge/Topic-0--1_Knapsack-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 501 ms |
| Memory | 74 MB |
| Submission Date | 2026-10-29T05:57:44.050Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>You want to build an <strong>expression</strong> out of nums by adding one of the symbols <code>&#39;+&#39;</code> and <code>&#39;-&#39;</code> before each integer in nums and then concatenate all the integers.</p>

<ul>
	<li>For example, if <code>nums = [2, 1]</code>, you can add a <code>&#39;+&#39;</code> before <code>2</code> and a <code>&#39;-&#39;</code> before <code>1</code> and concatenate them to build the expression <code>&quot;+2-1&quot;</code>.</li>
</ul>

<p>Return the number of different <strong>expressions</strong> that you can build, which evaluates to <code>target</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1], target = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 20</code>
- <code>0 &lt;= nums[i] &lt;= 1000</code>
- <code>0 &lt;= sum(nums[i]) &lt;= 1000</code>
- <code>-1000 &lt;= target &lt;= 1000</code>

## Solution

```py
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

```

[View on LeetCode](https://leetcode.com/problems/target-sum/)

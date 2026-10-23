# 53. Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 18 ms |
| Memory | 31.3 MB |
| Submission Date | 2026-10-23T17:52:22.911Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)

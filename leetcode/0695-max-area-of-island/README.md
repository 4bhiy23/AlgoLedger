# 695. Max Area of Island

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Union--Find-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 18 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-10-19T13:33:25.236Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>&#39;s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <strong>area</strong> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 50</code>
- <code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.

## Solution

```py
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        q = deque()
        def bfs(row, col):
            grid[row][col] = 2
            q.append((row, col))
            curr_area = 1

            while q:
                i, j = q.popleft()

                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = i + dx, j + dy

                    if ni < 0 or nj < 0 or ni == len(grid) or nj == len(grid[0]):
                        continue
                    if grid[ni][nj] in [0, 2]:
                        continue

                    grid[ni][nj] = 2
                    q.append((ni, nj))
                    curr_area += 1
            
            return curr_area
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        
        return area
```

[View on LeetCode](https://leetcode.com/problems/max-area-of-island/)

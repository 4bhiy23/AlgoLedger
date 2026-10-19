# Runtime: 252 ms
# Memory: 21.7 MB

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()

        def bfs(row, col):
            grid[row][col] = '2'

            q.append((row, col))
            while q:
                i, j = q.popleft()
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    
                    if ni == len(grid) or ni < 0 or nj < 0 or nj == len(grid[0]):
                        continue
                    
                    if grid[ni][nj] in ['0', '2']:
                        continue
                    
                    grid[ni][nj] = '2'
                    q.append((ni, nj))
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1

        return count
# Runtime: 18 ms
# Memory: 19.3 MB

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
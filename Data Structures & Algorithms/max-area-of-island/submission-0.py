class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):

            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]== 0:
                return 0

            grid[i][j] = 0
            area = 1
            area += dfs(i-1, j)
            area += dfs(i+1, j)
            area += dfs(i, j-1)
            area += dfs(i, j+1)

            return area

        
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area
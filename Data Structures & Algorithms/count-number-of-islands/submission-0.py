class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            n, m = len(grid), len(grid[0])
            
            if i<0 or i>=n or j<0 or j>=m or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count +=1
                    dfs(i , j)

        return count


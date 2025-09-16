class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    
    def dfs(self, grid, i, j):
        row = len(grid)
        col = len(grid[0])

        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 1:
            return 0

        count = 1
        grid[i][j] = 2
        count += self.dfs(grid, i+1, j)
        count += self.dfs(grid, i-1, j)
        count += self.dfs(grid, i, j+1)
        count += self.dfs(grid, i, j-1)

        return count




class Solution:
    def dfs(self, grid, i, j ):
        row = len(grid)
        col = len(grid[0])

        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    result += 1
        
        return result
    
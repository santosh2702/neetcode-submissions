class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=R or j>=C or grid[i][j]=='0':
                return
            grid[i][j] = '0'
            dfs(i+1,j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)
        cnt = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    dfs(i,j); cnt += 1
        return cnt
                



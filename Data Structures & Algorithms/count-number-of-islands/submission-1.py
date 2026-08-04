class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        marked = [[0]*c for _ in range(r)]
        def markIslands(i, j):
            if i < 0 or i >= r or j >= c or j < 0:
                return
            marked[i][j] = 1
            if i+1 < r and grid[i+1][j] == "1" and not marked[i+1][j]:
                markIslands(i+1, j)
            if i > 0 and grid[i-1][j] == "1" and not marked[i-1][j]:
                markIslands(i-1, j)
            if j+1 < c and grid[i][j+1] == "1" and not marked[i][j+1]:
                markIslands(i, j+1)
            if j > 0 and grid[i][j-1] == "1" and not marked[i][j-1]:
                markIslands(i, j-1)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and not marked[i][j]:
                    markIslands(i, j)
                    res += 1
        return res
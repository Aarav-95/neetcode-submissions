class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        temp = 1
        def back(i, j):
            nonlocal res, temp
            grid[i][j] = -1
            if j-1 >= 0 and grid[i][j-1] == 1:
                temp += 1
                back(i, j-1)
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                temp += 1
                back(i, j+1)
            if i-1 >= 0 and grid[i-1][j] == 1:
                temp += 1
                back(i-1, j)
            if i+1 < len(grid) and grid[i+1][j] == 1:
                temp += 1
                back(i+1, j)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    back(i, j)
                    res = max(res, temp)
                    temp = 1
        
        return res
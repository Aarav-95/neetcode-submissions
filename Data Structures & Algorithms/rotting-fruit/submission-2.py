class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        step = 0
        directions = ((1,0), (0,1), (-1,0), (0,-1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q:
            queue_len = len(q)
            for i in range(queue_len):
                row, col = q.popleft()

                for dir_x, dir_y in directions:
                    if row+dir_x < len(grid) and row+dir_x >= 0 and col+dir_y < len(grid[0]) and col+dir_y >= 0 and grid[row+dir_x][col+dir_y] == 1:
                        grid[row+dir_x][col+dir_y] = 2
                        q.append((row+dir_x, col+dir_y))
            
            if q:
                step += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return step
        

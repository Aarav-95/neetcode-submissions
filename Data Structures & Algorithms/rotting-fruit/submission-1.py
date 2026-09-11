class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        step = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i, j in directions:
                    if r+i >= 0 and r+i < len(grid) and c+j >= 0 and c+j < len(grid[0]) and grid[r+i][c+j] == 1:
                        grid[r+i][c+j] = 2
                        q.append((r+i, c+j))
            if q:
                step += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return step
                
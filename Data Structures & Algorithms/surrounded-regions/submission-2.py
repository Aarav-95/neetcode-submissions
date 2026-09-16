class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "T"
            for r, c in directions:
                dfs(i+r, j+c)
            
        
        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board)-1, i)
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        

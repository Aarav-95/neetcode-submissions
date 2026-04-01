class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            freq = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in freq:
                    return False
                else:
                    freq[board[j][i]] = 1
        for i in range(9):
            freq = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in freq:
                    return False
                else:
                    freq[board[i][j]] = 1
        
        for i in range(0, 9, 3):
            freq = {}
            for j in range(9):
                n = j % 3
                r = j // 3
                if board[i+r][n] == '.':
                    continue
                elif board[i+r][n] in freq:
                    return False
                else:
                    freq[board[i+r][n]] = 1
        for i in range(0, 9, 3):
            freq = {}
            for j in range(9):
                n = j % 3
                r = j // 3
                if board[i+r][3+n] == '.':
                    continue
                elif board[i+r][3+n] in freq:
                    return False
                else:
                    freq[board[i+r][3+n]] = 1

        for i in range(0, 9, 3):
            freq = {}
            for j in range(9):
                n = j % 3
                r = j // 3
                if board[i+r][6+n] == '.':
                    continue
                elif board[i+r][6+n] in freq:
                    return False
                else:
                    freq[board[i+r][6+n]] = 1
        return True


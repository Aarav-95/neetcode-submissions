class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        r = len(board)
        c = len(board[0])
        prev = []

        def back(idx, i, j):
            nonlocal prev
            if idx == n:
                return True
            if j > 0 and board[i][j-1] == word[idx] and [i,j-1] not in prev:
                prev.append([i,j])
                if (back(idx+1, i, j-1)):
                    return True
                prev.pop()
            if j < c-1 and board[i][j+1] == word[idx] and [i,j+1] not in prev:
                prev.append([i,j])
                if (back(idx+1, i, j+1)):
                    return True
                prev.pop()
            if i > 0 and board[i-1][j] == word[idx] and [i-1,j] not in prev:
                prev.append([i,j])
                if (back(idx+1, i-1, j)):
                    return True
                prev.pop()
            if i < r-1 and board[i+1][j] == word[idx] and [i+1,j] not in prev:
                prev.append([i,j])
                if (back(idx+1, i+1, j)):
                    return True
                prev.pop()
        
        for i in range(0, r):
            for j in range(0, c):
                if board[i][j] == word[0]:
                    if (back(1, i, j)):
                        return True
                prev = []
        
        return False
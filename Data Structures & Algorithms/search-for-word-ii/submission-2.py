class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        res = []
        def makeTrie(words):
            for word in words:
                cur = root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = Node()
                    cur = cur.children[c]
                
                cur.end = True
                cur.word = word

        makeTrie(words)

        def back(m, n, cur, visited):
            if cur.end == True:
                if cur.word not in res:
                    res.append(cur.word)

            if n-1 >= 0 and (m, n-1) not in visited and board[m][n-1] in cur.children:
                visited.append((m,n))
                back(m, n-1, cur.children[board[m][n-1]], visited)
                visited.remove((m, n))
            
            if n+1 < len(board[0]) and (m, n+1) not in visited and board[m][n+1] in cur.children:
                visited.append((m,n))
                back(m, n+1, cur.children[board[m][n+1]], visited)
                visited.remove((m, n))
            
            if m-1 >= 0 and (m-1, n) not in visited and board[m-1][n] in cur.children:
                visited.append((m,n))
                back(m-1, n, cur.children[board[m-1][n]], visited)
                visited.remove((m, n))
            
            if m+1 < len(board) and (m+1, n) not in visited and board[m+1][n] in cur.children:
                visited.append((m,n))
                back(m+1, n, cur.children[board[m+1][n]], visited)
                visited.remove((m, n))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    back(i, j, root.children[board[i][j]], [])
        
        return res

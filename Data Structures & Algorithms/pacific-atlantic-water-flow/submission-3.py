class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac = set()
        atl = set()
        def dfs(i, j, visit, prevHeight):
            if ((i, j) in visit or i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0])) or heights[i][j] < prevHeight:
                return
            visit.add((i, j))
            for r, c in directions:
                dfs(i+r, j+c, visit, heights[i][j])

        for i in range(len(heights[0])):
            dfs(0, i, pac, heights[0][i])
            dfs(len(heights)-1, i, atl, heights[len(heights)-1][i])

        for i in range(len(heights)):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, len(heights[0])-1, atl, heights[i][len(heights[0])-1])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
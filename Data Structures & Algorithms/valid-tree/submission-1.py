class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {c: [] for c in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        

        cycle = set()
        def dfs(val, prev):
            if val in cycle:
                return False
            cycle.add(val)
            for i in graph[val]:
                if i != prev and dfs(i, val) == False:
                    return False
        
        if dfs(0, None) == False or len(cycle) != n:
            return False
            
        return True
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {c: [] for c in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def dfs(val, prev):
            visited.add(val)
            for i in graph[val]:
                if i != prev and i not in visited:
                    dfs(i, val)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, None)

        return count
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        d = deque([source])
        visited = [False] * n
        visited[source] = True
        while d:
            x = d.popleft()
            if x == destination:
                return True
            for nei in graph[x]:
                if not visited[nei]:
                    d.append(nei)
                    visited[nei] = True
        return False
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        st = [0]
        def dfs(i):
            x = st.pop()
            for nei in rooms[x]:
                if nei not in visited:
                    st.append(nei)
                    visited.add(nei)
                    dfs(nei)
        dfs(0)
        return len(rooms) == len(visited)
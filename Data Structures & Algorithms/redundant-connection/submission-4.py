class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))

        for curr, next in edges:
            u, v = curr, next

            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]

            while next != parent[next]:
                parent[next] = parent[parent[next]]
                next = parent[next]

            if parent[curr] == parent[next]:
                return [u, v]

            parent[next] = curr



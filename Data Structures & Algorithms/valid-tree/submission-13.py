class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjList = {i : [] for i in range(n)}
        edgeCount = 0

        for curr, adj in edges:
            adjList[curr].append(adj)
            adjList[adj].append(curr)
            edgeCount += 1

        if edgeCount != n - 1:
            return False
        
        stack = [0]
        seen = set()
        seen.add(0)

        while stack:
            currNode = stack.pop()
            for adj in adjList[currNode]:
                if adj not in seen:
                    stack.append(adj)
                    seen.add(adj)

        if len(seen) != n:
            return False
            
        return True

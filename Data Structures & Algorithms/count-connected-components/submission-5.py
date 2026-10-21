class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """

        Assuming all nodes are connected to each other (so there is 1 component), and it does not form a cycle

        We know the number of edges = n - 1

        For each increase in components, number of edges will decrement by one, assuming there is still no cycles in any component

        edges + x == n - 1

        x + 1 <- number of components        

        However, if there is a cycle in a component, this means that we have excessive edges that isn't needed to keep all nodes in the component connected to each other

        For each excessive edge, we also increment the number of edges

        Now we need a logic to catch the cycle, and how many excessive edges we have

        """

        seen = set(i for i in range(n))

        adjList = [[] for i in range(n)]

        for curr, adj in edges:
            adjList[curr].append(adj)
            adjList[adj].append(curr)

        count = 0

        while seen:
            queue = deque([seen.pop()])
            while queue:
                curr = queue.popleft()
                queue.extend(adj for adj in adjList[curr] if adj in seen)
                if curr in seen:
                    seen.remove(curr)

            count += 1

        return count






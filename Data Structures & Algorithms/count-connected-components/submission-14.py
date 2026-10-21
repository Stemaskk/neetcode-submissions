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

        Realized that is very difficult and has too many edge cases, so its better to have each node as a component first then build it into a bigger component using the edges        

        """

        parent = list(range(n))
        count = n

        for curr, next in edges:
            while parent[curr] != curr:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]

            while parent[next] != next:
                parent[next] = parent[parent[next]]
                next = parent[next]

            if curr != next:
                parent[next] = curr
                count -= 1


        return count







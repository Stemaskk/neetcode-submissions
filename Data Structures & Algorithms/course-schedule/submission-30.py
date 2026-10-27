class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        adjList = [[] for i in range(numCourses)]
        count = [0] * numCourses

        for curr, prereq in prerequisites:                
            adjList[prereq].append(curr)
            count[curr] += 1
        
        queue = deque([c for c in range(len(count)) if count[c] == 0])
        taken = 0

        while queue:
            curr = queue.popleft()
            taken += 1

            for adj in adjList[curr]:
                count[adj] -= 1
                if count[adj] == 0:
                    queue.append(adj)

        return taken == numCourses
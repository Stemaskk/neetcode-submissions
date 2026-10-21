class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        path = defaultdict(list)

        safe = set()

        for p in prerequisites:
            path[p[1]].append(p[0])

        def DFS(course, count):
            if course in safe:
                return False

            if count == numCourses:
                return True

            if course not in path.keys():
                safe.add(course)
                return False
            
            isLoop = False

            for p in path[course]:
                isLoop = isLoop or DFS(p, count + 1)
            
            if isLoop == False:
                safe.add(course)
            
            return isLoop


        for n in range(numCourses):
            if DFS(n, 0):
                return False

        return True
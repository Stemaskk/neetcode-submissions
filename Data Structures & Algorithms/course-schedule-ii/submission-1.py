class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        path = {i : [] for i in range(numCourses)}

        prereqCount = [0] * numCourses

        for curr, prev in prerequisites:
            path[prev].append(curr)
            prereqCount[curr] += 1

        queue = deque(i for i in range(len(prereqCount)) if prereqCount[i] == 0)

        result = []

        while queue:
            currCourse = queue.popleft()
            result.append(currCourse)

            for i in path[currCourse]:
                prereqCount[i] -= 1

                if prereqCount[i] == 0:
                    queue.append(i)

        return result if len(result) == numCourses else []
            


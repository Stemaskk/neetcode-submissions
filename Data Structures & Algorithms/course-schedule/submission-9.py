class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        path = defaultdict(list)

        courseLeft = [0] * numCourses

        for p in prerequisites:
            path[p[1]].append(p[0])
            courseLeft[p[0]] += 1

        queue = deque()

        for i in range(numCourses):
            if not courseLeft[i]:
                queue.append(i)
        
        while queue:
            currCourse = queue.popleft()

            if currCourse in path.keys():
                for p in path[currCourse]:
                    courseLeft[p] -= 1
                    if courseLeft[p] == 0:
                        queue.append(p)

        return all(course == 0 for course in courseLeft)

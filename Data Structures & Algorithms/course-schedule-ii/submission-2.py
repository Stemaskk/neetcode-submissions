class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        path = {i : [] for i in range(numCourses)}

        prereqCount = [0] * numCourses

        for curr, prev in prerequisites:
            path[prev].append(curr)
            prereqCount[curr] += 1

        result = [i for i in range(len(prereqCount)) if prereqCount[i] == 0]
        i = 0

        while i < len(result):
            currCourse = result[i]
            i += 1

            for clear in path[currCourse]:
                prereqCount[clear] -= 1
                if prereqCount[clear] == 0:
                    result.append(clear)

        return result if len(result) == numCourses else []
            


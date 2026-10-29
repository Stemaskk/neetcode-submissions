class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

#{i : [] for i in range(numCourses)}
        prereq = defaultdict(list)
        count = [0] * numCourses
        result = []

        for curr, pre in prerequisites:
            prereq[pre].append(curr)
            count[curr] += 1

        queue = deque(i for i in range(numCourses) if count[i] == 0)

        while queue:
            curr = queue.popleft()
            result.append(curr)
            if count[curr] < 0:
                    return []

            for cleared in prereq[curr]:
                count[cleared] -= 1
                

                if count[cleared] == 0:
                    queue.append(cleared)

        for i in range(numCourses):
            if count[i] != 0:
                return []

        return result
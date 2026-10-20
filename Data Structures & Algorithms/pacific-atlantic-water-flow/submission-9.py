class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []

        pacific = set()
        atlantic = set()
        pqueue = deque([])
        aqueue = deque([])

        totalRow = len(heights)
        totalCol = len(heights[0])

        for r in range(totalRow):
            pqueue.append((r, 0))
            aqueue.append((r, totalCol - 1))
            pacific.add((r, 0))
            atlantic.add((r, totalCol - 1))

        for c in range(totalCol):
            pqueue.append((0, c))
            aqueue.append((totalRow - 1, c))
            pacific.add((0, c))
            atlantic.add((totalRow - 1, c))

        while pqueue:
            currRow, currCol = pqueue.popleft()

            if currRow - 1 >= 0 and (currRow - 1, currCol) not in pacific and heights[currRow - 1][currCol] >= heights[currRow][currCol]:
                pqueue.append((currRow - 1, currCol))
                pacific.add((currRow - 1, currCol))

            if currRow + 1 < totalRow and (currRow + 1, currCol) not in pacific and heights[currRow + 1][currCol] >= heights[currRow][currCol]:
                pqueue.append((currRow + 1, currCol))
                pacific.add((currRow + 1, currCol))

            if currCol + 1 < totalCol and (currRow, currCol + 1) not in pacific and heights[currRow][currCol + 1] >= heights[currRow][currCol]:
                pqueue.append((currRow, currCol + 1))
                pacific.add((currRow, currCol + 1))

            if currCol - 1 >= 0 and (currRow, currCol - 1) not in pacific and heights[currRow][currCol - 1] >= heights[currRow][currCol]:
                pqueue.append((currRow, currCol - 1))
                pacific.add((currRow, currCol - 1))

        while aqueue:
            currRow, currCol = aqueue.popleft()

            if currRow - 1 >= 0 and (currRow - 1, currCol) not in atlantic and heights[currRow - 1][currCol] >= heights[currRow][currCol]:
                aqueue.append((currRow - 1, currCol))
                atlantic.add((currRow - 1, currCol))

            if currRow + 1 < totalRow and (currRow + 1, currCol) not in atlantic and heights[currRow + 1][currCol] >= heights[currRow][currCol]:
                aqueue.append((currRow + 1, currCol))
                atlantic.add((currRow + 1, currCol))

            if currCol + 1 < totalCol and (currRow, currCol + 1) not in atlantic and heights[currRow][currCol + 1] >= heights[currRow][currCol]:
                aqueue.append((currRow, currCol + 1))
                atlantic.add((currRow, currCol + 1))

            if currCol - 1 >= 0 and (currRow, currCol - 1) not in atlantic and heights[currRow][currCol - 1] >= heights[currRow][currCol]:
                aqueue.append((currRow, currCol - 1))
                atlantic.add((currRow, currCol - 1))

        for r in range(totalRow):
            for c in range(totalCol):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
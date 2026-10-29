class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        totalRow = len(grid)
        totalCol = len(grid[0])

        fresh = set()

        queue = deque()
        time = 0

        for r in range(totalRow):
            for c in range(totalCol):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh.add((r, c))

        if not fresh:
            return 0

        while queue and fresh:
            time += 1
            size = len(queue)
            for i in range(size):
                currRow, currCol = queue.popleft()

                if currRow + 1 < totalRow and (currRow + 1, currCol) in fresh:
                    fresh.remove((currRow + 1, currCol))
                    queue.append((currRow + 1, currCol))

                if currRow - 1 >= 0 and (currRow - 1, currCol) in fresh:
                    fresh.remove((currRow - 1, currCol))
                    queue.append((currRow - 1, currCol))

                if currCol + 1 < totalCol and (currRow, currCol + 1) in fresh:
                    fresh.remove((currRow, currCol + 1))
                    queue.append((currRow, currCol + 1))

                if currCol - 1 >= 0 and (currRow, currCol - 1) in fresh:
                    fresh.remove((currRow, currCol - 1))
                    queue.append((currRow, currCol - 1))

        if fresh:
            return -1

        return time

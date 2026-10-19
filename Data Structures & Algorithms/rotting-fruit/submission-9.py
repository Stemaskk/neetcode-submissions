class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque([])
        totalRows = len(grid)
        totalCols = len(grid[0])
        freshCount = 0


        for r in range(totalRows):
            for c in range(totalCols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    freshCount += 1
                
        time = 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                north = row - 1
                south = row + 1
                west = col - 1
                east = col + 1

                if north >= 0 and grid[north][col] == 1:
                    queue.append((north, col))
                    grid[north][col] = 2
                    freshCount -= 1

                if south < totalRows and grid[south][col] == 1:
                    queue.append((south, col))
                    grid[south][col] = 2
                    freshCount -= 1

                if west >= 0 and grid[row][west] == 1:
                    queue.append((row, west))
                    grid[row][west] = 2
                    freshCount -= 1

                if east < totalCols and grid[row][east] == 1:
                    queue.append((row, east))
                    grid[row][east] = 2
                    freshCount -= 1
            if queue:
                time += 1

        if freshCount != 0:
            return -1

        return time

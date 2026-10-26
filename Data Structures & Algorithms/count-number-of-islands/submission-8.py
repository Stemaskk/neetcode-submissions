class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        totalRow = len(grid)
        totalCol = len(grid[0])

        count = 0

        def BFS(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "*"

            while queue:
                currRow, currCol = queue.popleft()

                if currRow - 1 >= 0 and grid[currRow - 1][currCol] == "1":
                    queue.append((currRow - 1, currCol))
                    grid[currRow - 1][currCol] = "*"

                if currRow + 1 < totalRow and grid[currRow + 1][currCol] == "1":
                    queue.append((currRow + 1, currCol))
                    grid[currRow + 1][currCol] = "*"

                if currCol - 1 >= 0 and grid[currRow][currCol - 1] == "1":
                    queue.append((currRow, currCol - 1))
                    grid[currRow][currCol - 1] = "*"

                if currCol + 1 < totalCol and grid[currRow][currCol + 1] == "1":
                    queue.append((currRow, currCol + 1))
                    grid[currRow][currCol + 1] = "*"


        for r in range(totalRow):
            for c in range(totalCol):
                if grid[r][c] == "1":
                    BFS(r, c)
                    count += 1

        return count
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])
        seen = set([])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    seen.add((r, c))

        while queue:
            row, col = queue.popleft()

            if row - 1 >= 0 and (row - 1, col) not in seen and grid[row - 1][col] > 0:
                queue.append((row - 1, col))
                seen.add((row - 1, col))
                grid[row - 1][col] = min(grid[row - 1][col], grid[row][col] + 1)

            if row + 1 < rows and (row + 1, col) not in seen and grid[row + 1][col] > 0:
                queue.append((row + 1, col))
                seen.add((row + 1, col))
                grid[row + 1][col] = min(grid[row + 1][col], grid[row][col] + 1)

            if col + 1 < cols and (row, col + 1) not in seen and grid[row][col + 1] > 0:
                queue.append((row, col + 1))
                seen.add((row, col + 1))
                grid[row][col + 1] = min(grid[row][col + 1], grid[row][col] + 1)

            if col - 1 >= 0 and (row, col - 1) not in seen and grid[row][col - 1] > 0:
                queue.append((row, col - 1))
                seen.add((row, col - 1))
                grid[row][col - 1] = min(grid[row][col - 1], grid[row][col] + 1)


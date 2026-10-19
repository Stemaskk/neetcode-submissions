class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def found(row, col):
            if row > rows - 1 or row < 0 or col > cols - 1 or col < 0 or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + found(row - 1, col) + found(row + 1, col) + found(row, col - 1) + found(row, col + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, found(r, c))

        return maxArea
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        cols = len(grid)
        rows = len(grid[0])

        def found(col, row):
            if col > cols - 1 or col < 0 or row > rows - 1 or row < 0 or grid[col][row] != "1":
                return
            grid[col][row] = "*"

            found(col, row - 1)
            found(col, row + 1)
            found(col - 1, row)
            found(col + 1, row)

        for c in range(cols):
            for r in range(rows):
                if grid[c][r] == "1":
                    count += 1
                    found(c, r)

        return count
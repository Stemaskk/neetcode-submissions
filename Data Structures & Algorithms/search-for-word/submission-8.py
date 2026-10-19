class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board[0]) - 1
        cols = len(board) - 1
        seen = set()

        def backtrack(col, row, i):

            if row > rows or row < 0 or col > cols or col < 0 or board[col][row] != word[i] or (col, row) in seen:
                return False

            if i == len(word) - 1:
                return True
            
            seen.add((col, row))

            found = backtrack(col, row - 1, i + 1) or backtrack(col, row + 1, i + 1) or backtrack(col - 1, row, i + 1) or backtrack(col + 1, row, i + 1)

            seen.remove((col, row))

            return found

        for c in range(cols + 1):
            for r in range(rows + 1):
                if backtrack(c, r, 0):
                    return True

        return False
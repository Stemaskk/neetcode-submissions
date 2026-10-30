class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        colMask = 0
        posDiag = 0
        negDiag = 0
        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            nonlocal colMask, posDiag, negDiag

            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if ((colMask & (1 << col)) or (posDiag & (1 << (row + col))) or (negDiag & (1 << (row - col + n)))):
                    continue

                colMask ^= (1 << col)
                posDiag ^= (1 << (row + col))
                negDiag ^= (1 << (row - col + n))

                board[row][col] = "Q"

                backtrack(row + 1)

                colMask ^= (1 << col)
                posDiag ^= (1 << (row + col))
                negDiag ^= (1 << (row - col + n))

                board[row][col] = "."


        backtrack(0)
        return result
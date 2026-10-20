class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        notEnclosed = set()

        queue = deque()

        totalRow = len(board)
        totalCol = len(board[0])

        for r in range(totalRow):

            if board[r][0] == 'O':
                queue.append((r, 0))
                notEnclosed.add((r, 0))

            if board[r][totalCol - 1] == 'O':
                queue.append((r, totalCol - 1))
                notEnclosed.add((r, totalCol - 1))
        
        for c in range(1, totalCol - 1):

            if board[0][c] == 'O':
                queue.append((0, c))
                notEnclosed.add((0, c))

            if board[totalRow - 1][c] == 'O':
                queue.append((totalRow - 1, c))
                notEnclosed.add((totalRow - 1, c))

        while queue:
            currRow, currCol = queue.popleft()

            if currRow - 1 >= 0 and (currRow - 1, currCol) not in notEnclosed and board[currRow - 1][currCol] == 'O':
                queue.append((currRow - 1, currCol))
                notEnclosed.add((currRow - 1, currCol))

            if currRow + 1 < totalRow and (currRow + 1, currCol) not in notEnclosed and board[currRow + 1][currCol] == 'O':
                queue.append((currRow + 1, currCol))
                notEnclosed.add((currRow + 1, currCol))

            if currCol - 1 >= 0 and (currRow, currCol - 1) not in notEnclosed and board[currRow][currCol - 1] == 'O':
                queue.append((currRow, currCol - 1))
                notEnclosed.add((currRow, currCol - 1))

            if currCol + 1 < totalCol and (currRow, currCol + 1) not in notEnclosed and board[currRow][currCol + 1] == 'O':
                queue.append((currRow, currCol + 1))
                notEnclosed.add((currRow, currCol + 1))

        for r in range(totalRow):
            for c in range(totalCol):
                if board[r][c] == 'O' and (r, c) not in notEnclosed:
                    board[r][c] = 'X'



